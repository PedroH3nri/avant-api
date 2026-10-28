"""Métricas e relatórios: /api/v1/metrics/catalog e /api/v1/reports/query."""

from avant_core.access.models import Actor
from avant_core.identity.enums import Locale
from fastapi import APIRouter, Depends, Response

from avant_api.app.security import require
from avant_api.modules.reports.dependencies import report_service
from avant_api.modules.reports.dto import MetricCatalogOut, ReportQueryIn, ReportResultOut
from avant_api.modules.reports.service import ReportService

router = APIRouter(tags=["reports"])


@router.get("/metrics/catalog")
def catalog(
    _: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> MetricCatalogOut:
    """Métricas e dimensões que a pessoa pode pedir, com os textos nos três idiomas."""
    return service.catalog()


@router.post("/reports/query")
def query(
    body: ReportQueryIn,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> ReportResultOut:
    """Roda uma consulta sem salvar (a pré-visualização do construtor de relatórios)."""
    return service.query(actor, body)


@router.post("/reports/query/export")
def export(
    body: ReportQueryIn,
    locale: Locale = Locale.PT,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> Response:
    """A mesma consulta em CSV, com o cabeçalho no idioma pedido."""
    return Response(
        content=service.export(actor, body, locale),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": 'attachment; filename="relatorio.csv"'},
    )
