"""Moedas do painel e a moeda de visualização da pessoa: /api/v1/currencies e
/api/v1/auth/preferences.
"""

from avant_core.identity.service import Authenticated
from fastapi import APIRouter, Depends

from avant_api.app.security import get_auth, get_session_auth
from avant_api.modules.currencies.dependencies import currency_service
from avant_api.modules.currencies.dto import CurrencyOut, PreferencesIn
from avant_api.modules.currencies.service import CurrencyService

router = APIRouter(tags=["currencies"])


@router.get("/currencies")
def list_currencies(
    _: Authenticated = Depends(get_auth),
    service: CurrencyService = Depends(currency_service),
) -> list[CurrencyOut]:
    """As moedas em que o painel mostra valores, e se já há cotação para cada uma."""
    return service.list_all()


@router.put("/auth/preferences")
def update_preferences(
    body: PreferencesIn,
    auth: Authenticated = Depends(get_session_auth),
    service: CurrencyService = Depends(currency_service),
) -> PreferencesIn:
    """Troca a moeda em que a pessoa vê os valores do painel."""
    return service.set_preferences(auth.user.id, body)
