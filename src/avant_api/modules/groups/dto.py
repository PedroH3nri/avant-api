"""DTOs de entrada e saída dos grupos de funcionários. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.groups.enums import GroupStatus
from avant_core.groups.models import GroupMember
from avant_core.groups.services import GroupView
from avant_core.groups.services.group_service import MAX_DESCRIPTION_LENGTH, MAX_NAME_LENGTH
from pydantic import BaseModel, Field


class GroupMemberOut(BaseModel):
    membership_id: uuid.UUID
    added_at: datetime

    @classmethod
    def of(cls, member: GroupMember) -> "GroupMemberOut":
        """Monta uma pessoa do grupo pelo vínculo dela com a Empresa."""
        return cls(membership_id=member.membership_id, added_at=member.added_at)


class GroupOut(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    status: GroupStatus
    members: list[GroupMemberOut]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, view: GroupView) -> "GroupOut":
        """Monta o grupo com as pessoas dele, na ordem em que entraram."""
        group = view.group
        return cls(
            id=group.id,
            name=group.name,
            description=group.description,
            status=group.status,
            members=[GroupMemberOut.of(member) for member in view.members],
            created_at=group.created_at,
            updated_at=group.updated_at,
        )


class GroupIn(BaseModel):
    name: str = Field(min_length=1, max_length=MAX_NAME_LENGTH)
    description: str | None = Field(default=None, max_length=MAX_DESCRIPTION_LENGTH)
    membership_ids: list[uuid.UUID] = Field(min_length=1, max_length=500)


class GroupPatchIn(BaseModel):
    name: str = Field(min_length=1, max_length=MAX_NAME_LENGTH)
    description: str | None = Field(default=None, max_length=MAX_DESCRIPTION_LENGTH)


class GroupMembersIn(BaseModel):
    membership_ids: list[uuid.UUID] = Field(min_length=1, max_length=500)
