"""Sites e ad units: /api/v1/sites e /api/v1/ad-units.

Fora do alcance de quem age, o site responde 404, como se não existisse. A importação é
do worker; aqui se lê, se cadastra site à mão (aguardando o GAM), se liga ad unit a site
e se atribui sites.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.gam.inventory.enums import InventoryStatus
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require
from avant_api.modules.sites.dependencies import site_service
from avant_api.modules.sites.dto import (
    AdUnitOut,
    AdUnitPatchIn,
    MemberSitesIn,
    SiteDetailOut,
    SiteIn,
    SiteListOut,
    SiteMemberOut,
    SiteOut,
)
from avant_api.modules.sites.service import SiteService
from avant_api.shared.dto import ItemsOut, PageOut

router = APIRouter(tags=["sites"])


@router.get("/sites")
def index(
    network_id: uuid.UUID | None = None,
    approval_status: str | None = Query(default=None, max_length=40),
    query: str | None = Query(alias="q", default=None, max_length=200),
    include_archived: bool = False,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("sites.view")),
    service: SiteService = Depends(site_service),
) -> PageOut[SiteListOut]:
    """Uma página dos sites que quem age enxerga, o mais recente primeiro, com filtros."""
    return service.page(actor, network_id, approval_status, query, include_archived, page)


@router.get("/sites/options")
def site_options(
    actor: Actor = Depends(require("sites.view")),
    service: SiteService = Depends(site_service),
) -> ItemsOut[SiteListOut]:
    """Todos os sites ativos que quem age enxerga, para seletores e telas que juntam dados."""
    return ItemsOut(items=service.list_all(actor))


@router.post("/sites", status_code=status.HTTP_201_CREATED)
def create(
    body: SiteIn,
    actor: Actor = Depends(require("sites.manage")),
    service: SiteService = Depends(site_service),
) -> SiteListOut:
    """Site pelo domínio, aguardando o GAM; a importação o junta ao site do mesmo domínio."""
    return service.create(actor, body.domain)


@router.delete("/sites/{site_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.manage")),
    service: SiteService = Depends(site_service),
) -> None:
    """Só o site que ainda aguarda o GAM; o do GAM sai de lá."""
    service.delete(actor, site_id)


@router.get("/sites/{site_id}")
def show(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.view")),
    service: SiteService = Depends(site_service),
) -> SiteDetailOut:
    """Mostra um site com os ad units."""
    return service.show(actor, site_id)


@router.get("/sites/{site_id}/members")
def members(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.assign")),
    service: SiteService = Depends(site_service),
) -> ItemsOut[SiteMemberOut]:
    """Lista quem vê o site."""
    return ItemsOut(items=service.members(actor, site_id))


@router.get("/ad-units/unlinked")
def unlinked(
    network_id: uuid.UUID | None = None,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("sites.view")),
    service: SiteService = Depends(site_service),
) -> PageOut[AdUnitOut]:
    """Uma página dos ad units sem site; só quem vê todos os sites os enxerga."""
    return service.unlinked(actor, network_id, page)


@router.get("/ad-units")
def ad_units(
    network_id: uuid.UUID | None = None,
    site_id: uuid.UUID | None = None,
    status: InventoryStatus | None = None,
    unlinked: bool = False,
    actor: Actor = Depends(require("sites.view")),
    service: SiteService = Depends(site_service),
) -> ItemsOut[AdUnitOut]:
    """Lista plana; a tela monta a árvore pelos ``parent_id``."""
    return ItemsOut(items=service.ad_units(actor, network_id, site_id, status, unlinked))


@router.patch("/ad-units/{ad_unit_id}")
def link(
    ad_unit_id: uuid.UUID,
    body: AdUnitPatchIn,
    actor: Actor = Depends(require("sites.assign")),
    service: SiteService = Depends(site_service),
) -> AdUnitOut:
    """Liga ou desliga à mão um ad unit de um site."""
    return service.link(actor, ad_unit_id, body)


@router.get("/members/{membership_id}/sites")
def sites_of_member(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.view")),
    service: SiteService = Depends(site_service),
) -> ItemsOut[SiteOut]:
    """Lista os sites atribuídos a um membro."""
    return ItemsOut(items=service.sites_of_member(actor, membership_id))


@router.put("/members/{membership_id}/sites")
def assign_sites(
    membership_id: uuid.UUID,
    body: MemberSitesIn,
    actor: Actor = Depends(require("sites.assign")),
    service: SiteService = Depends(site_service),
) -> ItemsOut[SiteOut]:
    """A lista inteira: o que não vier deixa de estar atribuído."""
    return ItemsOut(items=service.assign(actor, membership_id, body.site_ids))
