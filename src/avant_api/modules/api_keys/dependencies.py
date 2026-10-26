"""Monta o service das chaves de API com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.api_keys.service import ApiKeyService


def api_key_service(services: Services = Depends(get_services)) -> ApiKeyService:
    """O service das chaves com o banco e o relógio da aplicação."""
    return ApiKeyService(services, services.clock)
