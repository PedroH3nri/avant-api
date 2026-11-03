"""Monta o service das observações dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.client_notes.service import ClientNoteService


def client_note_service(services: Services = Depends(get_services)) -> ClientNoteService:
    """O service das observações com o banco e o relógio da aplicação."""
    return ClientNoteService(services, services.clock)
