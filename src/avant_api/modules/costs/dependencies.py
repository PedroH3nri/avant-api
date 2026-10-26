"""Monta o service dos custos com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.costs.service import CostService


def cost_service(services: Services = Depends(get_services)) -> CostService:
    """O service dos custos com o banco e o relógio da aplicação."""
    return CostService(services, services.clock)
