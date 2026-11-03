"""Tarefas de suporte da equipe Groone: /api/v1/internal/tasks.

Cada pessoa vê as tarefas que criou e as que estão com ela; ``scope=all`` pede
``internal.tasks.all``. Tarefa que a pessoa não vê responde 404.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.support_tasks.enums import TaskPriority, TaskScope, TaskStatus
from avant_core.support_tasks.models import TaskFilter
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.tasks.dependencies import support_task_service
from avant_api.modules.internal.tasks.dto import (
    TaskCommentIn,
    TaskDetailOut,
    TaskIn,
    TaskOut,
    TaskPatchIn,
)
from avant_api.modules.internal.tasks.service import SupportTaskService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal/tasks", tags=["internal"])
PERMISSION = "internal.tasks.view"


@router.get("")
def tasks(
    scope: TaskScope = TaskScope.MINE,
    status_filter: list[TaskStatus] = Query(default=[], alias="status"),
    priority: TaskPriority | None = None,
    assignee: uuid.UUID | None = None,
    client: uuid.UUID | None = None,
    query: str | None = Query(default=None, alias="q", max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: SupportTaskService = Depends(support_task_service),
) -> PageOut[TaskOut]:
    """Uma página das tarefas, com filtros de situação, prioridade, responsável e cliente."""
    filters = TaskFilter(
        scope=scope,
        statuses=tuple(status_filter),
        priority=priority,
        assignee_id=assignee,
        client_id=client,
        query=query or None,
    )
    return service.page(actor, filters, page)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: TaskIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: SupportTaskService = Depends(support_task_service),
) -> TaskDetailOut:
    """Abre uma tarefa."""
    return service.create(actor, body)


@router.get("/{task_id}")
def task(
    task_id: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: SupportTaskService = Depends(support_task_service),
) -> TaskDetailOut:
    """A tarefa com a linha do tempo."""
    return service.get(actor, task_id)


@router.patch("/{task_id}")
def change(
    task_id: uuid.UUID,
    body: TaskPatchIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: SupportTaskService = Depends(support_task_service),
) -> TaskDetailOut:
    """Muda situação, prioridade, responsável ou dados; quem criou, o responsável ou o gestor."""
    return service.change(actor, task_id, body)


@router.post("/{task_id}/comments", status_code=status.HTTP_201_CREATED)
def comment(
    task_id: uuid.UUID,
    body: TaskCommentIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: SupportTaskService = Depends(support_task_service),
) -> TaskDetailOut:
    """Comenta na tarefa e devolve a linha do tempo atualizada."""
    return service.comment(actor, task_id, body.message)
