"""Membros da Empresa ativa: /api/v1/members."""

import uuid

from avant_core.company.application import Actor
from avant_core.company.domain import MembershipStatus
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import get_session_actor, require
from avant_api.modules.members.dependencies import member_service
from avant_api.modules.members.dto import MemberDetailOut, MemberPatchIn, MemberPermissionsIn
from avant_api.modules.members.service import MemberService
from avant_api.shared.dto import ItemsOut, MemberOut

router = APIRouter(prefix="/members", tags=["team"])


@router.get("")
def index(
    member_status: MembershipStatus | None = Query(default=None, alias="status"),
    role: uuid.UUID | None = None,
    query: str | None = Query(alias="q", default=None, max_length=120),
    actor: Actor = Depends(require("team.view")),
    service: MemberService = Depends(member_service),
) -> ItemsOut[MemberOut]:
    """A equipe cabe no limite de vagas, então a lista vem inteira, sem cursor."""
    return ItemsOut(items=service.list_all(actor, status=member_status, role_id=role, query=query))


@router.post("/me/leave", status_code=status.HTTP_204_NO_CONTENT)
def leave(
    actor: Actor = Depends(get_session_actor), service: MemberService = Depends(member_service)
) -> None:
    """Tira quem está agindo da Empresa ativa."""
    service.leave(actor)


@router.get("/{membership_id}")
def show(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.view")),
    service: MemberService = Depends(member_service),
) -> MemberDetailOut:
    """Mostra um membro com papel e permissões diretas."""
    return service.show(actor, membership_id)


@router.patch("/{membership_id}")
def edit(
    membership_id: uuid.UUID,
    body: MemberPatchIn,
    actor: Actor = Depends(require("team.manage")),
    service: MemberService = Depends(member_service),
) -> MemberDetailOut:
    """Muda o papel ou o status de um membro."""
    return service.update(actor, membership_id, body)


@router.delete("/{membership_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.manage")),
    service: MemberService = Depends(member_service),
) -> None:
    """Remove um membro da Empresa."""
    service.remove(actor, membership_id)


@router.put("/{membership_id}/permissions")
def set_permissions(
    membership_id: uuid.UUID,
    body: MemberPermissionsIn,
    actor: Actor = Depends(require("permissions.grant")),
    service: MemberService = Depends(member_service),
) -> MemberDetailOut:
    """Troca a lista inteira de permissões diretas do membro."""
    return service.set_permissions(actor, membership_id, body)
