"""Service das networks do MCM sem dono no painel interno."""

import uuid

from avant_core.company.application import Actor
from avant_core.gam.application import assign_mcm_candidate, list_mcm_candidates
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.tasks import TaskQueue
from avant_api.modules.internal.mcm.dto import McmCandidateOut
from avant_api.modules.networks.dto import NetworkOut
from avant_api.modules.networks.service import enqueue_sync


class McmService:
    """Liga networks aprovadas no MCM às Empresas certas."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, tasks: TaskQueue) -> None:
        self._uows = uows
        self._clock = clock
        self._tasks = tasks

    def unassigned(self, actor: Actor) -> list[McmCandidateOut]:
        """Networks MCM aprovadas cujo e-mail não é dono de nenhuma Empresa."""
        candidates = list_mcm_candidates(self._uows.trusted_uow(), actor=actor)
        return [McmCandidateOut.of(candidate) for candidate in candidates]

    def assign(self, actor: Actor, candidate_id: uuid.UUID, company_id: uuid.UUID) -> NetworkOut:
        """Liga a network a uma Empresa e agenda a primeira sincronização."""
        network = assign_mcm_candidate(
            self._uows.trusted_uow(),
            actor=actor,
            candidate_id=candidate_id,
            company_id=company_id,
            clock=self._clock,
        )
        enqueue_sync(self._tasks, network)
        return NetworkOut.of(network)
