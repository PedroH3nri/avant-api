"""Monta o service dos avisos com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.events.service import EventService


def event_service(services: Services = Depends(get_services)) -> EventService:
    """O service dos avisos com o canal de eventos da aplicação."""
    return EventService(services.events)
