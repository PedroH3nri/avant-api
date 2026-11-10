"""Ad tags da Empresa ativa: /api/v1/ad-tags e /api/v1/sites/{id}/ad-tag-units.

Ver pede ``ad_tags.view``; criar, editar, publicar, voltar versão, pausar e apagar pedem
``ad_tags.manage``. Quem tem só alguns sites atribuídos vê e mexe só nas tags deles (o core
confere). O site só recebe o que foi publicado.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require
from avant_api.modules.ad_tags.dependencies import ad_tag_service
from avant_api.modules.ad_tags.dto import (
    AdTagActiveIn,
    AdTagCreateIn,
    AdTagIn,
    AdTagOut,
    AdTagPublishIn,
    AdTagUnitDayOut,
    AdTagVersionOut,
)
from avant_api.modules.ad_tags.service import AdTagService
from avant_api.shared.dto import PageOut

VIEW = "ad_tags.view"
MANAGE = "ad_tags.manage"

router = APIRouter(tags=["ad-tags"])


@router.get("/ad-tags")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    site_id: uuid.UUID | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: AdTagService = Depends(ad_tag_service),
) -> PageOut[AdTagOut]:
    """Uma página das ad tags, a mais nova primeiro, com busca no nome e na chave."""
    return service.page(actor, page, site_id, query)


@router.post("/ad-tags", status_code=status.HTTP_201_CREATED)
def create(
    body: AdTagCreateIn,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Cria uma ad tag vazia num site."""
    return service.create(actor, body)


@router.get("/ad-tags/{ad_tag_id}")
def show(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Uma ad tag com o rascunho e a versão no ar."""
    return service.get(actor, ad_tag_id)


@router.put("/ad-tags/{ad_tag_id}")
def update(
    ad_tag_id: uuid.UUID,
    body: AdTagIn,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Guarda o nome e o rascunho, sem publicar."""
    return service.update(actor, ad_tag_id, body)


@router.patch("/ad-tags/{ad_tag_id}")
def set_active(
    ad_tag_id: uuid.UUID,
    body: AdTagActiveIn,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Pausa ou ativa a ad tag; pausada, o site não recebe blocos."""
    return service.set_active(actor, ad_tag_id, body.active)


@router.delete("/ad-tags/{ad_tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> None:
    """Apaga a ad tag; a chave para de responder."""
    service.delete(actor, ad_tag_id)


@router.post("/ad-tags/{ad_tag_id}/publish")
def publish(
    ad_tag_id: uuid.UUID,
    body: AdTagPublishIn,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Publica o rascunho como versão nova."""
    return service.publish(actor, ad_tag_id, body.note)


@router.get("/ad-tags/{ad_tag_id}/versions")
def versions(
    ad_tag_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: AdTagService = Depends(ad_tag_service),
) -> list[AdTagVersionOut]:
    """As versões publicadas, a mais nova primeiro."""
    return service.versions(actor, ad_tag_id)


@router.post("/ad-tags/{ad_tag_id}/versions/{number}/restore")
def restore(
    ad_tag_id: uuid.UUID,
    number: int,
    actor: Actor = Depends(require(MANAGE)),
    service: AdTagService = Depends(ad_tag_service),
) -> AdTagOut:
    """Volta para uma versão antiga, publicada como versão nova."""
    return service.restore(actor, ad_tag_id, number)


@router.get("/sites/{site_id}/ad-tag-units")
def units(
    site_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: AdTagService = Depends(ad_tag_service),
) -> list[AdTagUnitDayOut]:
    """Os dias com blocos de ad tag no site e os tipos de cada dia, o mais recente primeiro."""
    return service.units(actor, site_id)
