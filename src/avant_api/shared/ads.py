"""O que as integrações de anúncios (Facebook e Google Ads) usam igual: o período pedido, dinheiro
em micros e a pessoa resumida."""

import uuid
from datetime import date, timedelta
from decimal import Decimal

from avant_core.identity.models import User
from fastapi import Query
from pydantic import BaseModel

DEFAULT_DAYS = 7
MICROS = Decimal(1_000_000)
MAX_LIMIT = Decimal(1_000_000_000)


def period(
    start: date | None = Query(default=None, alias="from"),
    end: date | None = Query(default=None, alias="to"),
) -> tuple[date, date]:
    """O período pedido; sem ele, os últimos 7 dias até hoje (o core confere o tamanho)."""
    last = end or date.today()
    return start or last - timedelta(days=DEFAULT_DAYS - 1), last


def money(micros: int | None) -> Decimal | None:
    """Micros para o valor na moeda; vazio continua vazio."""
    return None if micros is None else Decimal(micros) / MICROS


def micros(amount: Decimal | None) -> int | None:
    """O valor na moeda para micros; vazio é sem limite."""
    return None if amount is None else int(amount * MICROS)


class PersonRefOut(BaseModel):
    id: uuid.UUID
    name: str
    email: str

    @classmethod
    def of(cls, user: User | None) -> "PersonRefOut | None":
        """A pessoa resumida, ou vazio."""
        return None if user is None else cls(id=user.id, name=user.name, email=user.email)
