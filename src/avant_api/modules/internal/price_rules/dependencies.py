"""Monta o service das regras de preço dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.price_rules.service import ClientPriceRuleService


def client_price_rule_service(
    services: Services = Depends(get_services),
) -> ClientPriceRuleService:
    """O service com o banco, o relógio e o cache dos floors."""
    return ClientPriceRuleService(services, services.clock, services.rewards)
