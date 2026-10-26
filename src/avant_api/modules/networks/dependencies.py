"""Monta o service das networks com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.networks.service import NetworkService


def network_service(services: Services = Depends(get_services)) -> NetworkService:
    """O service das networks com o banco, o relógio, a fila e a conta de serviço."""
    return NetworkService(
        services, services.clock, services.tasks, services.settings.gam_service_account_email
    )
