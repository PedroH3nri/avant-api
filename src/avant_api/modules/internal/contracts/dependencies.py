"""Monta o service dos contratos com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.contracts.service import ContractService


def contract_service(services: Services = Depends(get_services)) -> ContractService:
    """O service dos contratos com o banco e o relógio da aplicação."""
    return ContractService(services, services.clock)
