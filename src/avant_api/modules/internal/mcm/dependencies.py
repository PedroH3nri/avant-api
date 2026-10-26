"""Monta o service do MCM com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.mcm.service import McmService


def mcm_service(services: Services = Depends(get_services)) -> McmService:
    """O service do MCM com o banco, o relógio e a fila do worker."""
    return McmService(services, services.clock, services.tasks)
