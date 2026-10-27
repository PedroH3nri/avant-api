"""Monta o service do perfil com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.profile.service import ProfileService


def profile_service(services: Services = Depends(get_services)) -> ProfileService:
    """O service do perfil com o banco, o relógio e o conversor de imagens."""
    return ProfileService(services, services.clock, services.images)
