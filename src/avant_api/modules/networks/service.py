"""Service das networks do Google Ad Manager da Empresa ativa.

A API não fala com o GAM: conectar e sincronizar gravam o pedido e enfileiram
``avant.gam.sync_network`` no avant-worker, que tem a chave da conta de serviço.
"""

import uuid

from avant_core.company.service import Actor
from avant_core.gam.model import Network
from avant_core.gam.service import (
    connect_network,
    disconnect_network,
    get_network,
    list_networks,
    list_sync_runs,
    request_sync,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import SYNC_NETWORK, TaskQueue
from avant_api.modules.networks.dto import NetworkDetailOut, NetworkIn, SyncRunOut


def enqueue_sync(tasks: TaskQueue, network: Network) -> None:
    """Agenda no worker a sincronização da network."""
    tasks.send(SYNC_NETWORK, str(network.company_id), str(network.id))


class NetworkService:
    """Conectar, sincronizar, listar e desconectar networks."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, tasks: TaskQueue, service_account: str
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._tasks = tasks
        self.service_account = service_account

    def list_all(self, actor: Actor) -> list[NetworkDetailOut]:
        """As networks da Empresa ativa."""
        views = list_networks(self._uows.uow(actor.company_id), actor=actor)
        return [NetworkDetailOut.of_view(view) for view in views]

    def show(self, actor: Actor, network_id: uuid.UUID) -> NetworkDetailOut:
        """Uma network com sites e últimas sincronizações."""
        view = get_network(self._uows.uow(actor.company_id), actor=actor, network_id=network_id)
        return NetworkDetailOut.of_view(view)

    def connect(self, actor: Actor, body: NetworkIn) -> NetworkDetailOut:
        """A network nasce pendente e o worker testa o acesso em seguida."""
        network = connect_network(
            self._uows.uow(actor.company_id),
            actor=actor,
            network_code=body.network_code,
            clock=self._clock,
        )
        enqueue_sync(self._tasks, network)
        return self.show(actor, network.id)

    def sync(self, actor: Actor, network_id: uuid.UUID) -> NetworkDetailOut:
        """Pede uma sincronização; no máximo uma a cada 10 minutos."""
        network = request_sync(
            self._uows.uow(actor.company_id),
            actor=actor,
            network_id=network_id,
            clock=self._clock,
        )
        enqueue_sync(self._tasks, network)
        return self.show(actor, network.id)

    def sync_runs(self, actor: Actor, network_id: uuid.UUID, limit: int) -> list[SyncRunOut]:
        """As sincronizações recentes de uma network."""
        runs = list_sync_runs(
            self._uows.uow(actor.company_id), actor=actor, network_id=network_id, limit=limit
        )
        return [SyncRunOut.of(run) for run in runs]

    def disconnect(self, actor: Actor, network_id: uuid.UUID) -> NetworkDetailOut:
        """Desconecta uma network da Empresa."""
        disconnect_network(
            self._uows.uow(actor.company_id),
            actor=actor,
            network_id=network_id,
            clock=self._clock,
        )
        return self.show(actor, network_id)
