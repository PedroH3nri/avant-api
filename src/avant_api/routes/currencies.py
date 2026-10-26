"""Moedas do painel e a moeda de visualização da pessoa: /api/v1/currencies e
/api/v1/auth/preferences.

A cotação é dado público, sem Empresa, e a moeda de visualização é da pessoa: as duas
rotas usam trusted_uow, como a conta.
"""

from avant_core.identity.application import Authenticated
from avant_core.money.application import set_display_currency
from avant_core.money.domain import BASE_CURRENCY, CURRENCIES
from fastapi import APIRouter, Depends

from avant_api.deps import get_auth, get_services, get_session_auth
from avant_api.schemas import CurrencyOut, PreferencesIn
from avant_api.services import Services

router = APIRouter(tags=["currencies"])


@router.get("/currencies")
def list_currencies(
    _: Authenticated = Depends(get_auth),
    services: Services = Depends(get_services),
) -> list[CurrencyOut]:
    """As moedas em que o painel mostra valores, e se já há cotação para cada uma."""
    with services.trusted_uow() as uow:
        available = {
            currency.code
            for currency in CURRENCIES
            if currency.code == BASE_CURRENCY or uow.exchange_rates.latest(currency.code)
        }
    return [
        CurrencyOut(
            code=currency.code,
            name=currency.name,
            symbol=currency.symbol,
            decimals=currency.decimals,
            available=currency.code in available,
        )
        for currency in CURRENCIES
    ]


@router.put("/auth/preferences")
def update_preferences(
    body: PreferencesIn,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> PreferencesIn:
    """Troca a moeda em que a pessoa vê os valores do painel."""
    user = set_display_currency(
        services.trusted_uow(), user_id=auth.user.id, currency=body.display_currency
    )
    return PreferencesIn(display_currency=user.display_currency)
