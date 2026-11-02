"""Dashboards: /api/v1/dashboards.

Ver, escolher o próprio e rodar widgets pedem ``reports.view`` (e que a pessoa veja o
dashboard); criar, duplicar, partir de um modelo e marcar o padrão da Empresa pedem
``dashboards.manage``. Editar e apagar são do dono ou de quem tem ``dashboards.manage``,
conferido no avant-core. Como os relatórios, na Company Groone só abrem pela sessão com 2FA.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Path, Query, status

from avant_api.app.security import require_report
from avant_api.modules.dashboards.dependencies import dashboard_service
from avant_api.modules.dashboards.dto import (
    DashboardChoiceIn,
    DashboardIn,
    DashboardOut,
    DashboardPageOut,
    DashboardTemplateOut,
    HomeDashboardOut,
    WidgetRunIn,
)
from avant_api.modules.dashboards.service import DashboardService
from avant_api.modules.reports.dto import ReportResultOut
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/dashboards", tags=["dashboards"])


@router.get("")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardPageOut:
    """Os dashboards que a pessoa vê, o padrão primeiro; ``q`` busca no nome."""
    return service.page(actor, query, page)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: DashboardIn,
    actor: Actor = Depends(require_report("dashboards.manage")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardOut:
    """Salva um dashboard novo, de quem cria."""
    return service.create(actor, body)


@router.get("/home")
def home(
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> HomeDashboardOut:
    """O dashboard que abre para a pessoa: o que ela escolheu, senão o padrão da Empresa."""
    return service.home(actor)


@router.put("/home", status_code=status.HTTP_204_NO_CONTENT)
def choose(
    body: DashboardChoiceIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> None:
    """Escolhe o dashboard que abre para a pessoa; vazio volta para o padrão da Empresa."""
    service.choose(actor, body.dashboard_id)


@router.put("/default", status_code=status.HTTP_204_NO_CONTENT)
def set_default(
    body: DashboardChoiceIn,
    actor: Actor = Depends(require_report("dashboards.manage")),
    service: DashboardService = Depends(dashboard_service),
) -> None:
    """Marca o dashboard padrão da Empresa (visível para a Empresa inteira); vazio tira."""
    service.set_default(actor, body.dashboard_id)


@router.get("/templates")
def templates(
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> ItemsOut[DashboardTemplateOut]:
    """Os modelos prontos da Empresa ativa, com o nome nos três idiomas."""
    return ItemsOut(items=service.templates(actor))


@router.post("/templates/{key}", status_code=status.HTTP_201_CREATED)
def create_from_template(
    key: str,
    actor: Actor = Depends(require_report("dashboards.manage")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardOut:
    """Cria um dashboard privado a partir de um modelo, com o nome no idioma da pessoa."""
    return service.create_from_template(actor, key)


@router.post("/templates/{key}/widgets/{widget_id}/run")
def run_template(
    body: WidgetRunIn,
    key: str = Path(max_length=40),
    widget_id: str = Path(max_length=40),
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> ReportResultOut:
    """Roda um widget de um modelo pronto, para a tela inicial de quem ainda não tem dashboard."""
    return service.run_template(actor, key, widget_id, body)


@router.get("/{dashboard_id}")
def show(
    dashboard_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardOut:
    """Um dashboard que a pessoa vê; o privado de outra pessoa é 404."""
    return service.get(actor, dashboard_id)


@router.put("/{dashboard_id}")
def update(
    dashboard_id: uuid.UUID,
    body: DashboardIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardOut:
    """Troca tudo do dashboard, menos o dono (o dono ou quem tem dashboards.manage)."""
    return service.update(actor, dashboard_id, body)


@router.delete("/{dashboard_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    dashboard_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> None:
    """Apaga um dashboard (o dono ou quem tem dashboards.manage)."""
    service.delete(actor, dashboard_id)


@router.post("/{dashboard_id}/duplicate", status_code=status.HTTP_201_CREATED)
def duplicate(
    dashboard_id: uuid.UUID,
    actor: Actor = Depends(require_report("dashboards.manage")),
    service: DashboardService = Depends(dashboard_service),
) -> DashboardOut:
    """Faz uma cópia privada, de quem duplica, com " (cópia)" no nome."""
    return service.duplicate(actor, dashboard_id)


@router.post("/{dashboard_id}/widgets/{widget_id}/run")
def run(
    dashboard_id: uuid.UUID,
    body: WidgetRunIn,
    widget_id: str = Path(max_length=40),
    actor: Actor = Depends(require_report("reports.view")),
    service: DashboardService = Depends(dashboard_service),
) -> ReportResultOut:
    """Roda um widget de relatório ou de consulta, com os filtros da tela ou os gravados, na
    moeda de quem olha e só nos sites e clientes que ela enxerga."""
    return service.run(actor, dashboard_id, widget_id, body)
