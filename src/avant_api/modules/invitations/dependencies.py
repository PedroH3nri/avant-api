"""Monta o service dos convites com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.invitations.service import InvitationService


def invitation_service(services: Services = Depends(get_services)) -> InvitationService:
    """O service dos convites com o banco, o relógio e o e-mail da aplicação."""
    return InvitationService(services, services.clock, services.mailer)
