"""Filtros de período e de listagem que o painel do cliente e o interno usam."""

import uuid

from avant_core.facebook.enums import FacebookLevel
from avant_core.facebook.models import FacebookObjectFilter
from fastapi import Query

from avant_api.shared.ads import period

__all__ = ["object_filter", "period"]


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
