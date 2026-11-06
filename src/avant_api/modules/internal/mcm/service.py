"""Service das networks no painel interno: o cadastro pela equipe e as do MCM sem cadastro."""

import uuid

from avant_core.access.models import Actor
from avant_core.gam.mcm.services import page_mcm_candidates
from avant_core.gam.networks.services import (
    confirm_client_network,
    register_client_network,
    reject_client_network,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import TaskQueue
from avant_api.modules.internal.mcm.dto import McmCandidateOut
from avant_api.modules.networks.dto import NetworkOut
from avant_api.modules.networks.service import enqueue_sync
from avant_api.shared.dto import PageOut, page_out


class McmService:
    """Cadastra networks dos clientes e lista as do MCM sem cadastro."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, tasks: TaskQueue) -> None:
        self._uows = uows
        self._clock = clock
        self._tasks = tasks

    def unassigned(self, actor: Actor, page: int) -> PageOut[McmCandidateOut]:
        """Uma página das networks do MCM sem cadastro, a vista primeiro por último antes."""
        found = page_mcm_candidates(self._uows.trusted_uow(), actor=actor, page=page)
        return page_out(found, McmCandidateOut.of)

    def register(self, actor: Actor, company_id: uuid.UUID, network_code: str) -> NetworkOut:
        """Cadastra a network pendente do cliente e agenda o teste no worker."""
        network = register_client_network(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            network_code=network_code,
            clock=self._clock,
        )
        enqueue_sync(self._tasks, network)
        return NetworkOut.of(network)

    def confirm(self, actor: Actor, network_id: uuid.UUID) -> NetworkOut:
        """Confirma a network do MCM cadastrada pelo cliente e agenda o teste no worker só
        quando ela ainda esperava: o clique repetido não enfileira outro teste."""
        was_awaiting = self._awaiting(network_id)
        network = confirm_client_network(
            self._uows.trusted_uow(), actor=actor, network_id=network_id, clock=self._clock
        )
        if was_awaiting:
            enqueue_sync(self._tasks, network)
        return NetworkOut.of(network)

    def _awaiting(self, network_id: uuid.UUID) -> bool:
        """Diz se a network ainda espera a confirmação da equipe Groone."""
        with self._uows.trusted_uow() as uow:
            network = uow.networks.get(network_id)
            return network is not None and network.awaiting_confirmation

    def reject(self, actor: Actor, network_id: uuid.UUID) -> None:
        """Recusa a network do MCM cadastrada pelo cliente que não é dele."""
        reject_client_network(
            self._uows.trusted_uow(), actor=actor, network_id=network_id, clock=self._clock
        )
