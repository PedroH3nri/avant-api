"""Monta o service das pessoas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.people.service import PeopleService


def people_service(services: Services = Depends(get_services)) -> PeopleService:
    """O service das pessoas com o banco, o relógio e o e-mail da aplicação."""
    return PeopleService(services, services.clock, services.mailer)
