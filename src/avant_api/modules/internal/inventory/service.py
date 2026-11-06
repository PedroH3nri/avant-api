"""Service das networks e dos sites dos clientes, vistos pela equipe Groone."""

import uuid

from avant_core.access.models import Actor
from avant_core.internal.services import page_client_networks, page_client_sites
from avant_core.shared.clock import Clock
from avant_core.site_checklists.services import site_checklist_progress

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.inventory.dto import (
    ClientNetworkOut,
    ClientSiteChecklistOut,
    ClientSiteOut,
)
from avant_api.shared.dto import PageOut, page_out

CHECKLISTS = "internal.checklists.view"


class ClientInventoryService:
    """Lê as networks e os sites de todas as Empresas cliente, sem RLS."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def networks(
        self,
        actor: Actor,
        query: str | None,
        page: int,
        awaiting_confirmation: bool = False,
        client_id: uuid.UUID | None = None,
    ) -> PageOut[ClientNetworkOut]:
        """Uma página das networks dos clientes com o status de faturamento."""
        found = page_client_networks(
            self._uows.trusted_uow(),
            actor=actor,
            clock=self._clock,
            query=query,
            page=page,
            awaiting_confirmation=awaiting_confirmation,
            company_id=client_id,
        )
        return page_out(found, ClientNetworkOut.of_view)

    def sites(self, actor: Actor, query: str | None, page: int) -> PageOut[ClientSiteOut]:
        """Uma página dos sites dos clientes com o status de faturamento."""
        found = page_client_sites(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, query=query, page=page
        )
        listed = page_out(found, ClientSiteOut.of_view)
        if actor.grants.can(CHECKLISTS) and listed.items:
            self._add_checklists(listed.items)
        return listed

    def _add_checklists(self, sites: list[ClientSiteOut]) -> None:
        """Põe em cada site o checklist do mês atual e quantos itens estão ok."""
        with self._uows.trusted_uow() as uow:
            progress = site_checklist_progress(
                uow, site_ids={site.id for site in sites}, clock=self._clock
            )
        for site in sites:
            if site.id in progress:
                checklist_id, found = progress[site.id]
                site.checklist = ClientSiteChecklistOut(
                    id=checklist_id, done=found.done, total=found.total, complete=found.complete
                )
