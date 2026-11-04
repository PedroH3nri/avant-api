"""Monta o service das ferramentas do GAM com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.gam_tools.service import GamToolService


def gam_tool_service(services: Services = Depends(get_services)) -> GamToolService:
    """O service com o banco, o relógio, a fila do worker e a network da Groone."""
    return GamToolService(
        services, services.clock, services.tasks, services.settings.gam_groone_network_code
    )
