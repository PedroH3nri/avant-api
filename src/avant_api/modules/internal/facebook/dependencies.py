"""Monta o service do Facebook dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.facebook.service import ClientFacebookService


def client_facebook_service(services: Services = Depends(get_services)) -> ClientFacebookService:
    """O service com o banco e o relógio."""
    return ClientFacebookService(services, services.clock)
