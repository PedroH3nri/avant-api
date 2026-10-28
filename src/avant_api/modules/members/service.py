"""Service dos membros da Empresa ativa: lista, detalhe, papel, saída e permissões diretas."""

import uuid

from avant_core.access.models import Actor
from avant_core.company.enums import MembershipStatus
from avant_core.company.services import (
    DirectPermission,
    get_member,
    leave_company,
    list_members,
    remove_member,
    set_member_permissions,
    update_member,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.members.dto import MemberDetailOut, MemberPatchIn, MemberPermissionsIn
from avant_api.shared.dto import MemberOut


class MemberService:
    """Membros da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(
        self,
        actor: Actor,
        *,
        status: MembershipStatus | None,
        role_id: uuid.UUID | None,
        query: str | None,
    ) -> list[MemberOut]:
        """A equipe inteira, com filtros de situação, papel e busca."""
        items = list_members(
            self._uows.uow(actor.company_id),
            actor=actor,
            status=status,
            role_id=role_id,
            query=query,
        )
        return [MemberOut.of(member) for member in items]

    def leave(self, actor: Actor) -> None:
        """Tira quem está agindo da Empresa ativa."""
        leave_company(self._uows.uow(actor.company_id), actor=actor, clock=self._clock)

    def show(self, actor: Actor, membership_id: uuid.UUID) -> MemberDetailOut:
        """Um membro com papel e permissões diretas."""
        detail = get_member(
            self._uows.uow(actor.company_id), actor=actor, membership_id=membership_id
        )
        return MemberDetailOut.of(detail)

    def update(
        self, actor: Actor, membership_id: uuid.UUID, body: MemberPatchIn
    ) -> MemberDetailOut:
        """Muda o papel ou a situação de um membro."""
        detail = update_member(
            self._uows.uow(actor.company_id),
            actor=actor,
            membership_id=membership_id,
            clock=self._clock,
            role_id=body.role_id,
            status=body.status,
        )
        return MemberDetailOut.of(detail)

    def remove(self, actor: Actor, membership_id: uuid.UUID) -> None:
        """Remove um membro da Empresa."""
        remove_member(
            self._uows.uow(actor.company_id),
            actor=actor,
            membership_id=membership_id,
            clock=self._clock,
        )

    def set_permissions(
        self, actor: Actor, membership_id: uuid.UUID, body: MemberPermissionsIn
    ) -> MemberDetailOut:
        """Troca a lista inteira de permissões diretas do membro."""
        detail = set_member_permissions(
            self._uows.uow(actor.company_id),
            actor=actor,
            membership_id=membership_id,
            permissions=[
                DirectPermission(permission.permission, permission.effect, permission.expires_at)
                for permission in body.permissions
            ],
            clock=self._clock,
        )
        return MemberDetailOut.of(detail)
