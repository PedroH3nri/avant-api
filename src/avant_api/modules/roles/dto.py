"""DTOs de entrada e saída do domínio roles. Datas sempre em ISO 8601 UTC."""

import uuid

from avant_core.access.enums import SiteScope
from avant_core.access.models import PermissionDef, Role
from avant_core.company.services import RoleView
from pydantic import BaseModel, Field


class PermissionOut(BaseModel):
    key: str
    group: str
    name: dict[str, str]

    @classmethod
    def of(cls, definition: PermissionDef) -> "PermissionOut":
        """Monta uma permissão do catálogo."""
        return cls(key=definition.key, group=definition.group, name=definition.label)


class RoleOut(BaseModel):
    id: uuid.UUID
    key: str
    name: dict[str, str]
    permissions: list[str]
    site_scope: SiteScope
    is_system: bool
    member_count: int

    @classmethod
    def of(cls, view: RoleView) -> "RoleOut":
        """Monta o papel com quantos membros o usam."""
        role: Role = view.role
        return cls(
            id=role.id,
            key=role.key,
            name=role.name,
            permissions=sorted(role.permissions),
            site_scope=role.site_scope,
            is_system=role.company_id is None,
            member_count=view.member_count,
        )


class RoleIn(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    permissions: list[str] = Field(default_factory=list, max_length=32)
    site_scope: SiteScope = SiteScope.ASSIGNED


class RolePatchIn(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=60)
    permissions: list[str] | None = Field(default=None, max_length=32)
    site_scope: SiteScope | None = None
