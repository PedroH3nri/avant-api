"""Monta o service dos itens do checklist com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.checklist_items.service import ChecklistItemService


def checklist_item_service(services: Services = Depends(get_services)) -> ChecklistItemService:
    """O service dos itens com o banco e o relógio da aplicação."""
    return ChecklistItemService(services, services.clock)
