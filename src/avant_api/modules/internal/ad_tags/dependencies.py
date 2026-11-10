"""Monta o service das ad tags dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.ad_tags.service import ClientAdTagService


def client_ad_tag_service(services: Services = Depends(get_services)) -> ClientAdTagService:
    """O service com o banco, o relógio e o cache das tags."""
    return ClientAdTagService(services, services.clock, services.rewards)
