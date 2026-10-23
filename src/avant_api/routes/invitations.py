"""Convites da Empresa ativa: /api/v1/invitations."""

import uuid

from avant_core.company.application import (
    Actor,
    invite_member,
    list_pending_invitations,
)
from avant_core.company.domain import Invitation
from avant_core.company.team import cancel_invitation, resend_invitation
from fastapi import APIRouter, Depends, status

from avant_api.deps import get_services, require
from avant_api.schemas import InvitationOut, InviteIn, ItemsOut
from avant_api.services import Services

router = APIRouter(prefix="/invitations", tags=["team"])


def invitation_out(i: Invitation) -> InvitationOut:
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
    return ItemsOut(items=[invitation_out(i) for i in items])


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
    return invitation_out(invitation)


@router.post("/{invitation_id}/resend")
def resend(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require("team.invite")),
    services: Services = Depends(get_services),
) -> InvitationOut:
    """Token novo e mais 1 dia; o link anterior para de valer."""
    invitation = resend_invitation(
        services.uow(actor.company_id),
        actor=actor,
        invitation_id=invitation_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return invitation_out(invitation)


@router.delete("/{invitation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require("team.invite")),
    services: Services = Depends(get_services),
) -> None:
    cancel_invitation(
        services.uow(actor.company_id),
        actor=actor,
        invitation_id=invitation_id,
        clock=services.clock,
    )
