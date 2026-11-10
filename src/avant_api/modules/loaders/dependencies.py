"""Monta o service dos loaders com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.loaders.service import LoaderService


def loader_service(services: Services = Depends(get_services)) -> LoaderService:
    """O service dos loaders com o banco, o relógio e o cache das tags."""
    return LoaderService(services, services.clock, services.rewards)
