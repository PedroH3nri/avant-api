"""Service dos convites da Empresa ativa: listar, convidar, reenviar e cancelar."""

import uuid

from avant_core.company.service import Actor, invite_member, list_pending_invitations
from avant_core.company.team_service import cancel_invitation, resend_invitation
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.invitations.dto import InviteIn
from avant_api.shared.dto import InvitationOut


class InvitationService:
    """Convites de equipe da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def list_all(self, actor: Actor) -> list[InvitationOut]:
        """Os convites pendentes da Empresa ativa."""
        items = list_pending_invitations(self._uows.uow(actor.company_id), actor=actor)
        return [InvitationOut.of(invitation) for invitation in items]

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
