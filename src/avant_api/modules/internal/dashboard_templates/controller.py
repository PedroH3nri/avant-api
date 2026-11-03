"""Modelos prontos de dashboard: /api/v1/internal/dashboard-templates.

Pede a equipe Groone com 2FA e ``internal.dashboard_templates.manage``. Cada modelo é da Groone
ou dos clientes, pode ser limitado a papéis e um por público abre no início de quem ainda não
tem dashboard. Mudar um modelo não mexe nos dashboards já copiados dele.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.dashboards.services import MANAGE_TEMPLATES
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.dashboard_templates.dependencies import (
    dashboard_template_service,
)
from avant_api.modules.internal.dashboard_templates.dto import (
    DashboardTemplateIn,
    ManagedTemplateOut,
    TemplateRolesOut,
)
from avant_api.modules.internal.dashboard_templates.service import DashboardTemplateService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal/dashboard-templates", tags=["internal"])


@router.get("")
def index(
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> ItemsOut[ManagedTemplateOut]:
    """Todos os modelos, os da Groone primeiro e o de início no topo de cada público."""
    return ItemsOut(items=service.list(actor))


@router.get("/roles")
def roles(
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> TemplateRolesOut:
    """Os papéis da equipe Groone e os predefinidos dos clientes, para limitar quem vê."""
    return service.roles(actor)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: DashboardTemplateIn,
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> ManagedTemplateOut:
    """Salva um modelo novo, fora do início."""
    return service.create(actor, body)


@router.get("/{template_id}")
def show(
    template_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> ManagedTemplateOut:
    """Um modelo, para editar."""
    return service.get(actor, template_id)


@router.put("/{template_id}")
def update(
    template_id: uuid.UUID,
    body: DashboardTemplateIn,
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> ManagedTemplateOut:
    """Troca tudo do modelo; mudar o público tira a marca de início."""
    return service.update(actor, template_id, body)


@router.delete("/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    template_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> None:
    """Apaga um modelo; os dashboards já copiados dele ficam."""
    service.delete(actor, template_id)


@router.put("/{template_id}/home")
def set_home(
    template_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE_TEMPLATES)),
    service: DashboardTemplateService = Depends(dashboard_template_service),
) -> ManagedTemplateOut:
    """Marca o modelo de início do público dele, no lugar do anterior."""
    return service.set_home(actor, template_id)
