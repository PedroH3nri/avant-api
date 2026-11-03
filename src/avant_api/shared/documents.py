"""Documentos do cliente: formato de saída, download e leitura do envio, usados pelo
painel do cliente e pelo painel interno."""

from datetime import datetime
from urllib.parse import quote

from avant_core.documents.enums import DocumentKind, DocumentStatus
from avant_core.documents.errors import DocumentTooLarge
from avant_core.documents.models import CompanyDocument, DocumentsOverview
from avant_core.documents.services import MAX_BYTES
from fastapi import Request, Response
from pydantic import BaseModel

# Documento pessoal: o navegador não guarda cópia.
DOCUMENT_CACHE = "private, no-store"


class DocumentOut(BaseModel):
    kind: DocumentKind
    status: DocumentStatus
    file_name: str
    content_type: str
    size_bytes: int
    uploaded_at: datetime
    reviewed_at: datetime | None
    rejection_reason: str | None

    @classmethod
    def of(cls, document: CompanyDocument) -> "DocumentOut":
        """Monta o documento sem o arquivo, que sai pela rota de download."""
        return cls(
            kind=document.kind,
            status=document.status,
            file_name=document.file_name,
            content_type=document.content_type,
            size_bytes=document.size_bytes,
            uploaded_at=document.uploaded_at,
            reviewed_at=document.reviewed_at,
            rejection_reason=document.rejection_reason,
        )


class DocumentsOut(BaseModel):
    required: bool
    documents: list[DocumentOut]

    @classmethod
    def of(cls, overview: DocumentsOverview) -> "DocumentsOut":
        """Monta a lista e se a Empresa precisa enviar documentos (Manage Inventory)."""
        return cls(
            required=overview.required,
            documents=[DocumentOut.of(document) for document in overview.documents],
        )


def document_response(document: CompanyDocument, content: bytes) -> Response:
    """Devolve o arquivo como download, com o nome original e sem cache."""
    disposition = f"attachment; filename*=UTF-8''{quote(document.file_name)}"
    headers = {"Content-Disposition": disposition, "Cache-Control": DOCUMENT_CACHE}
    return Response(content, media_type=document.content_type, headers=headers)


async def document_upload(request: Request) -> bytes:
    """Corpo do PUT do documento (o arquivo cru); para de ler ao passar de 5 MB."""
    message = f"o arquivo passa de {MAX_BYTES // (1024 * 1024)} MB"
    declared = request.headers.get("Content-Length", "")
    if declared.isdigit() and int(declared) > MAX_BYTES:
        raise DocumentTooLarge(message)
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > MAX_BYTES:
            raise DocumentTooLarge(message)
    return bytes(body)
