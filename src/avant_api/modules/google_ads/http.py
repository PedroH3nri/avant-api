"""Filtros de listagem do Google Ads que o painel do cliente e o interno usam."""

import uuid

from avant_core.google_ads.enums import GoogleAdsLevel
from avant_core.google_ads.models import GoogleAdsObjectFilter
from fastapi import Query


def object_filter(
    level: GoogleAdsLevel = Query(default=GoogleAdsLevel.CAMPAIGN),
    account_id: uuid.UUID | None = Query(default=None),
    parent: str | None = Query(default=None, max_length=40),
    active: bool | None = Query(default=None),
    with_issues: bool = Query(default=False),
    query: str | None = Query(alias="q", default=None, max_length=200),
) -> GoogleAdsObjectFilter:
    """Nível, conta, objeto acima, ligado ou pausado, com problema na revisão e a busca no
    nome."""
    return GoogleAdsObjectFilter(
        level=level,
        account_id=account_id,
        parent_external_id=parent,
        active=active,
        with_issues=with_issues,
        query=query,
    )
