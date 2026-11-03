"""Service do checklist de domínio no painel interno.

Usa ``trusted_uow()`` (sem RLS) porque as tabelas do checklist são só do painel interno; o
core confere ``ensure_staff`` e a permissão em cada caso de uso. "Conferir agora" enfileira a
tarefa do worker depois que o core aceitou o pedido.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.shared.clock import Clock
from avant_core.site_checklists.enums import ChecklistState
from avant_core.site_checklists.services import (
    add_checklist_note,
    checklist_month,
    checklist_months,
    delete_checklist_note,
    edit_checklist_note,
    get_checklist,
    mark_checklist_item,
    page_checklists,
    request_checklist_check,
)

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import CHECK_CHECKLIST, TaskQueue
from avant_api.modules.internal.checklists.dto import (
    ChecklistDetailOut,
    ChecklistMonthOut,
    ChecklistOut,
)
from avant_api.shared.dto import ItemsOut, PageOut, page_out


class SiteChecklistService:
    """Os checklists do mês, a página de cada site, as marcações e as observações."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, tasks: TaskQueue) -> None:
        self._uows = uows
        self._clock = clock
        self._tasks = tasks

    def months(self, actor: Actor) -> ItemsOut[date]:
        """Os meses com checklist, do mais novo para o mais antigo."""
        found = checklist_months(self._uows.trusted_uow(), actor=actor, clock=self._clock)
        return ItemsOut(items=found)

    def summary(self, actor: Actor, month: date) -> ChecklistMonthOut:
        """O resumo do mês."""
        found = checklist_month(self._uows.trusted_uow(), actor=actor, month=month)
        return ChecklistMonthOut.of(found)

    def page(
        self, actor: Actor, month: date, query: str | None, state: ChecklistState, page: int
    ) -> PageOut[ChecklistOut]:
        """Uma página do mês, do maior faturamento para o menor."""
        found = page_checklists(
            self._uows.trusted_uow(),
            actor=actor,
            month=month,
            query=query,
            state=state,
            page=page,
        )
        return page_out(found, ChecklistOut.of)

    def get(self, actor: Actor, checklist_id: uuid.UUID) -> ChecklistDetailOut:
        """O checklist do site com os itens e as observações."""
        detail = get_checklist(
            self._uows.trusted_uow(), actor=actor, checklist_id=checklist_id, clock=self._clock
        )
        return ChecklistDetailOut.of_detail(detail)

    def mark(
        self, actor: Actor, checklist_id: uuid.UUID, item_id: uuid.UUID, ok: bool
    ) -> ChecklistDetailOut:
        """Marca o item como ok ou tira a marcação."""
        detail = mark_checklist_item(
            self._uows.trusted_uow(),
            actor=actor,
            checklist_id=checklist_id,
            item_id=item_id,
            ok=ok,
            clock=self._clock,
        )
        return ChecklistDetailOut.of_detail(detail)

    def check(self, actor: Actor, checklist_id: uuid.UUID) -> None:
        """Pede ao worker uma conferência nova do site."""
        checklist = request_checklist_check(
            self._uows.trusted_uow(), actor=actor, checklist_id=checklist_id, clock=self._clock
        )
        self._tasks.send(CHECK_CHECKLIST, str(checklist.id))

    def add_note(self, actor: Actor, checklist_id: uuid.UUID, message: str) -> None:
        """Escreve uma observação."""
        add_checklist_note(
            self._uows.trusted_uow(),
            actor=actor,
            checklist_id=checklist_id,
            message=message,
            clock=self._clock,
        )

    def edit_note(
        self, actor: Actor, checklist_id: uuid.UUID, note_id: uuid.UUID, message: str
    ) -> None:
        """Troca o texto da observação."""
        edit_checklist_note(
            self._uows.trusted_uow(),
            actor=actor,
            checklist_id=checklist_id,
            note_id=note_id,
            message=message,
            clock=self._clock,
        )

    def delete_note(self, actor: Actor, checklist_id: uuid.UUID, note_id: uuid.UUID) -> None:
        """Apaga a observação."""
        delete_checklist_note(
            self._uows.trusted_uow(), actor=actor, checklist_id=checklist_id, note_id=note_id
        )
