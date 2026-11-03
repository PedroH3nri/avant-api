"""Itens do checklist de domínio: /api/v1/internal/checklist-items.

Ver pede ``internal.checklists.view``; criar, editar e mudar a ordem pedem
``internal.checklists.manage`` (o core confere).
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.checklist_items.dependencies import checklist_item_service
from avant_api.modules.internal.checklist_items.dto import (
    ChecklistItemIn,
    ChecklistItemMoveIn,
    ChecklistItemOut,
)
from avant_api.modules.internal.checklist_items.service import ChecklistItemService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal/checklist-items", tags=["internal"])
VIEW = "internal.checklists.view"
MANAGE = "internal.checklists.manage"


@router.get("")
def items(
    actor: Actor = Depends(require_staff(VIEW)),
    service: ChecklistItemService = Depends(checklist_item_service),
) -> ItemsOut[ChecklistItemOut]:
    """Todos os itens, ativos e desligados, na ordem."""
    return service.list(actor)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: ChecklistItemIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ChecklistItemService = Depends(checklist_item_service),
) -> ChecklistItemOut:
    """Cria um item no fim da lista; ativo, ele entra no checklist do mês atual."""
    return service.create(actor, body)


@router.put("/{item_id}")
def update(
    item_id: uuid.UUID,
    body: ChecklistItemIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ChecklistItemService = Depends(checklist_item_service),
) -> ChecklistItemOut:
    """Muda nome, jeito de conferir, palavras e se o item está ativo."""
    return service.update(actor, item_id, body)


@router.post("/{item_id}/move")
def move(
    item_id: uuid.UUID,
    body: ChecklistItemMoveIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ChecklistItemService = Depends(checklist_item_service),
) -> ItemsOut[ChecklistItemOut]:
    """Sobe ou desce o item uma posição."""
    return service.move(actor, item_id, body.step)
