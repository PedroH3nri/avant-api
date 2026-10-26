"""Monta os services da conta e do Google com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.account.google_service import GoogleService
from avant_api.modules.account.redirects import GoogleRedirects
from avant_api.modules.account.service import AccountService


def account_service(services: Services = Depends(get_services)) -> AccountService:
    """O service da conta com banco, relógio, senhas, segredos, e-mail e limite."""
    return AccountService(
        services, services.clock, services.hasher, services.box, services.mailer, services.limiter
    )


def google_service(services: Services = Depends(get_services)) -> GoogleService:
    """O service do Google com banco, relógio, e-mail e o cliente OAuth, se houver."""
    return GoogleService(services, services.clock, services.mailer, services.google)


def google_redirects(services: Services = Depends(get_services)) -> GoogleRedirects:
    """Os redirecionamentos do fluxo do Google com as configurações da aplicação."""
    return GoogleRedirects(services.settings)
