"""Service da equipe Groone no painel interno."""

from avant_core.access.models import Actor
from avant_core.internal.services import invite_staff, page_staff, staff_options
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.staff.dto import StaffInviteIn
from avant_api.shared.dto import InvitationOut, MemberOut, PageOut, page_out


class StaffService:
    """Lista e convida a equipe Groone."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def list_all(self, actor: Actor, page: int) -> PageOut[MemberOut]:
        """Uma página da equipe Groone, a mais recente primeiro."""
        found = page_staff(self._uows.trusted_uow(), actor=actor, page=page)
        return page_out(found, MemberOut.of)

    def options(self, actor: Actor) -> list[MemberOut]:
        """A equipe Groone inteira (sem os removidos), para os seletores."""
        return [MemberOut.of(view) for view in staff_options(self._uows.trusted_uow(), actor=actor)]

    def invite(self, actor: Actor, body: StaffInviteIn) -> InvitationOut:
        """Convida alguém para a equipe Groone com um papel interno."""
        invitation = invite_staff(
            self._uows.trusted_uow(),
            actor=actor,
            email=body.email,
            role_id=body.role_id,
            clock=self._clock,
            mailer=self._mailer,
        )
        return InvitationOut.of(invitation)
