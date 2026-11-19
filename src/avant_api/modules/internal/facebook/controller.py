"""Facebook de todos os clientes: /api/v1/internal/facebook. Só leitura.

Tudo pede ``internal.facebook.view``. A equipe Groone não muda nada no Facebook dos clientes.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.facebook.enums import FacebookChangeOrigin
from avant_core.facebook.models import FacebookObjectFilter
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require_staff
from avant_api.modules.facebook.http import object_filter, period
from avant_api.modules.internal.facebook.dependencies import client_facebook_service
from avant_api.modules.internal.facebook.dto import (
    FacebookAccountOut,
    FacebookAlertOut,
    FacebookChangeOut,
    FacebookObjectDetailOut,
    FacebookObjectOut,
)
from avant_api.modules.internal.facebook.service import ClientFacebookService
from avant_api.shared.dto import PageOut

VIEW = "internal.facebook.view"

router = APIRouter(prefix="/internal/facebook", tags=["internal"])


@router.get("/accounts")
def accounts(
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientFacebookService = Depends(client_facebook_service),
) -> list[FacebookAccountOut]:
    """As contas de todos os clientes, ou de um, com quem usa e o gasto do mês."""
    return service.accounts(actor, company_id)


@router.get("/objects")
def objects(
    filters: FacebookObjectFilter = Depends(object_filter),
    dates: tuple[date, date] = Depends(period),
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientFacebookService = Depends(client_facebook_service),
) -> PageOut[FacebookObjectOut]:
    """Uma página das campanhas, conjuntos ou anúncios dos clientes com os números."""
    return service.objects(actor, filters, dates[0], dates[1], page, company_id)


@router.get("/objects/{external_id}")
def show_object(
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientFacebookService = Depends(client_facebook_service),
) -> FacebookObjectDetailOut:
    """Uma campanha, conjunto ou anúncio de um cliente com os números por dia e por país."""
    return service.object(actor, external_id, dates[0], dates[1])


@router.get("/changes")
def changes(
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    account_id: uuid.UUID | None = Query(default=None),
    object_id: str | None = Query(default=None, max_length=40),
    origin: FacebookChangeOrigin | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientFacebookService = Depends(client_facebook_service),
) -> PageOut[FacebookChangeOut]:
    """Uma página do histórico dos clientes."""
    return service.changes(actor, page, company_id, account_id, object_id, origin)


@router.get("/alerts")
def alerts(
    page: int = Query(default=1, ge=1),
    company_id: uuid.UUID | None = Query(default=None),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientFacebookService = Depends(client_facebook_service),
) -> PageOut[FacebookAlertOut]:
    """Uma página dos avisos dos clientes."""
    return service.alerts(actor, page, company_id)
