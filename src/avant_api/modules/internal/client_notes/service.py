"""Service das observações dos clientes no painel interno.

Usa ``trusted_uow()`` (sem RLS) porque a Groone enxerga todas as Empresas; o core confere
``ensure_staff`` em cada caso de uso.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.client_notes.services import (
    add_client_note,
    delete_client_note,
    edit_client_note,
    page_client_notes,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.client_notes.dto import ClientNoteOut
from avant_api.shared.dto import PageOut, page_out


class ClientNoteService:
    """Observações que a equipe Groone escreve sobre um cliente."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def page(self, actor: Actor, company_id: uuid.UUID, page: int) -> PageOut[ClientNoteOut]:
        """Uma página das observações, da mais nova para a mais antiga."""
        found = page_client_notes(
            self._uows.trusted_uow(), actor=actor, company_id=company_id, page=page
        )
        return page_out(found, ClientNoteOut.of)

    def add(self, actor: Actor, company_id: uuid.UUID, message: str) -> None:
        """Escreve uma observação sobre o cliente."""
        add_client_note(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            message=message,
            clock=self._clock,
        )

    def edit(self, actor: Actor, company_id: uuid.UUID, note_id: uuid.UUID, message: str) -> None:
        """Troca o texto da observação; fica guardado quem editou e quando."""
        edit_client_note(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            note_id=note_id,
            message=message,
            clock=self._clock,
        )

    def delete(self, actor: Actor, company_id: uuid.UUID, note_id: uuid.UUID) -> None:
        """Apaga a observação."""
        delete_client_note(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            note_id=note_id,
            clock=self._clock,
        )
