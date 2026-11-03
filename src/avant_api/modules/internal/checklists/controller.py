"""Checklist de domínio: /api/v1/internal/checklists.

Ver pede ``internal.checklists.view``; marcar, conferir agora e escrever observações pedem
``internal.checklists.check``. Só o checklist do mês atual muda (``checklist_not_checkable``).
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.site_checklists.enums import ChecklistState
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.checklists.dependencies import site_checklist_service
from avant_api.modules.internal.checklists.dto import (
    ChecklistDetailOut,
    ChecklistMarkIn,
    ChecklistMonthOut,
    ChecklistNoteIn,
    ChecklistOut,
)
from avant_api.modules.internal.checklists.service import SiteChecklistService
from avant_api.shared.dto import ItemsOut, PageOut

router = APIRouter(prefix="/internal/checklists", tags=["internal"])
VIEW = "internal.checklists.view"
CHECK = "internal.checklists.check"


@router.get("/months")
def months(
    actor: Actor = Depends(require_staff(VIEW)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> ItemsOut[date]:
    """Os meses com checklist, do mais novo para o mais antigo; o atual sempre aparece."""
    return service.months(actor)


@router.get("/summary")
def summary(
    month: date,
    actor: Actor = Depends(require_staff(VIEW)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> ChecklistMonthOut:
    """Quantos sites o mês tem, quantos estão feitos e a última conferência."""
    return service.summary(actor, month)


@router.get("")
def checklists(
    month: date,
    query: str | None = Query(alias="q", default=None, max_length=200),
    state: ChecklistState = ChecklistState.ALL,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(VIEW)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> PageOut[ChecklistOut]:
    """Uma página do mês, do maior faturamento para o menor, com busca e filtro de feito."""
    return service.page(actor, month, query or None, state, page)


@router.get("/{checklist_id}")
def checklist(
    checklist_id: uuid.UUID,
    actor: Actor = Depends(require_staff(VIEW)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> ChecklistDetailOut:
    """O checklist do site com os itens ativos e as observações."""
    return service.get(actor, checklist_id)


@router.put("/{checklist_id}/items/{item_id}")
def mark(
    checklist_id: uuid.UUID,
    item_id: uuid.UUID,
    body: ChecklistMarkIn,
    actor: Actor = Depends(require_staff(CHECK)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> ChecklistDetailOut:
    """Marca o item como ok (vence o automático) ou tira a marcação."""
    return service.mark(actor, checklist_id, item_id, body.ok)


@router.post("/{checklist_id}/check", status_code=status.HTTP_202_ACCEPTED)
def check(
    checklist_id: uuid.UUID,
    actor: Actor = Depends(require_staff(CHECK)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> None:
    """Pede ao worker uma conferência nova; o painel recarrega a página depois."""
    service.check(actor, checklist_id)


@router.post("/{checklist_id}/notes", status_code=status.HTTP_204_NO_CONTENT)
def add_note(
    checklist_id: uuid.UUID,
    body: ChecklistNoteIn,
    actor: Actor = Depends(require_staff(CHECK)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> None:
    """Escreve uma observação, no idioma do cliente."""
    service.add_note(actor, checklist_id, body.message)


@router.patch("/{checklist_id}/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def edit_note(
    checklist_id: uuid.UUID,
    note_id: uuid.UUID,
    body: ChecklistNoteIn,
    actor: Actor = Depends(require_staff(CHECK)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> None:
    """Troca o texto; quem escreveu ou quem tem ``internal.checklists.manage``."""
    service.edit_note(actor, checklist_id, note_id, body.message)


@router.delete("/{checklist_id}/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    checklist_id: uuid.UUID,
    note_id: uuid.UUID,
    actor: Actor = Depends(require_staff(CHECK)),
    service: SiteChecklistService = Depends(site_checklist_service),
) -> None:
    """Apaga a observação; quem escreveu ou quem tem ``internal.checklists.manage``."""
    service.delete_note(actor, checklist_id, note_id)
