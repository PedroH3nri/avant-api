"""Monta o service dos papéis com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.roles.service import RoleService


def role_service(services: Services = Depends(get_services)) -> RoleService:
    """O service dos papéis com o banco e o relógio da aplicação."""
    return RoleService(services, services.clock)
