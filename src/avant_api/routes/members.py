"""Membros da Empresa ativa: /api/v1/members."""

import uuid

from avant_core.company.application import Actor
from avant_core.company.domain import MembershipStatus
from avant_core.company.team import (
    DirectPermission,
    get_member,
    leave_company,
    list_members,
    remove_member,
    set_member_permissions,
    update_member,
)
from fastapi import APIRouter, Depends, Query, status

from avant_api.deps import get_services, get_session_actor, require
from avant_api.schemas import (
    ItemsOut,
    MemberDetailOut,
    MemberOut,
    MemberPatchIn,
    MemberPermissionsIn,
)
from avant_api.services import Services

router = APIRouter(prefix="/members", tags=["team"])


@router.get("")
def index(
    member_status: MembershipStatus | None = Query(default=None, alias="status"),
    role: uuid.UUID | None = None,
    query: str | None = Query(alias="q", default=None, max_length=120),
    actor: Actor = Depends(require("team.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[MemberOut]:
    """A equipe cabe no limite de vagas, então a lista vem inteira, sem cursor."""
    items = list_members(
        services.uow(actor.company_id), actor=actor, status=member_status, role_id=role, query=query
    )
    return ItemsOut(items=[MemberOut.of(member) for member in items])


@router.post("/me/leave", status_code=status.HTTP_204_NO_CONTENT)
def leave(
    actor: Actor = Depends(get_session_actor), services: Services = Depends(get_services)
) -> None:
    """Tira quem está agindo da Empresa ativa."""
    leave_company(services.uow(actor.company_id), actor=actor, clock=services.clock)


@router.get("/{membership_id}")
def show(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.view")),
    services: Services = Depends(get_services),
) -> MemberDetailOut:
    """Mostra um membro com papel e permissões diretas."""
    detail = get_member(services.uow(actor.company_id), actor=actor, membership_id=membership_id)
    return MemberDetailOut.of(detail)


@router.patch("/{membership_id}")
def edit(
    membership_id: uuid.UUID,
    body: MemberPatchIn,
    actor: Actor = Depends(require("team.manage")),
    services: Services = Depends(get_services),
) -> MemberDetailOut:
    """Muda o papel ou o status de um membro."""
    detail = update_member(
        services.uow(actor.company_id),
        actor=actor,
        membership_id=membership_id,
        clock=services.clock,
        role_id=body.role_id,
        status=body.status,
    )
    return MemberDetailOut.of(detail)


@router.delete("/{membership_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Remove um membro da Empresa."""
    remove_member(
        services.uow(actor.company_id),
        actor=actor,
        membership_id=membership_id,
        clock=services.clock,
    )


@router.put("/{membership_id}/permissions")
def set_permissions(
    membership_id: uuid.UUID,
    body: MemberPermissionsIn,
    actor: Actor = Depends(require("permissions.grant")),
    services: Services = Depends(get_services),
) -> MemberDetailOut:
    """Troca a lista inteira de permissões diretas do membro."""
    detail = set_member_permissions(
        services.uow(actor.company_id),
        actor=actor,
        membership_id=membership_id,
        permissions=[
            DirectPermission(permission.permission, permission.effect, permission.expires_at)
            for permission in body.permissions
        ],
        clock=services.clock,
    )
    return MemberDetailOut.of(detail)
