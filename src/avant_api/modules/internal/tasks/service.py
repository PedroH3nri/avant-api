"""Service das tarefas de suporte da equipe Groone.

Usa ``trusted_uow()`` (sem RLS) porque as tabelas são só do painel interno; o core confere
``ensure_staff`` e quem pode ver cada tarefa.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock
from avant_core.support_tasks.models import TaskFilter
from avant_core.support_tasks.services import (
    change_task,
    comment_task,
    create_task,
    get_task,
    page_tasks,
)

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.tasks.dto import TaskDetailOut, TaskIn, TaskOut, TaskPatchIn
from avant_api.shared.dto import PageOut, page_out


class SupportTaskService:
    """Tarefas que a equipe Groone abre, distribui e comenta."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def page(self, actor: Actor, filters: TaskFilter, page: int) -> PageOut[TaskOut]:
        """Uma página das tarefas, da mudada por último para a mais antiga."""
        found = page_tasks(self._uows.trusted_uow(), actor=actor, filters=filters, page=page)
        return page_out(found, TaskOut.of)

    def get(self, actor: Actor, task_id: uuid.UUID) -> TaskDetailOut:
        """A tarefa com a linha do tempo."""
        detail = get_task(self._uows.trusted_uow(), actor=actor, task_id=task_id)
        return TaskDetailOut.of_detail(detail)

    def create(self, actor: Actor, body: TaskIn) -> TaskDetailOut:
        """Abre a tarefa; o responsável recebe um e-mail."""
        detail = create_task(
            self._uows.trusted_uow(),
            actor=actor,
            data=body.to_input(body.assignee_id),
            clock=self._clock,
            mailer=self._mailer,
        )
        return TaskDetailOut.of_detail(detail)

    def change(self, actor: Actor, task_id: uuid.UUID, body: TaskPatchIn) -> TaskDetailOut:
        """Muda situação, prioridade, responsável ou os dados da tarefa."""
        detail = change_task(
            self._uows.trusted_uow(),
            actor=actor,
            task_id=task_id,
            change=body.to_change(),
            clock=self._clock,
            mailer=self._mailer,
        )
        return TaskDetailOut.of_detail(detail)

    def comment(self, actor: Actor, task_id: uuid.UUID, message: str) -> TaskDetailOut:
        """Comenta; quem criou e o responsável recebem e-mail, menos quem escreveu."""
        detail = comment_task(
            self._uows.trusted_uow(),
            actor=actor,
            task_id=task_id,
            message=message,
            clock=self._clock,
            mailer=self._mailer,
        )
        return TaskDetailOut.of_detail(detail)
