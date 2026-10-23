"""Convites da Empresa ativa: /api/v1/invitations."""

from avant_core.company.application import (
    Actor,
    invite_member,
    list_pending_invitations,
)
from avant_core.company.domain import Invitation
from fastapi import APIRouter, Depends, status

from avant_api.deps import get_services, require
from avant_api.schemas import InvitationOut, InviteIn, ItemsOut
from avant_api.services import Services

router = APIRouter(prefix="/invitations", tags=["team"])


def _out(i: Invitation) -> InvitationOut:
    return InvitationOut(
        id=i.id,
        email=i.email,
        role_id=i.role_id,
        status=i.status,
        expires_at=i.expires_at,
        invited_by=i.invited_by,
    )


@router.get("")
def list_invitations(
    actor: Actor = Depends(require("team.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[InvitationOut]:
    items = list_pending_invitations(services.uow(actor.company_id), actor=actor)
    return ItemsOut(items=[_out(i) for i in items])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_invitation(
    body: InviteIn,
    actor: Actor = Depends(require("team.invite")),
    services: Services = Depends(get_services),
) -> InvitationOut:
    invitation = invite_member(
        services.uow(actor.company_id),
        actor=actor,
        email=body.email,
        role_id=body.role_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return _out(invitation)
