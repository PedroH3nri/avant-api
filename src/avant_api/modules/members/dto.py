"""DTOs de entrada e saída do domínio members. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.access.enums import Effect
from avant_core.access.models import MemberPermission
from avant_core.company.enums import MembershipStatus
from avant_core.company.services import MemberDetail, MemberView
from pydantic import BaseModel, Field

from avant_api.shared.dto import MemberOut


class DirectPermissionOut(BaseModel):
    permission: str
    effect: Effect
    expires_at: datetime | None

    @classmethod
    def of(cls, permission: MemberPermission) -> "DirectPermissionOut":
        """Monta uma permissão direta do membro."""
        return cls(
            permission=permission.permission_key,
            effect=permission.effect,
            expires_at=permission.expires_at,
        )


class MemberDetailOut(MemberOut):
    permissions: list[DirectPermissionOut]

    @classmethod
    def of(cls, view: MemberView) -> "MemberDetailOut":
        """Monta o membro com as permissões diretas."""
        assert isinstance(view, MemberDetail)
        base = MemberOut.of(view).model_dump()
        return cls(
            **base,
            permissions=[DirectPermissionOut.of(permission) for permission in view.permissions],
        )


class MemberPatchIn(BaseModel):
    role_id: uuid.UUID | None = None
    status: MembershipStatus | None = None


class DirectPermissionIn(BaseModel):
    permission: str
    effect: Effect
    expires_at: datetime | None = None


class MemberPermissionsIn(BaseModel):
    permissions: list[DirectPermissionIn] = Field(max_length=64)
