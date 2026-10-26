"""Monta o service do 2FA com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.mfa.service import MfaService


def mfa_service(services: Services = Depends(get_services)) -> MfaService:
    """O service do 2FA com o banco, o relógio e a caixa de segredos."""
    return MfaService(services, services.clock, services.box)
