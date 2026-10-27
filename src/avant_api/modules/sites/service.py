"""Service dos sites, ad units e sites atribuídos a membros.

Quem não vê todos os sites (papel com ``site_scope=assigned``) só recebe os atribuídos.
"""

import uuid

from avant_core.company.service import Actor
from avant_core.gam.inventory_service import (
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
from avant_core.gam.model import InventoryStatus
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.sites.dto import (
    AdUnitOut,
    AdUnitPatchIn,
    SiteDetailOut,
    SiteListOut,
    SiteMemberOut,
    SiteOut,
)


class SiteService:
    """Leitura e cadastro manual do inventário da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(
        self,
        actor: Actor,
        network_id: uuid.UUID | None,
        approval_status: str | None,
        query: str | None,
        include_archived: bool,
    ) -> list[SiteListOut]:
        """Os sites que quem age enxerga, com filtros."""
        views = list_sites(
            self._uows.uow(actor.company_id),
            actor=actor,
            network_id=network_id,
            approval_status=approval_status,
            query=query,
            include_archived=include_archived,
        )
        return [SiteListOut.of_view(view) for view in views]

    def create(self, actor: Actor, domain: str) -> SiteListOut:
        """Site pelo domínio, aguardando o GAM."""
        site = add_site(
            self._uows.uow(actor.company_id), actor=actor, domain=domain, clock=self._clock
        )
        return SiteListOut(**SiteOut.of(site).model_dump(), ad_units=0)

    def delete(self, actor: Actor, site_id: uuid.UUID) -> None:
        """Apaga um site que ainda aguarda o GAM."""
        remove_site(
            self._uows.uow(actor.company_id), actor=actor, site_id=site_id, clock=self._clock
        )

    def show(self, actor: Actor, site_id: uuid.UUID) -> SiteDetailOut:
        """Um site com os ad units."""
        return SiteDetailOut.of_detail(
            get_site(self._uows.uow(actor.company_id), actor=actor, site_id=site_id)
        )

    def members(self, actor: Actor, site_id: uuid.UUID) -> list[SiteMemberOut]:
        """Quem vê o site."""
        found = site_members(self._uows.uow(actor.company_id), actor=actor, site_id=site_id)
        return [SiteMemberOut.of_site_member(member) for member in found]

    def ad_units(
        self,
        actor: Actor,
        network_id: uuid.UUID | None,
        site_id: uuid.UUID | None,
        status: InventoryStatus | None,
        unlinked: bool,
    ) -> list[AdUnitOut]:
        """Os ad units em lista plana, com filtros."""
        units = list_ad_units(
            self._uows.uow(actor.company_id),
            actor=actor,
            network_id=network_id,
            site_id=site_id,
            status=status,
            unlinked=unlinked,
        )
        return [AdUnitOut.of(unit) for unit in units]

    def link(self, actor: Actor, ad_unit_id: uuid.UUID, body: AdUnitPatchIn) -> AdUnitOut:
        """Liga ou desliga à mão um ad unit de um site."""
        unit = link_ad_unit(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_unit_id=ad_unit_id,
            site_id=body.site_id,
            automatic=body.automatic,
            clock=self._clock,
        )
        return AdUnitOut.of(unit)

    def sites_of_member(self, actor: Actor, membership_id: uuid.UUID) -> list[SiteOut]:
        """Os sites atribuídos a um membro."""
        found = member_sites(
            self._uows.uow(actor.company_id), actor=actor, membership_id=membership_id
        )
        return [SiteOut.of(site) for site in found]

    def assign(
        self, actor: Actor, membership_id: uuid.UUID, site_ids: list[uuid.UUID]
    ) -> list[SiteOut]:
        """Troca a lista inteira de sites atribuídos ao membro."""
        found = set_member_sites(
            self._uows.uow(actor.company_id),
            actor=actor,
            membership_id=membership_id,
            site_ids=site_ids,
            clock=self._clock,
        )
        return [SiteOut.of(site) for site in found]
