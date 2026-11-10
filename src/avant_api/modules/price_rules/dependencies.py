"""Monta o service das regras de preço com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.price_rules.service import PriceRuleService


def price_rule_service(services: Services = Depends(get_services)) -> PriceRuleService:
    """O service com o banco, o relógio e o cache dos floors."""
    return PriceRuleService(services, services.clock, services.rewards)
