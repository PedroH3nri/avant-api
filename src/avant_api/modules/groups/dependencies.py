"""Monta o service dos grupos com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.groups.service import GroupService


def group_service(services: Services = Depends(get_services)) -> GroupService:
    """O service dos grupos com o banco e o relógio da aplicação."""
    return GroupService(services, services.clock)
