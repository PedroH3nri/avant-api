"""Monta o service e os redirecionamentos do Facebook com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.facebook.oauth import FacebookRedirects
from avant_api.modules.facebook.service import FacebookService


def facebook_service(services: Services = Depends(get_services)) -> FacebookService:
    """O service do Facebook com o banco, o relógio, a Graph API e a cifra dos tokens."""
    return FacebookService(services, services.clock, services.facebook, services.facebook_box)


def facebook_redirects(services: Services = Depends(get_services)) -> FacebookRedirects:
    """Os redirecionamentos do login do Facebook com as configurações da aplicação."""
    return FacebookRedirects(services.settings)
