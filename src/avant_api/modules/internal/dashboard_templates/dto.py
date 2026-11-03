"""Formatos de entrada e saída dos modelos prontos de dashboard no painel interno."""

import uuid
from datetime import datetime
from typing import Any

from avant_core.access.models import Role
from avant_core.dashboards.enums import TemplateAudience
from avant_core.dashboards.models import DashboardTemplate
from avant_core.dashboards.services import TemplateInput, TemplateRoles
from pydantic import BaseModel, Field


class TemplateNameIn(BaseModel):
    pt: str = Field(min_length=1, max_length=120)
    en: str = Field(default="", max_length=120)
    es: str = Field(default="", max_length=120)


class DashboardTemplateIn(BaseModel):
    """Um modelo pronto; sem papéis, todos do público veem."""

    name: TemplateNameIn
    definition: dict[str, Any]
    audience: TemplateAudience
    role_ids: list[uuid.UUID] = Field(default_factory=list, max_length=50)

    def input(self) -> TemplateInput:
        """O formulário no formato do caso de uso."""
        return TemplateInput(
            name=self.name.model_dump(),
            definition=self.definition,
            audience=self.audience,
            role_ids=tuple(self.role_ids),
        )


class ManagedTemplateOut(BaseModel):
    id: uuid.UUID
    key: str | None
    name: dict[str, str]
    definition: dict[str, Any]
    audience: TemplateAudience
    role_ids: list[uuid.UUID]
    is_home: bool
    updated_at: datetime

    @classmethod
    def of(cls, template: DashboardTemplate) -> "ManagedTemplateOut":
        """Monta o modelo com o público, os papéis e a marca de início."""
        return cls(
            id=template.id,
            key=template.key,
            name=template.name,
            definition=template.definition,
            audience=template.audience,
            role_ids=template.role_ids,
            is_home=template.is_home,
            updated_at=template.updated_at,
        )


class TemplateRoleOut(BaseModel):
    id: uuid.UUID
    name: dict[str, str]

    @classmethod
    def of(cls, role: Role) -> "TemplateRoleOut":
        """Monta o papel com o nome nos três idiomas."""
        return cls(id=role.id, name=role.name)


class TemplateRolesOut(BaseModel):
    """Os papéis da equipe Groone e os predefinidos dos clientes."""

    groone: list[TemplateRoleOut]
    clients: list[TemplateRoleOut]

    @classmethod
    def of(cls, roles: TemplateRoles) -> "TemplateRolesOut":
        """Monta as duas listas de papéis."""
        return cls(
            groone=[TemplateRoleOut.of(role) for role in roles.groone],
            clients=[TemplateRoleOut.of(role) for role in roles.clients],
        )
