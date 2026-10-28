"""Service dos grupos de funcionários da Empresa ativa."""

import uuid

from avant_core.access.models import Actor
from avant_core.groups.services import (
    add_group_members,
    create_group,
    delete_group,
    get_group,
    list_groups,
    remove_group_member,
    update_group,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.groups.dto import GroupIn, GroupMembersIn, GroupOut, GroupPatchIn


class GroupService:
    """Grupos da Empresa ativa e as pessoas de cada um."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(self, actor: Actor) -> list[GroupOut]:
        """Os grupos da Empresa ativa, pelo nome."""
        views = list_groups(self._uows.uow(actor.company_id), actor=actor)
        return [GroupOut.of(view) for view in views]

    def detail(self, actor: Actor, group_id: uuid.UUID) -> GroupOut:
        """Um grupo com as pessoas dele."""
        view = get_group(self._uows.uow(actor.company_id), actor=actor, group_id=group_id)
        return GroupOut.of(view)

    def create(self, actor: Actor, body: GroupIn) -> GroupOut:
        """Cria o grupo já com as pessoas escolhidas."""
        view = create_group(
            self._uows.uow(actor.company_id),
            actor=actor,
            name=body.name,
            description=body.description,
            membership_ids=body.membership_ids,
            clock=self._clock,
        )
        return GroupOut.of(view)

    def update(self, actor: Actor, group_id: uuid.UUID, body: GroupPatchIn) -> GroupOut:
        """Troca o nome e a descrição do grupo."""
        view = update_group(
            self._uows.uow(actor.company_id),
            actor=actor,
            group_id=group_id,
            name=body.name,
            description=body.description,
            clock=self._clock,
        )
        return GroupOut.of(view)

    def add_members(self, actor: Actor, group_id: uuid.UUID, body: GroupMembersIn) -> GroupOut:
        """Põe pessoas no grupo; o grupo inativo volta a ficar ativo."""
        view = add_group_members(
            self._uows.uow(actor.company_id),
            actor=actor,
            group_id=group_id,
            membership_ids=body.membership_ids,
            clock=self._clock,
        )
        return GroupOut.of(view)

    def remove_member(
        self, actor: Actor, group_id: uuid.UUID, membership_id: uuid.UUID
    ) -> GroupOut:
        """Tira uma pessoa do grupo; a última não sai."""
        view = remove_group_member(
            self._uows.uow(actor.company_id),
            actor=actor,
            group_id=group_id,
            membership_id=membership_id,
            clock=self._clock,
        )
        return GroupOut.of(view)

    def delete(self, actor: Actor, group_id: uuid.UUID) -> None:
        """Exclui o grupo; as pessoas voltam ao padrão da Empresa."""
        delete_group(
            self._uows.uow(actor.company_id), actor=actor, group_id=group_id, clock=self._clock
        )
