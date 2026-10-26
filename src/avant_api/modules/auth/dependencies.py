"""Monta o service do login com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.auth.service import AuthService


def auth_service(services: Services = Depends(get_services)) -> AuthService:
    """O service do login com o banco, o relógio, as senhas e o limite de tentativas."""
    return AuthService(services, services.clock, services.hasher, services.limiter)
