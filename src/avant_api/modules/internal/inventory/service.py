"""Service das networks e dos sites dos clientes, vistos pela equipe Groone."""

from avant_core.access.models import Actor
from avant_core.internal.services import page_client_networks, page_client_sites
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.inventory.dto import ClientNetworkOut, ClientSiteOut
from avant_api.shared.dto import PageOut, page_out


class ClientInventoryService:
    """Lê as networks e os sites de todas as Empresas cliente, sem RLS."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def networks(self, actor: Actor, query: str | None, page: int) -> PageOut[ClientNetworkOut]:
        """Uma página das networks dos clientes com o status de faturamento."""
        found = page_client_networks(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, query=query, page=page
        )
        return page_out(found, ClientNetworkOut.of_view)

    def sites(self, actor: Actor, query: str | None, page: int) -> PageOut[ClientSiteOut]:
        """Uma página dos sites dos clientes com o status de faturamento."""
        found = page_client_sites(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, query=query, page=page
        )
        return page_out(found, ClientSiteOut.of_view)
