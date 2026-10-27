"""Service dos relatórios: traduz a definição para o motor de consulta do avant-core.

O motor confere tudo contra o catálogo e soma no banco com RLS, só nos sites que a pessoa
enxerga. As consultas têm um limite de taxa próprio, por pessoa e Empresa.
"""

import time
from collections.abc import Iterator
from contextlib import contextmanager

from avant_core.company.service import Actor
from avant_core.identity.model import Locale
from avant_core.metrics.catalog import DIMENSIONS, visible_metrics
from avant_core.metrics.query import (
    MAX_DAYS,
    MAX_LIMIT,
    FilterOperator,
    QueryResult,
    RelativePeriod,
)
from avant_core.metrics.report_service import run_query
from avant_core.shared.clock import Clock
from sqlalchemy.exc import OperationalError

from avant_api.app.errors import QueryTooHeavy, RateLimited
from avant_api.app.limits import REPORTS, Bucket
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.reports.csv_export import to_csv
from avant_api.modules.reports.dto import (
    DimensionOut,
    MetricCatalogOut,
    MetricOut,
    ReportQueryIn,
    ReportResultOut,
)

QUERY_CANCELED = "57014"


class ReportService:
    """Catálogo de métricas e consultas de relatório com limite de taxa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, bucket: Bucket) -> None:
        self._uows = uows
        self._clock = clock
        self._bucket = bucket

    def catalog(self) -> MetricCatalogOut:
        """Métricas e dimensões que um cliente pode pedir, nos três idiomas."""
        return MetricCatalogOut(
            metrics=[MetricOut.of(metric) for metric in visible_metrics(internal=False)],
            dimensions=[DimensionOut.of(dimension) for dimension in DIMENSIONS],
            operators=list(FilterOperator),
            periods=list(RelativePeriod),
            max_days=MAX_DAYS,
            max_limit=MAX_LIMIT,
        )

    def query(self, actor: Actor, body: ReportQueryIn) -> ReportResultOut:
        """Roda uma consulta sem salvar."""
        return ReportResultOut.of(self._run(actor, body))

    def export(self, actor: Actor, body: ReportQueryIn, locale: Locale) -> str:
        """A mesma consulta em CSV, com o cabeçalho no idioma pedido."""
        return to_csv(self._run(actor, body), body, locale)

    def _run(self, actor: Actor, body: ReportQueryIn) -> QueryResult:
        """Aplica o limite de taxa e roda o motor de consulta na Empresa ativa."""
        taken = self._bucket.take(
            f"reports:{actor.company_id}:{actor.user_id}", REPORTS, time.time()
        )
        if not taken.allowed:
            raise RateLimited(
                "muitas consultas de relatório", retry_after=max(taken.retry_after, 1)
            )
        with _statement_timeout():
            return run_query(
                self._uows.uow(actor.company_id),
                actor=actor,
                definition=body.definition(),
                clock=self._clock,
            )


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
