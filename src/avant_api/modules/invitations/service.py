"""Service dos convites da Empresa ativa: listar, convidar, reenviar e cancelar."""

import uuid

from avant_core.access.models import Actor
from avant_core.company.services import (
    cancel_invitation,
    invite_member,
    page_pending_invitations,
    resend_invitation,
)
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.invitations.dto import InviteIn
from avant_api.shared.dto import InvitationOut, PageOut, page_out


class InvitationService:
    """Convites de equipe da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def page(self, actor: Actor, page: int) -> PageOut[InvitationOut]:
        """Uma página dos convites pendentes da Empresa ativa."""
        found = page_pending_invitations(self._uows.uow(actor.company_id), actor=actor, page=page)
        return page_out(found, InvitationOut.of)

    def invite(self, actor: Actor, body: InviteIn) -> InvitationOut:
        """Convida alguém para a equipe da Empresa ativa."""
        invitation = invite_member(
            self._uows.uow(actor.company_id),
            actor=actor,
            email=body.email,
            role_id=body.role_id,
            clock=self._clock,
            mailer=self._mailer,
        )
        return InvitationOut.of(invitation)

    def resend(self, actor: Actor, invitation_id: uuid.UUID) -> InvitationOut:
        """Token novo e mais 1 dia; o link anterior para de valer."""
        invitation = resend_invitation(
            self._uows.uow(actor.company_id),
            actor=actor,
            invitation_id=invitation_id,
            clock=self._clock,
            mailer=self._mailer,
        )
        return InvitationOut.of(invitation)

    def cancel(self, actor: Actor, invitation_id: uuid.UUID) -> None:
        """Cancela um convite pendente."""
        cancel_invitation(
            self._uows.uow(actor.company_id),
            actor=actor,
            invitation_id=invitation_id,
            clock=self._clock,
        )
