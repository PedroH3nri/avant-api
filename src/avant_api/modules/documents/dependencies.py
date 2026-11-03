"""Monta o service dos documentos com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.documents.service import DocumentService


def document_service(services: Services = Depends(get_services)) -> DocumentService:
    """O service dos documentos com o banco e o relógio da aplicação."""
    return DocumentService(services, services.clock)
