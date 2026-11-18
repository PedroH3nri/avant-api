"""Filtros de período e de listagem que o painel do cliente e o interno usam."""

import uuid
from datetime import date, timedelta

from avant_core.facebook.enums import FacebookLevel
from avant_core.facebook.models import FacebookObjectFilter
from fastapi import Query

DEFAULT_DAYS = 7


def period(
    start: date | None = Query(default=None, alias="from"),
    end: date | None = Query(default=None, alias="to"),
) -> tuple[date, date]:
    """O período pedido; sem ele, os últimos 7 dias até hoje (o core confere o tamanho)."""
    last = end or date.today()
    return start or last - timedelta(days=DEFAULT_DAYS - 1), last


def object_filter(
    level: FacebookLevel = Query(default=FacebookLevel.CAMPAIGN),
    account_id: uuid.UUID | None = Query(default=None),
    parent: str | None = Query(default=None, max_length=40),
    active: bool | None = Query(default=None),
    in_review: bool = Query(default=False),
    query: str | None = Query(alias="q", default=None, max_length=200),
) -> FacebookObjectFilter:
    """Nível, conta, objeto acima, ligado ou pausado, em revisão e a busca no nome."""
    return FacebookObjectFilter(
        level=level,
        account_id=account_id,
        parent_external_id=parent,
        active=active,
        in_review=in_review,
        query=query,
    )
