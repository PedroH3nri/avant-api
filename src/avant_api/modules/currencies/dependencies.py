"""Monta o service das moedas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.currencies.service import CurrencyService


def currency_service(services: Services = Depends(get_services)) -> CurrencyService:
    """O service das moedas com o banco da aplicação."""
    return CurrencyService(services)
