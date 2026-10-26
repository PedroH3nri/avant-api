"""Monta o service da Empresa ativa com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.company.service import CompanyService


def company_service(services: Services = Depends(get_services)) -> CompanyService:
    """O service da Empresa com o banco e o relógio da aplicação."""
    return CompanyService(services, services.clock)
