"""Service dos relatórios: consultas avulsas e relatórios salvos, pelo motor do avant-core.

O motor confere tudo contra o catálogo e soma no banco com RLS, só nos sites que a pessoa
enxerga. As consultas têm um limite de taxa próprio, por pessoa e Empresa, e o mesmo vale
para rodar e exportar um relatório salvo. Criar, editar e duplicar pedem ao worker a miniatura
do relatório; a lista só lê a que está guardada.
"""

import time
import uuid
from collections.abc import Iterator
from contextlib import contextmanager
from typing import Any

from avant_core.access.models import Actor
from avant_core.identity.enums import Locale
from avant_core.metrics.catalog import CUSTOM_PREFIX, DIMENSIONS, visible_metrics
from avant_core.metrics.enums import FilterOperator, RelativePeriod
from avant_core.metrics.models import QueryDefinition, QueryResult
from avant_core.metrics.services import (
    CustomMetricSet,
    decode_query,
    list_custom_metrics,
    run_query,
)
from avant_core.metrics.services.query_rules import MAX_DAYS, MAX_LIMIT
from avant_core.reports.enums import ReportScope
from avant_core.reports.models.saved_report import SavedReport
from avant_core.reports.services import (
    PinnedReports,
    create_from_template,
    create_report,
    delete_report,
    duplicate_report,
    get_report,
    list_templates,
    page_reports,
    pin_report,
    pinned_reports,
    run_report,
    unpin_report,
    update_report,
)
from avant_core.shared.clock import Clock
from sqlalchemy.exc import OperationalError

from avant_api.app.errors import QueryTooHeavy, RateLimited
from avant_api.app.limits import REPORTS, Bucket
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import REFRESH_REPORT_PREVIEW, TaskQueue
from avant_api.modules.reports.dto import (
    CustomCatalogMetricOut,
    DimensionOut,
    ExportFormat,
    MetricCatalogOut,
    MetricOut,
    ReportCountsOut,
    ReportPageOut,
    ReportPreviewOut,
    ReportQueryIn,
    ReportResultOut,
    ReportTemplateOut,
    SavedReportIn,
    SavedReportOut,
)
from avant_api.modules.reports.export import to_csv, to_xlsx

QUERY_CANCELED = "57014"


