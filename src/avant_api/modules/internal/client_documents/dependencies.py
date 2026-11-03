"""Monta o service dos documentos dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.client_documents.service import ClientDocumentService


def client_document_service(services: Services = Depends(get_services)) -> ClientDocumentService:
    """O service dos documentos com o banco, o relógio e o e-mail da aplicação."""
    return ClientDocumentService(services, services.clock, services.mailer)
