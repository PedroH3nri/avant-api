"""Monta o service das visões salvas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.views.service import SavedViewService


def saved_view_service(services: Services = Depends(get_services)) -> SavedViewService:
    """O service das visões salvas com o banco e o relógio da aplicação."""
    return SavedViewService(services, services.clock)
