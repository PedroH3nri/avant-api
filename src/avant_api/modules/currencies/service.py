"""Service das moedas do painel e da moeda de visualização da pessoa.

A cotação é dado público, sem Empresa, e a moeda é da pessoa: os dois usam trusted_uow.
"""

import uuid

from avant_core.money.catalog import BASE_CURRENCY, CURRENCIES
from avant_core.money.services import set_display_currency

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.currencies.dto import CurrencyOut, PreferencesIn


class CurrencyService:
    """Moedas disponíveis e preferência de moeda."""

    def __init__(self, uows: UnitOfWorkFactory) -> None:
        self._uows = uows

    def list_all(self) -> list[CurrencyOut]:
        """As moedas em que o painel mostra valores, e se já há cotação para cada uma."""
        with self._uows.trusted_uow() as uow:
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

    def set_preferences(self, user_id: uuid.UUID, body: PreferencesIn) -> PreferencesIn:
        """Troca a moeda em que a pessoa vê os valores do painel."""
        user = set_display_currency(
            self._uows.trusted_uow(), user_id=user_id, currency=body.display_currency
        )
        return PreferencesIn(display_currency=user.display_currency)
