"""Monta o service da saúde com o banco da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.health.service import HealthService


def health_service(services: Services = Depends(get_services)) -> HealthService:
    """O service da saúde com a conexão do banco."""
    return HealthService(services.engine)
