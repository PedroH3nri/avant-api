"""Monta o service da equipe Groone com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.staff.service import StaffService


def staff_service(services: Services = Depends(get_services)) -> StaffService:
    """O service da equipe Groone com o banco, o relógio e o e-mail da aplicação."""
    return StaffService(services, services.clock, services.mailer)
