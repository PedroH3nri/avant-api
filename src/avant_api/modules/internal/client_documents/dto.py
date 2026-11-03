"""DTOs dos documentos dos clientes no painel interno."""

import uuid

from avant_core.documents.models import CompanyDocument, DocumentsOverview
from pydantic import BaseModel, Field

from avant_api.shared.documents import DocumentOut


class ClientDocumentOut(DocumentOut):
    uploaded_by: uuid.UUID | None
    reviewed_by: uuid.UUID | None

    @classmethod
    def of(cls, document: CompanyDocument) -> "ClientDocumentOut":
        """Monta o documento com quem enviou e quem decidiu."""
        return cls(
            **DocumentOut.of(document).model_dump(),
            uploaded_by=document.uploaded_by,
            reviewed_by=document.reviewed_by,
        )


class ClientDocumentsOut(BaseModel):
    required: bool
    documents: list[ClientDocumentOut]

    @classmethod
    def of(cls, overview: DocumentsOverview) -> "ClientDocumentsOut":
        """Monta a lista e se o cliente precisa enviar documentos (Manage Inventory)."""
        return cls(
            required=overview.required,
            documents=[ClientDocumentOut.of(document) for document in overview.documents],
        )


class RejectDocumentIn(BaseModel):
    reason: str = Field(min_length=1, max_length=1000)
