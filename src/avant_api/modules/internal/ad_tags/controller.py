"""Ad tags de todos os clientes: /api/v1/internal/ad-tags e /internal/sites/{id}/ad-tag-units.

Ver pede ``internal.ad_tags.view``; mexer pede ``internal.ad_tags.manage``. Toda ação grava na
auditoria do cliente.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.ad_tags.dependencies import client_ad_tag_service
from avant_api.modules.internal.ad_tags.dto import (
    AdTagActiveIn,
    AdTagCreateIn,
    AdTagIn,
    AdTagOut,
    AdTagPublishIn,
    AdTagUnitDayOut,
    AdTagVersionOut,
)
from avant_api.modules.internal.ad_tags.service import ClientAdTagService
from avant_api.shared.dto import PageOut

VIEW = "internal.ad_tags.view"
MANAGE = "internal.ad_tags.manage"

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/ad-tags")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    company_id: uuid.UUID | None = Query(default=None),
    site_id: uuid.UUID | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> PageOut[AdTagOut]:
    """Uma página das ad tags dos clientes, a mais nova primeiro, com busca no nome e na chave."""
    return service.page(actor, page, company_id, site_id, query)


@router.post("/ad-tags", status_code=status.HTTP_201_CREATED)
def create(
    body: AdTagCreateIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Cria uma ad tag vazia no site de um cliente."""
    return service.create(actor, body)


@router.get("/ad-tags/{ad_tag_id}")
def show(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Uma ad tag com o rascunho e a versão no ar."""
    return service.get(actor, ad_tag_id)


@router.put("/ad-tags/{ad_tag_id}")
def update(
    ad_tag_id: uuid.UUID,
    body: AdTagIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Guarda o nome e o rascunho, sem publicar."""
    return service.update(actor, ad_tag_id, body)


@router.patch("/ad-tags/{ad_tag_id}")
def set_active(
    ad_tag_id: uuid.UUID,
    body: AdTagActiveIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Pausa ou ativa a ad tag."""
    return service.set_active(actor, ad_tag_id, body.active)


@router.delete("/ad-tags/{ad_tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> None:
    """Apaga a ad tag."""
    service.delete(actor, ad_tag_id)


@router.post("/ad-tags/{ad_tag_id}/publish")
def publish(
    ad_tag_id: uuid.UUID,
    body: AdTagPublishIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Publica o rascunho como versão nova."""
    return service.publish(actor, ad_tag_id, body.note)


@router.get("/ad-tags/{ad_tag_id}/versions")
def versions(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> list[AdTagVersionOut]:
    """As versões publicadas, a mais nova primeiro."""
    return service.versions(actor, ad_tag_id)


@router.post("/ad-tags/{ad_tag_id}/versions/{number}/restore")
def restore(
    ad_tag_id: uuid.UUID,
    number: int,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> AdTagOut:
    """Volta para uma versão antiga, publicada como versão nova."""
    return service.restore(actor, ad_tag_id, number)


@router.get("/sites/{site_id}/ad-tag-units")
def units(
    site_id: uuid.UUID,
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientAdTagService = Depends(client_ad_tag_service),
) -> list[AdTagUnitDayOut]:
    """Os dias com blocos de ad tag no site de um cliente."""
    return service.units(actor, site_id)
