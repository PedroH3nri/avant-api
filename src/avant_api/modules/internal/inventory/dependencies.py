"""Monta o service das networks e dos sites dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.inventory.service import ClientInventoryService


def client_inventory_service(services: Services = Depends(get_services)) -> ClientInventoryService:
    """O service com o banco e o relógio da aplicação."""
    return ClientInventoryService(services, services.clock)
