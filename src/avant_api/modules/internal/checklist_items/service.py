"""Service dos itens do checklist de domínio.

Usa ``trusted_uow()`` (sem RLS) porque as tabelas do checklist são só do painel interno; o
core confere ``ensure_staff`` e a permissão em cada caso de uso.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.shared.clock import Clock
from avant_core.site_checklists.services import (
    create_checklist_item,
    list_checklist_items,
    move_checklist_item,
    update_checklist_item,
)

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.checklist_items.dto import ChecklistItemIn, ChecklistItemOut
from avant_api.shared.dto import ItemsOut


class ChecklistItemService:
    """A lista de itens que vale para todos os sites."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list(self, actor: Actor) -> ItemsOut[ChecklistItemOut]:
        """Todos os itens, na ordem."""
        items = list_checklist_items(self._uows.trusted_uow(), actor=actor)
        return ItemsOut(items=[ChecklistItemOut.of(item) for item in items])

    def create(self, actor: Actor, body: ChecklistItemIn) -> ChecklistItemOut:
        """Cria o item no fim da lista."""
        item = create_checklist_item(
            self._uows.trusted_uow(), actor=actor, data=body.to_input(), clock=self._clock
        )
        return ChecklistItemOut.of(item)

    def update(self, actor: Actor, item_id: uuid.UUID, body: ChecklistItemIn) -> ChecklistItemOut:
        """Muda o item."""
        item = update_checklist_item(
            self._uows.trusted_uow(),
            actor=actor,
            item_id=item_id,
            data=body.to_input(),
            clock=self._clock,
        )
        return ChecklistItemOut.of(item)

    def move(self, actor: Actor, item_id: uuid.UUID, step: int) -> ItemsOut[ChecklistItemOut]:
        """Sobe ou desce o item e devolve a lista na ordem nova."""
        items = move_checklist_item(
            self._uows.trusted_uow(), actor=actor, item_id=item_id, step=step
        )
        return ItemsOut(items=[ChecklistItemOut.of(item) for item in items])
