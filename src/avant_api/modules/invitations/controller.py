"""Convites da Empresa ativa: /api/v1/invitations."""

import uuid

from avant_core.company.application import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require
from avant_api.modules.invitations.dependencies import invitation_service
from avant_api.modules.invitations.dto import InviteIn
from avant_api.modules.invitations.service import InvitationService
from avant_api.shared.dto import InvitationOut, ItemsOut

router = APIRouter(prefix="/invitations", tags=["team"])


@router.get("")
def list_invitations(
    actor: Actor = Depends(require("team.view")),
    service: InvitationService = Depends(invitation_service),
) -> ItemsOut[InvitationOut]:
    """Lista os convites pendentes da Empresa ativa."""
    return ItemsOut(items=service.list_all(actor))


@router.post("", status_code=status.HTTP_201_CREATED)
def create_invitation(
    body: InviteIn,
    actor: Actor = Depends(require("team.invite")),
    service: InvitationService = Depends(invitation_service),
) -> InvitationOut:
    """Convida alguém para a equipe da Empresa ativa."""
    return service.invite(actor, body)


@router.post("/{invitation_id}/resend")
def resend(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require("team.invite")),
    service: InvitationService = Depends(invitation_service),
) -> InvitationOut:
    """Token novo e mais 1 dia; o link anterior para de valer."""
    return service.resend(actor, invitation_id)


@router.delete("/{invitation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require("team.invite")),
    service: InvitationService = Depends(invitation_service),
) -> None:
    """Cancela um convite pendente."""
    service.cancel(actor, invitation_id)
