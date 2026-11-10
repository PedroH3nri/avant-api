"""Monta o service das ad tags com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.ad_tags.service import AdTagService


def ad_tag_service(services: Services = Depends(get_services)) -> AdTagService:
    """O service das ad tags com o banco, o relógio e o cache das tags."""
    return AdTagService(services, services.clock, services.rewards)
