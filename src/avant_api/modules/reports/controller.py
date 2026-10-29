"""Métricas e relatórios: /api/v1/metrics/catalog, /api/v1/reports/query e os relatórios
salvos em /api/v1/reports.

Ver, rodar e exportar pedem ``reports.view`` (e que a pessoa veja o relatório: privado,
Empresa ou papéis); criar, duplicar e partir de um modelo pedem ``reports.manage``. Editar e
apagar são do dono ou de quem tem ``reports.manage``, conferido no avant-core.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.identity.enums import Locale
from avant_core.reports.enums import ReportScope
from fastapi import APIRouter, Depends, Query, Response, status

from avant_api.app.security import require
from avant_api.modules.reports.dependencies import report_service
from avant_api.modules.reports.dto import (
    ExportFormat,
    MetricCatalogOut,
    ReportPageOut,
    ReportQueryIn,
    ReportResultOut,
    ReportTemplateOut,
    SavedReportIn,
    SavedReportOut,
)
from avant_api.modules.reports.service import ReportService
from avant_api.shared.dto import ItemsOut

router = APIRouter(tags=["reports"])

MEDIA_TYPES = {
    "csv": "text/csv; charset=utf-8",
    "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
}


@router.get("/metrics/catalog")
def catalog(
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> MetricCatalogOut:
    """Métricas e dimensões que a pessoa pode pedir, com os textos nos três idiomas, e as
    métricas personalizadas da Empresa ativa."""
    return service.catalog(actor)


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
        media_type=MEDIA_TYPES["csv"],
        headers={"Content-Disposition": 'attachment; filename="relatorio.csv"'},
    )


@router.get("/reports")
def index(
    scope: ReportScope | None = None,
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> ReportPageOut:
    """Uma página dos relatórios salvos que a pessoa vê, o mais recente primeiro; ``scope``
    separa os da pessoa (``mine``) dos compartilhados (``shared``) e a busca olha o nome."""
    return service.page_saved(actor, scope, query, page)


@router.post("/reports", status_code=status.HTTP_201_CREATED)
def create(
    body: SavedReportIn,
    actor: Actor = Depends(require("reports.manage")),
    service: ReportService = Depends(report_service),
) -> SavedReportOut:
    """Salva um relatório novo, de quem cria."""
    return service.create_saved(actor, body)


@router.get("/reports/templates")
def templates(
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> ItemsOut[ReportTemplateOut]:
    """Os modelos prontos da Groone, com o nome nos três idiomas."""
    return ItemsOut(items=service.templates())


@router.post("/reports/templates/{key}", status_code=status.HTTP_201_CREATED)
def create_from_template(
    key: str,
    actor: Actor = Depends(require("reports.manage")),
    service: ReportService = Depends(report_service),
) -> SavedReportOut:
    """Cria um relatório privado a partir de um modelo, com o nome no idioma da pessoa."""
    return service.create_from_template(actor, key)


@router.get("/reports/{report_id}")
def show(
    report_id: uuid.UUID,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> SavedReportOut:
    """Um relatório salvo que a pessoa vê; o privado de outra pessoa é 404."""
    return service.get_saved(actor, report_id)


@router.put("/reports/{report_id}")
def update(
    report_id: uuid.UUID,
    body: SavedReportIn,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> SavedReportOut:
    """Troca tudo do relatório, menos o dono (o dono ou quem tem reports.manage)."""
    return service.update_saved(actor, report_id, body)


@router.delete("/reports/{report_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    report_id: uuid.UUID,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> None:
    """Apaga um relatório (o dono ou quem tem reports.manage)."""
    service.delete_saved(actor, report_id)


@router.post("/reports/{report_id}/duplicate", status_code=status.HTTP_201_CREATED)
def duplicate(
    report_id: uuid.UUID,
    actor: Actor = Depends(require("reports.manage")),
    service: ReportService = Depends(report_service),
) -> SavedReportOut:
    """Faz uma cópia privada, de quem duplica, com " (cópia)" no nome."""
    return service.duplicate_saved(actor, report_id)


@router.post("/reports/{report_id}/run")
def run(
    report_id: uuid.UUID,
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> ReportResultOut:
    """Roda o relatório na moeda de quem roda, só nos sites que ela enxerga."""
    return service.run_saved(actor, report_id)


@router.get("/reports/{report_id}/export")
def export_saved(
    report_id: uuid.UUID,
    locale: Locale = Locale.PT,
    file_format: ExportFormat = Query("csv", alias="format"),
    actor: Actor = Depends(require("reports.view")),
    service: ReportService = Depends(report_service),
) -> Response:
    """O relatório salvo em CSV ou XLSX, com o cabeçalho no idioma pedido."""
    return Response(
        content=service.export_saved(actor, report_id, locale, file_format),
        media_type=MEDIA_TYPES[file_format],
        headers={"Content-Disposition": f'attachment; filename="relatorio.{file_format}"'},
    )
