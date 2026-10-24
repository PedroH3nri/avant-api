"""Métricas e relatórios: /api/v1/metrics/catalog e /api/v1/reports/query.

A rota só traduz a definição para o motor de consulta do avant-core, que confere tudo
contra o catálogo, soma no banco com RLS e só os sites que a pessoa enxerga. As consultas
têm um limite de taxa próprio, por pessoa e Empresa, além do das chaves de API.
"""

import csv
import io
import time
from collections.abc import Iterator
from contextlib import contextmanager
from decimal import Decimal

from avant_core.company.application import Actor
from avant_core.identity.domain import Locale
from avant_core.metrics.catalog import (
    DIMENSIONS,
    DIMENSIONS_BY_KEY,
    METRICS_BY_KEY,
    visible_metrics,
)
from avant_core.metrics.query import (
    MAX_DAYS,
    MAX_LIMIT,
    FilterOperator,
    QueryResult,
    RelativePeriod,
)
from avant_core.metrics.reports import run_query
from fastapi import APIRouter, Depends, Response
from sqlalchemy.exc import OperationalError

from avant_api.deps import get_services, require
from avant_api.errors import QueryTooHeavy, RateLimited
from avant_api.limits import REPORTS
from avant_api.schemas import (
    DimensionOut,
    MetricCatalogOut,
    MetricOut,
    ReportQueryIn,
    ReportResultOut,
    dimension_text,
)
from avant_api.services import Services

router = APIRouter(tags=["reports"])

QUERY_CANCELED = "57014"
FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


@router.get("/metrics/catalog")
def catalog(actor: Actor = Depends(require("reports.view"))) -> MetricCatalogOut:
    """Métricas e dimensões que a pessoa pode pedir, com os textos nos três idiomas."""
    return MetricCatalogOut(
        metrics=[MetricOut.of(metric) for metric in visible_metrics(internal=False)],
        dimensions=[DimensionOut.of(dimension) for dimension in DIMENSIONS],
        operators=list(FilterOperator),
        periods=list(RelativePeriod),
        max_days=MAX_DAYS,
        max_limit=MAX_LIMIT,
    )


@router.post("/reports/query")
def query(
    body: ReportQueryIn,
    actor: Actor = Depends(require("reports.view")),
    services: Services = Depends(get_services),
) -> ReportResultOut:
    """Roda uma consulta sem salvar (a pré-visualização do construtor de relatórios)."""
    return ReportResultOut.of(_run(body, actor, services))


@router.post("/reports/query/export")
def export(
    body: ReportQueryIn,
    locale: Locale = Locale.PT,
    actor: Actor = Depends(require("reports.view")),
    services: Services = Depends(get_services),
) -> Response:
    """A mesma consulta em CSV, com o cabeçalho no idioma pedido."""
    result = _run(body, actor, services)
    return Response(
        content=_csv(result, body, locale),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="relatorio.csv"'},
    )


def _run(body: ReportQueryIn, actor: Actor, services: Services) -> QueryResult:
    """Aplica o limite de taxa e roda o motor de consulta na Empresa ativa."""
    taken = services.bucket.take(
        f"reports:{actor.company_id}:{actor.user_id}", REPORTS, time.time()
    )
    if not taken.allowed:
        raise RateLimited("muitas consultas de relatório", retry_after=max(taken.retry_after, 1))
    with _statement_timeout():
        return run_query(
            services.uow(actor.company_id),
            actor=actor,
            definition=body.definition(),
            clock=services.clock,
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


def _csv(result: QueryResult, body: ReportQueryIn, locale: Locale) -> str:
    """Uma linha por grupo: dimensões (sites e networks pelo nome) e depois as métricas."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    header = [DIMENSIONS_BY_KEY[key].label.text(locale) for key in body.dimensions]
    header += [METRICS_BY_KEY[key].label.text(locale) for key in body.metrics]
    if body.compare:
        header += [f"{METRICS_BY_KEY[key].label.text(locale)} (anterior)" for key in body.metrics]
    writer.writerow(header)
    for row in result.rows:
        cells = []
        for key in body.dimensions:
            text = dimension_text(row.dimensions.get(key))
            cells.append(_safe_cell(result.labels.get(key, {}).get(text or "", text or "")))
        cells += [_number(row.metrics.get(key)) for key in body.metrics]
        if body.compare:
            previous = row.previous or {}
            cells += [_number(previous.get(key)) for key in body.metrics]
        writer.writerow(cells)
    return buffer.getvalue()


def _safe_cell(text: str) -> str:
    """Evita que a planilha rode como fórmula um texto vindo de fora (key-value, domínio)."""
    return f"'{text}" if text.startswith(FORMULA_PREFIXES) else text


def _number(value: Decimal | None) -> str:
    """Número sem notação científica; vazio quando a razão não tem denominador."""
    return "" if value is None else format(value.normalize(), "f")
