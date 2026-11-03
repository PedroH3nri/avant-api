"""Observações dos clientes: /api/v1/internal/clients/{company_id}/notes.

Editar e apagar a observação de outra pessoa pede ``internal.clients.notes.manage``; o core
confere isso, porque o autor também pode.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.client_notes.dependencies import client_note_service
from avant_api.modules.internal.client_notes.dto import ClientNoteIn, ClientNoteOut
from avant_api.modules.internal.client_notes.service import ClientNoteService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal/clients/{company_id}/notes", tags=["internal"])
PERMISSION = "internal.clients.notes"


@router.get("")
def notes(
    company_id: uuid.UUID,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientNoteService = Depends(client_note_service),
) -> PageOut[ClientNoteOut]:
    """Uma página das observações do cliente, da mais nova para a mais antiga."""
    return service.page(actor, company_id, page)


@router.post("", status_code=status.HTTP_204_NO_CONTENT)
def add(
    company_id: uuid.UUID,
    body: ClientNoteIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientNoteService = Depends(client_note_service),
) -> None:
    """Escreve uma observação; o painel recarrega a lista depois."""
    service.add(actor, company_id, body.message)


@router.patch("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def edit(
    company_id: uuid.UUID,
    note_id: uuid.UUID,
    body: ClientNoteIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientNoteService = Depends(client_note_service),
) -> None:
    """Troca o texto de uma observação."""
    service.edit(actor, company_id, note_id, body.message)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    company_id: uuid.UUID,
    note_id: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientNoteService = Depends(client_note_service),
) -> None:
    """Apaga uma observação."""
    service.delete(actor, company_id, note_id)
