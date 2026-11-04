"""Documentos da Empresa ativa: /api/v1/company/documents."""

from avant_core.access.models import Actor
from avant_core.documents.enums import DocumentKind
from fastapi import APIRouter, Depends, Query, Response

from avant_api.app.security import require
from avant_api.modules.documents.dependencies import document_service
from avant_api.modules.documents.dto import DocumentOut, DocumentsOut
from avant_api.modules.documents.service import DocumentService
from avant_api.shared.documents import document_response, document_upload

router = APIRouter(prefix="/company/documents", tags=["company"])


@router.get("")
def documents(
    actor: Actor = Depends(require("company.edit")),
    service: DocumentService = Depends(document_service),
) -> DocumentsOut:
    """Identidade e comprovante de residência enviados, com a situação de cada um."""
    return service.overview(actor)


@router.put("/{kind}")
def upload(
    kind: DocumentKind,
    name: str = Query(min_length=1, max_length=255),
    actor: Actor = Depends(require("company.edit")),
    content: bytes = Depends(document_upload),
    service: DocumentService = Depends(document_service),
) -> DocumentOut:
    """Envia o documento: o corpo é o arquivo JPG, PNG ou PDF de até 5 MB e ``name`` é o nome
    dele na máquina da pessoa."""
    return service.upload(actor, kind, name, content)


@router.get("/{kind}/file", response_class=Response)
def download(
    kind: DocumentKind,
    actor: Actor = Depends(require("company.edit")),
    service: DocumentService = Depends(document_service),
) -> Response:
    """Baixa o arquivo enviado; o download fica no histórico da Empresa."""
    return document_response(*service.file(actor, kind))
