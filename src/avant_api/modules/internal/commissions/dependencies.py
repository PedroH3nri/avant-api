"""Monta o service da comissão com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.commissions.service import CommissionService


def commission_service(services: Services = Depends(get_services)) -> CommissionService:
    """O service da comissão com o banco e o relógio da aplicação."""
    return CommissionService(services, services.clock)
