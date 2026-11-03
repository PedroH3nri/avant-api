"""DTOs dos itens do checklist de domínio."""

import uuid
from datetime import datetime

from avant_core.site_checklists.enums import CheckKind
from avant_core.site_checklists.models import ChecklistItem, ChecklistItemInput
from pydantic import BaseModel, Field


class ChecklistItemOut(BaseModel):
    id: uuid.UUID
    name: str
    kind: CheckKind
    # Só no tipo link: as palavras procuradas nos links da página inicial.
    words: list[str]
    position: int
    active: bool
    created_at: datetime

    @classmethod
    def of(cls, item: ChecklistItem) -> "ChecklistItemOut":
        """Monta o item."""
        return cls(
            id=item.id,
            name=item.name,
            kind=item.kind,
            words=list(item.words),
            position=item.position,
            active=item.active,
            created_at=item.created_at,
        )


class ChecklistItemIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    kind: CheckKind
    words: list[str] = Field(default_factory=list, max_length=20)
    active: bool = True

    def to_input(self) -> ChecklistItemInput:
        """Os dados no formato do caso de uso."""
        return ChecklistItemInput(self.name, self.kind, tuple(self.words), self.active)


class ChecklistItemMoveIn(BaseModel):
    # -1 sobe uma posição; 1 desce.
    step: int = Field(ge=-1, le=1)
