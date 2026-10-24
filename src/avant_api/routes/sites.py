"""Sites e ad units: /api/v1/sites e /api/v1/ad-units.

Quem não vê todos os sites (papel com ``site_scope=assigned``) só recebe os atribuídos;
o resto responde 404, como se não existisse. A importação é do worker; aqui se lê, se
cadastra site à mão (aguardando o GAM), se liga ad unit a site e se atribui sites.
"""

import uuid

from avant_core.company.application import Actor
from avant_core.gam.domain import InventoryStatus
from avant_core.gam.inventory import (
    add_site,
    get_site,
    link_ad_unit,
    list_ad_units,
    list_sites,
    member_sites,
    remove_site,
    set_member_sites,
    site_members,
)
from fastapi import APIRouter, Depends, Query, status

from avant_api.deps import get_services, require
from avant_api.schemas import (
    AdUnitOut,
    AdUnitPatchIn,
    ItemsOut,
    MemberSitesIn,
    SiteDetailOut,
    SiteIn,
    SiteListOut,
    SiteMemberOut,
    SiteOut,
)
from avant_api.services import Services

router = APIRouter(tags=["sites"])


@router.get("/sites")
def index(
    network_id: uuid.UUID | None = None,
    approval_status: str | None = Query(default=None, max_length=40),
    query: str | None = Query(alias="q", default=None, max_length=200),
    include_archived: bool = False,
    actor: Actor = Depends(require("sites.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[SiteListOut]:
    """Lista os sites que quem age enxerga, com filtros."""
    views = list_sites(
        services.uow(actor.company_id),
        actor=actor,
        network_id=network_id,
        approval_status=approval_status,
        query=query,
        include_archived=include_archived,
    )
    return ItemsOut(items=[SiteListOut.of_view(view) for view in views])


@router.post("/sites", status_code=status.HTTP_201_CREATED)
def create(
    body: SiteIn,
    actor: Actor = Depends(require("sites.manage")),
    services: Services = Depends(get_services),
) -> SiteListOut:
    """Site pelo domínio, aguardando o GAM; a importação o junta ao site do mesmo domínio."""
    site = add_site(
        services.uow(actor.company_id), actor=actor, domain=body.domain, clock=services.clock
    )
    return SiteListOut(**SiteOut.of(site).model_dump(), ad_units=0)


@router.delete("/sites/{site_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Só o site que ainda aguarda o GAM; o do GAM sai de lá."""
    remove_site(services.uow(actor.company_id), actor=actor, site_id=site_id, clock=services.clock)


@router.get("/sites/{site_id}")
def show(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.view")),
    services: Services = Depends(get_services),
) -> SiteDetailOut:
    """Mostra um site com os ad units."""
    return SiteDetailOut.of_detail(
        get_site(services.uow(actor.company_id), actor=actor, site_id=site_id)
    )


@router.get("/sites/{site_id}/members")
def members(
    site_id: uuid.UUID,
    actor: Actor = Depends(require("sites.assign")),
    services: Services = Depends(get_services),
) -> ItemsOut[SiteMemberOut]:
    """Lista quem vê o site."""
    found = site_members(services.uow(actor.company_id), actor=actor, site_id=site_id)
    return ItemsOut(items=[SiteMemberOut.of_site_member(member) for member in found])


@router.get("/ad-units")
def ad_units(
    network_id: uuid.UUID | None = None,
    site_id: uuid.UUID | None = None,
    status: InventoryStatus | None = None,
    unlinked: bool = False,
    actor: Actor = Depends(require("sites.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[AdUnitOut]:
    """Lista plana; a tela monta a árvore pelos ``parent_id``."""
    units = list_ad_units(
        services.uow(actor.company_id),
        actor=actor,
        network_id=network_id,
        site_id=site_id,
        status=status,
        unlinked=unlinked,
    )
    return ItemsOut(items=[AdUnitOut.of(unit) for unit in units])


@router.patch("/ad-units/{ad_unit_id}")
def link(
    ad_unit_id: uuid.UUID,
    body: AdUnitPatchIn,
    actor: Actor = Depends(require("sites.assign")),
    services: Services = Depends(get_services),
) -> AdUnitOut:
    """Liga ou desliga à mão um ad unit de um site."""
    unit = link_ad_unit(
        services.uow(actor.company_id),
        actor=actor,
        ad_unit_id=ad_unit_id,
        site_id=body.site_id,
        automatic=body.automatic,
        clock=services.clock,
    )
    return AdUnitOut.of(unit)


@router.get("/members/{membership_id}/sites")
def sites_of_member(
    membership_id: uuid.UUID,
    actor: Actor = Depends(require("team.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[SiteOut]:
    """Lista os sites atribuídos a um membro."""
    found = member_sites(services.uow(actor.company_id), actor=actor, membership_id=membership_id)
    return ItemsOut(items=[SiteOut.of(site) for site in found])


@router.put("/members/{membership_id}/sites")
def assign_sites(
    membership_id: uuid.UUID,
    body: MemberSitesIn,
    actor: Actor = Depends(require("sites.assign")),
    services: Services = Depends(get_services),
) -> ItemsOut[SiteOut]:
    """A lista inteira: o que não vier deixa de estar atribuído."""
    found = set_member_sites(
        services.uow(actor.company_id),
        actor=actor,
        membership_id=membership_id,
        site_ids=body.site_ids,
        clock=services.clock,
    )
    return ItemsOut(items=[SiteOut.of(site) for site in found])
