"""Formatos de entrada e saída dos dashboards."""

import uuid
from datetime import datetime
from typing import Any

from avant_core.access.enums import Visibility
from avant_core.dashboards.models import Dashboard, DashboardTemplate
from avant_core.dashboards.services import DashboardInput
from pydantic import BaseModel, Field

from avant_api.modules.reports.dto import LabelOut
from avant_api.shared.dto import PageOut


class DashboardIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    # Filtros e widgets (com schema_version), conferidos no avant-core.
    definition: dict[str, Any]
    visibility: Visibility = Visibility.PRIVATE
    # Papéis que veem o dashboard, só com a visibilidade ``roles``.
    role_ids: list[uuid.UUID] = Field(default_factory=list, max_length=50)

    def input(self) -> DashboardInput:
        """O formulário no formato do caso de uso."""
        return DashboardInput(
            name=self.name,
            definition=self.definition,
            visibility=self.visibility,
            role_ids=tuple(self.role_ids),
            description=self.description,
        )


class DashboardOut(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    definition: dict[str, Any]
    visibility: Visibility
    role_ids: list[uuid.UUID]
    owner_user_id: uuid.UUID
    created_by: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
    # O padrão da Empresa, que abre para quem não escolheu outro.
    is_default: bool
    # A pessoa pode editar e apagar (é a dona ou tem dashboards.manage).
    editable: bool

    @classmethod
    def of(cls, dashboard: Dashboard, editable: bool) -> "DashboardOut":
        """Monta o dashboard com a definição gravada."""
        return cls(
            id=dashboard.id,
            name=dashboard.name,
            description=dashboard.description,
            definition=dashboard.definition,
            visibility=dashboard.visibility,
            role_ids=dashboard.role_ids,
            owner_user_id=dashboard.owner_user_id,
            created_by=dashboard.created_by,
            created_at=dashboard.created_at,
            updated_at=dashboard.updated_at,
            is_default=dashboard.is_default,
            editable=editable,
        )


class DashboardPageOut(PageOut[DashboardOut]):
    """Uma página dos dashboards com o padrão da Empresa e o que a pessoa escolheu abrir."""

    default_id: uuid.UUID | None
    chosen_id: uuid.UUID | None


class DashboardChoiceIn(BaseModel):
    """O dashboard escolhido; vazio tira a escolha."""

    dashboard_id: uuid.UUID | None = None


class DashboardTemplateOut(BaseModel):
    key: str
    name: LabelOut
    definition: dict[str, Any]

    @classmethod
    def of(cls, template: DashboardTemplate) -> "DashboardTemplateOut":
        """Monta o modelo pronto com o nome nos três idiomas."""
        return cls(key=template.key, name=LabelOut(**template.name), definition=template.definition)


class HomeDashboardOut(BaseModel):
    """O dashboard que abre para a pessoa; sem nenhum, o modelo que a tela inicial mostra."""

    dashboard: DashboardOut | None
    template: DashboardTemplateOut | None = None


class WidgetRunIn(BaseModel):
    """Os filtros que a pessoa escolheu na tela; sem eles valem os gravados no dashboard."""

    filters: dict[str, Any] | None = None
