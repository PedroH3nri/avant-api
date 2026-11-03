"""Documentos dos clientes: /api/v1/internal/clients/{company_id}/documents."""

import uuid

from avant_core.access.models import Actor
from avant_core.documents.enums import DocumentKind
from fastapi import APIRouter, Depends, Response

from avant_api.app.security import require_staff
from avant_api.modules.internal.client_documents.dependencies import client_document_service
from avant_api.modules.internal.client_documents.dto import (
    ClientDocumentOut,
    ClientDocumentsOut,
    RejectDocumentIn,
)
from avant_api.modules.internal.client_documents.service import ClientDocumentService
from avant_api.shared.documents import document_response

router = APIRouter(prefix="/internal/clients/{company_id}/documents", tags=["internal"])
PERMISSION = "internal.clients.documents"


@router.get("")
def documents(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientDocumentService = Depends(client_document_service),
) -> ClientDocumentsOut:
    """Identidade e comprovante de residência do cliente, com a situação de cada um."""
    return service.overview(actor, company_id)


@router.get("/{kind}/file", response_class=Response)
def download(
    company_id: uuid.UUID,
    kind: DocumentKind,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientDocumentService = Depends(client_document_service),
) -> Response:
    """Baixa o arquivo enviado; o download fica no histórico do cliente."""
    return document_response(*service.file(actor, company_id, kind))


@router.post("/{kind}/approve")
def approve(
    company_id: uuid.UUID,
    kind: DocumentKind,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientDocumentService = Depends(client_document_service),
) -> ClientDocumentOut:
    """Aprova o documento em análise."""
    return service.approve(actor, company_id, kind)


@router.post("/{kind}/reject")
def reject(
    company_id: uuid.UUID,
    kind: DocumentKind,
    body: RejectDocumentIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: ClientDocumentService = Depends(client_document_service),
) -> ClientDocumentOut:
    """Recusa o documento com o motivo, que o cliente vê para enviar de novo."""
    return service.reject(actor, company_id, kind, body.reason)
