"""Google Ads de todos os clientes: /api/v1/internal/google-ads. Só leitura.

Tudo pede ``internal.google_ads.view``. A equipe Groone não muda nada no Google Ads dos
clientes.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.google_ads.enums import GoogleAdsChangeOrigin, GoogleAdsLevel
from avant_core.google_ads.models import GoogleAdsObjectFilter
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require_staff
from avant_api.modules.google_ads.dto import (
    GoogleAdsAccountOut,
    GoogleAdsAlertOut,
    GoogleAdsChangeOut,
    GoogleAdsKeywordOut,
    GoogleAdsObjectDetailOut,
    GoogleAdsObjectOut,
)
from avant_api.modules.google_ads.http import object_filter
from avant_api.modules.internal.google_ads.dependencies import client_google_ads_service
from avant_api.modules.internal.google_ads.service import ClientGoogleAdsService
from avant_api.shared.ads import period
from avant_api.shared.dto import PageOut

VIEW = "internal.google_ads.view"

router = APIRouter(prefix="/internal/google-ads", tags=["internal"])


@router.get("/accounts")
def accounts(
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> list[GoogleAdsAccountOut]:
    """As contas de todos os clientes, ou de um, com quem usa e o gasto do mês."""
    return service.accounts(actor, company_id)


@router.get("/objects")
def objects(
    filters: GoogleAdsObjectFilter = Depends(object_filter),
    dates: tuple[date, date] = Depends(period),
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> PageOut[GoogleAdsObjectOut]:
    """Uma página das campanhas, grupos ou anúncios dos clientes com os números."""
    return service.objects(actor, filters, dates[0], dates[1], page, company_id)


@router.get("/objects/{level}/{external_id}")
def show_object(
    level: GoogleAdsLevel,
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> GoogleAdsObjectDetailOut:
    """Uma campanha, grupo ou anúncio de um cliente com os números por dia."""
    return service.object(actor, level, external_id, dates[0], dates[1])


@router.get("/ad-groups/{external_id}/keywords")
def keywords(
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> list[GoogleAdsKeywordOut]:
    """As palavras-chave de um grupo de um cliente com os números."""
    return service.keywords(actor, external_id, dates[0], dates[1])


@router.get("/changes")
def changes(
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    account_id: uuid.UUID | None = Query(default=None),
    object_id: str | None = Query(default=None, max_length=40),
    origin: GoogleAdsChangeOrigin | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> PageOut[GoogleAdsChangeOut]:
    """Uma página do histórico dos clientes."""
    return service.changes(actor, page, company_id, account_id, object_id, origin)


@router.get("/alerts")
def alerts(
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientGoogleAdsService = Depends(client_google_ads_service),
) -> PageOut[GoogleAdsAlertOut]:
    """Uma página dos avisos dos clientes."""
    return service.alerts(actor, page, company_id)
