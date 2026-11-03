"""DTOs do checklist de domínio no painel interno."""

import uuid
from datetime import date, datetime

from avant_core.identity.models import User
from avant_core.site_checklists.enums import CheckOutcome
from avant_core.site_checklists.models import (
    ChecklistMonth,
    ChecklistNoteView,
    ChecklistProgress,
    ChecklistRow,
    SiteChecklistDetail,
    SiteChecklistView,
)
from pydantic import BaseModel, Field

from avant_api.modules.internal.checklist_items.dto import ChecklistItemOut


class ChecklistPersonOut(BaseModel):
    id: uuid.UUID
    name: str

    @classmethod
    def of(cls, user: User | None) -> "ChecklistPersonOut | None":
        """Nome da pessoa; vazio se ela foi apagada."""
        return cls(id=user.id, name=user.name) if user else None


class ChecklistProgressOut(BaseModel):
    done: int
    total: int
    complete: bool

    @classmethod
    def of(cls, progress: ChecklistProgress) -> "ChecklistProgressOut":
        """Itens ok, total de itens ativos e se o checklist está feito."""
        return cls(done=progress.done, total=progress.total, complete=progress.complete)


class ChecklistOut(BaseModel):
    id: uuid.UUID
    month: date
    site: dict[str, str]
    client: dict[str, str] | None
    # Faturamento bruto do site no mês anterior, em dólar.
    revenue: str
    checked_at: datetime | None
    progress: ChecklistProgressOut

    @classmethod
    def of(cls, view: SiteChecklistView) -> "ChecklistOut":
        """Monta a linha com o site, o cliente, o faturamento e o progresso."""
        checklist = view.checklist
        client = view.client
        return cls(
            id=checklist.id,
            month=checklist.month,
            site={"id": str(view.site.id), "domain": view.site.domain},
            client={"id": str(client.id), "name": client.name} if client else None,
            revenue=f"{checklist.revenue_micros / 1_000_000:.2f}",
            checked_at=checklist.checked_at,
            progress=ChecklistProgressOut.of(view.progress),
        )


class ChecklistRowOut(BaseModel):
    item: ChecklistItemOut
    # Vazio enquanto não foi conferido e sempre no item manual.
    outcome: CheckOutcome | None
    # Código da prova (o painel traduz) e o detalhe: endereço, linha ou palavras.
    evidence: str | None
    detail: str | None
    checked_at: datetime | None
    marked_by: ChecklistPersonOut | None
    marked_at: datetime | None
    ok: bool

    @classmethod
    def of(cls, row: ChecklistRow) -> "ChecklistRowOut":
        """Monta o item com o automático e o "ok" marcado."""
        result = row.result
        return cls(
            item=ChecklistItemOut.of(row.item),
            outcome=result.outcome,
            evidence=result.evidence,
            detail=result.detail,
            checked_at=result.checked_at,
            marked_by=ChecklistPersonOut.of(row.marked_by),
            marked_at=result.marked_at,
            ok=result.is_ok,
        )


class ChecklistNoteOut(BaseModel):
    id: uuid.UUID
    message: str
    created_at: datetime
    author: ChecklistPersonOut | None
    edited_at: datetime | None
    editor: ChecklistPersonOut | None
    editable: bool

    @classmethod
    def of(cls, view: ChecklistNoteView) -> "ChecklistNoteOut":
        """Monta a observação com quem escreveu e quem editou."""
        return cls(
            id=view.note.id,
            message=view.note.message,
            created_at=view.note.created_at,
            author=ChecklistPersonOut.of(view.author),
            edited_at=view.note.edited_at,
            editor=ChecklistPersonOut.of(view.editor),
            editable=view.editable,
        )


class ChecklistDetailOut(ChecklistOut):
    rows: list[ChecklistRowOut]
    notes: list[ChecklistNoteOut]
    # Idioma do dono do cliente: as observações entram no relatório dele.
    client_locale: str | None
    # Só o checklist do mês atual muda.
    current: bool

    @classmethod
    def of_detail(cls, detail: SiteChecklistDetail) -> "ChecklistDetailOut":
        """Monta a página do checklist do site."""
        return cls(
            **ChecklistOut.of(detail.view).model_dump(),
            rows=[ChecklistRowOut.of(row) for row in detail.rows],
            notes=[ChecklistNoteOut.of(note) for note in detail.notes],
            client_locale=detail.client_locale,
            current=detail.current,
        )


class ChecklistMonthOut(BaseModel):
    month: date
    sites: int
    done: int
    checked_at: datetime | None

    @classmethod
    def of(cls, month: ChecklistMonth) -> "ChecklistMonthOut":
        """O resumo do mês."""
        return cls(
            month=month.month, sites=month.sites, done=month.done, checked_at=month.checked_at
        )


class ChecklistMarkIn(BaseModel):
    ok: bool


class ChecklistNoteIn(BaseModel):
    message: str = Field(min_length=1, max_length=5000)
