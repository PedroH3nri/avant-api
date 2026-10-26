"""Monta o service dos sites com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.sites.service import SiteService


def site_service(services: Services = Depends(get_services)) -> SiteService:
    """O service dos sites com o banco e o relógio da aplicação."""
    return SiteService(services, services.clock)
