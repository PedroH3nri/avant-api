"""Monta o service dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.clients.service import ClientService


def client_service(services: Services = Depends(get_services)) -> ClientService:
    """O service dos clientes com o banco, o relógio e o e-mail da aplicação."""
    return ClientService(services, services.clock, services.mailer)
