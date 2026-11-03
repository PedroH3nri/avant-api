"""DTOs das observações dos clientes no painel interno."""

import uuid
from datetime import datetime

from avant_core.client_notes.models import ClientNoteView
from avant_core.identity.models import User
from pydantic import BaseModel, Field


class NotePersonOut(BaseModel):
    id: uuid.UUID
    name: str

    @classmethod
    def of(cls, user: User | None) -> "NotePersonOut | None":
        """Nome de quem escreveu ou editou; vazio se a pessoa foi apagada."""
        return cls(id=user.id, name=user.name) if user else None


class ClientNoteOut(BaseModel):
    id: uuid.UUID
    message: str
    created_at: datetime
    author: NotePersonOut | None
    edited_at: datetime | None
    editor: NotePersonOut | None
    editable: bool

    @classmethod
    def of(cls, view: ClientNoteView) -> "ClientNoteOut":
        """Monta a observação com autor, quem editou por último e se quem pediu pode mudar."""
        return cls(
            id=view.note.id,
            message=view.note.message,
            created_at=view.note.created_at,
            author=NotePersonOut.of(view.author),
            edited_at=view.note.edited_at,
            editor=NotePersonOut.of(view.editor),
            editable=view.editable,
        )


class ClientNoteIn(BaseModel):
    message: str = Field(min_length=1, max_length=5000)
