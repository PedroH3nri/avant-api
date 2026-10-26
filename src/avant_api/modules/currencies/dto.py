"""DTOs de entrada e saída do domínio currencies. Datas sempre em ISO 8601 UTC."""

from pydantic import BaseModel, Field


class CurrencyOut(BaseModel):
    code: str
    name: str
    symbol: str
    decimals: int
    # Já existe cotação para converter (o dólar sempre tem).
    available: bool


class PreferencesIn(BaseModel):
    display_currency: str = Field(min_length=3, max_length=3)
