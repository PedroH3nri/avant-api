"""Monta o service do resultado dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.results.service import ClientResultService


def client_result_service(services: Services = Depends(get_services)) -> ClientResultService:
    """O service do resultado dos clientes com o banco e o relógio da aplicação."""
    return ClientResultService(services, services.clock)
