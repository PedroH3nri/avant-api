"""Service do resultado de todas as Empresas cliente."""

from datetime import date

from avant_core.company.service import Actor
from avant_core.results.service import clients_results
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.results.dto import ResultsOut
from avant_api.modules.results.period import default_period


class ClientResultService:
    """O resultado mês a mês de cada Empresa cliente."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(
        self, actor: Actor, start: date | None, end: date | None, currency: str
    ) -> list[ResultsOut]:
        """O resultado de cada Empresa cliente no período, por nome."""
        first, last = default_period(start, end, self._clock.now().date())
        items = clients_results(
            self._uows.trusted_uow(),
            actor=actor,
            start=first,
            end=last,
            currency=currency,
            clock=self._clock,
        )
        return [ResultsOut.of(item) for item in items]