class ReportService:
    """Catálogo de métricas, consultas avulsas e relatórios salvos, com limite de taxa."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, bucket: Bucket, tasks: TaskQueue
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._bucket = bucket
        self._tasks = tasks

    def catalog(self, actor: Actor) -> MetricCatalogOut:
        """Métricas e dimensões que um cliente pode pedir, nos três idiomas, mais as
        personalizadas da Empresa ativa."""
        custom = list_custom_metrics(self._uows.uow(actor.company_id), actor=actor)
        rules = CustomMetricSet(custom)
        return MetricCatalogOut(
            metrics=[MetricOut.of(metric) for metric in visible_metrics(internal=False)],
            custom_metrics=[
                CustomCatalogMetricOut.of(metric, rules.sources(f"custom.{metric.key}"))
                for metric in custom
            ],
            dimensions=[DimensionOut.of(dimension) for dimension in DIMENSIONS],
            operators=list(FilterOperator),
            periods=list(RelativePeriod),
            max_days=MAX_DAYS,
            max_limit=MAX_LIMIT,
        )

    def query(self, actor: Actor, body: ReportQueryIn) -> ReportResultOut:
        """Roda uma consulta sem salvar."""
        return ReportResultOut.of(self._run(actor, body.definition()))

    def export(self, actor: Actor, body: ReportQueryIn, locale: Locale) -> str:
        """A mesma consulta em CSV, com o cabeçalho no idioma pedido."""
        definition = body.definition()
        return to_csv(self._run(actor, definition), definition, locale, self._names(actor))

    def page_saved(
        self, actor: Actor, scope: ReportScope | None, query: str | None, page: int
    ) -> ReportPageOut:
        """Uma página dos relatórios salvos que a pessoa vê, sem os fixados, com a aba, a busca,
        as contagens e as miniaturas."""
        found = page_reports(
            self._uows.uow(actor.company_id), actor=actor, scope=scope, query=query, page=page
        )
        return ReportPageOut(
            items=[
                self._out(actor, report, preview=found.previews.get(report.id))
                for report in found.page.items
            ],
            total=found.page.total,
            page=found.page.page,
            pages=found.page.pages,
            page_size=found.page.page_size,
            counts=ReportCountsOut(
                all=found.counts.all, mine=found.counts.mine, shared=found.counts.shared
            ),
        )

    def pinned(self, actor: Actor) -> list[SavedReportOut]:
        """Os relatórios que a pessoa fixou, na ordem em que fixou, com as miniaturas."""
        found: PinnedReports = pinned_reports(self._uows.uow(actor.company_id), actor=actor)
        return [
            self._out(actor, report, preview=found.previews.get(report.id), pinned=True)
            for report in found.items
        ]

    def pin(self, actor: Actor, report_id: uuid.UUID) -> None:
        """Fixa no topo da lista da pessoa um relatório que ela vê."""
        pin_report(
            self._uows.uow(actor.company_id), actor=actor, report_id=report_id, clock=self._clock
        )

    def unpin(self, actor: Actor, report_id: uuid.UUID) -> None:
        """Solta um relatório fixado da pessoa."""
        unpin_report(self._uows.uow(actor.company_id), actor=actor, report_id=report_id)

    def get_saved(self, actor: Actor, report_id: uuid.UUID) -> SavedReportOut:
        """Um relatório salvo que a pessoa vê."""
        report = get_report(self._uows.uow(actor.company_id), actor=actor, report_id=report_id)
        return self._out(actor, report)

    def create_saved(self, actor: Actor, body: SavedReportIn) -> SavedReportOut:
        """Salva um relatório novo, de quem cria."""
        report = create_report(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return self._refreshed(actor, report)

    def update_saved(
        self, actor: Actor, report_id: uuid.UUID, body: SavedReportIn
    ) -> SavedReportOut:
        """Troca tudo do relatório, menos o dono."""
        report = update_report(
            self._uows.uow(actor.company_id),
            actor=actor,
            report_id=report_id,
            data=body.input(),
            clock=self._clock,
        )
        return self._refreshed(actor, report)

    def delete_saved(self, actor: Actor, report_id: uuid.UUID) -> None:
        """Apaga um relatório que a pessoa pode editar."""
        delete_report(
            self._uows.uow(actor.company_id), actor=actor, report_id=report_id, clock=self._clock
        )

    def duplicate_saved(self, actor: Actor, report_id: uuid.UUID) -> SavedReportOut:
        """Faz uma cópia privada, da pessoa, de um relatório que ela vê."""
        report = duplicate_report(
            self._uows.uow(actor.company_id), actor=actor, report_id=report_id, clock=self._clock
        )
        return self._refreshed(actor, report)

    def templates(self) -> list[ReportTemplateOut]:
        """Os modelos prontos da Groone."""
        return [ReportTemplateOut.of(template) for template in list_templates()]

    def create_from_template(self, actor: Actor, key: str) -> SavedReportOut:
        """Cria um relatório privado a partir de um modelo, no idioma da pessoa."""
        report = create_from_template(
            self._uows.uow(actor.company_id), actor=actor, key=key, clock=self._clock
        )
        return self._refreshed(actor, report)

    def run_saved(self, actor: Actor, report_id: uuid.UUID) -> ReportResultOut:
        """Roda um relatório salvo na moeda de quem roda, só nos sites que ela enxerga."""
        return ReportResultOut.of(self._run_saved(actor, report_id))

    def export_saved(
        self, actor: Actor, report_id: uuid.UUID, locale: Locale, file_format: ExportFormat
    ) -> bytes:
        """O relatório salvo em CSV ou XLSX, com o cabeçalho no idioma pedido."""
        report = get_report(self._uows.uow(actor.company_id), actor=actor, report_id=report_id)
        result = self._run_saved(actor, report_id)
        definition = decode_query(report.query)
        if file_format == "xlsx":
            return to_xlsx(result, definition, locale, self._names(actor))
        return to_csv(result, definition, locale, self._names(actor)).encode()

    def _run(self, actor: Actor, definition: QueryDefinition) -> QueryResult:
        """Aplica o limite de taxa e roda o motor de consulta na Empresa ativa."""
        self._take_slot(actor)
        with _statement_timeout():
            return run_query(
                self._uows.uow(actor.company_id),
                actor=actor,
                definition=definition,
                clock=self._clock,
            )

    def _run_saved(self, actor: Actor, report_id: uuid.UUID) -> QueryResult:
        """Aplica o limite de taxa e roda o relatório salvo."""
        self._take_slot(actor)
        with _statement_timeout():
            return run_report(
                self._uows.uow(actor.company_id),
                actor=actor,
                report_id=report_id,
                clock=self._clock,
            )

    def _take_slot(self, actor: Actor) -> None:
        """Gasta uma consulta do limite da pessoa na Empresa; sem saldo, ``rate_limited``."""
        taken = self._bucket.take(
            f"reports:{actor.company_id}:{actor.user_id}", REPORTS, time.time()
        )
        if not taken.allowed:
            raise RateLimited(
                "muitas consultas de relatório", retry_after=max(taken.retry_after, 1)
            )

    def _names(self, actor: Actor) -> dict[str, str]:
        """O nome de cada métrica personalizada da Empresa, pela chave da consulta."""
        custom = list_custom_metrics(self._uows.uow(actor.company_id), actor=actor)
        return {CUSTOM_PREFIX + metric.key: metric.name for metric in custom}

    def _refreshed(self, actor: Actor, report: SavedReport) -> SavedReportOut:
        """Pede ao worker a miniatura do relatório que acabou de ser gravado e devolve ele."""
        self._tasks.send(REFRESH_REPORT_PREVIEW, str(report.id))
        return self._out(actor, report)

    def _out(
        self,
        actor: Actor,
        report: SavedReport,
        *,
        preview: dict[str, Any] | None = None,
        pinned: bool = False,
    ) -> SavedReportOut:
        """O relatório com a consulta lida, se a pessoa pode editá-lo, a miniatura e se está
        fixado."""
        editable = report.owner_user_id == actor.user_id or actor.grants.can("reports.manage")
        out = SavedReportOut.of(report, decode_query(report.query), editable)
        return out.model_copy(update={"preview": ReportPreviewOut.of(preview), "pinned": pinned})


@contextmanager
def _statement_timeout() -> Iterator[None]:
    """Troca o cancelamento do Postgres por tempo (statement_timeout) por um erro da API."""
    try:
        yield
    except OperationalError as error:
        if getattr(error.orig, "sqlstate", None) == QUERY_CANCELED:
            raise QueryTooHeavy(
                "consulta pesada demais: reduza o período ou as dimensões"
            ) from error
        raise
