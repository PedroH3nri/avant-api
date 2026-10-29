"""Service do resultado de todas as Empresas cliente."""

from datetime import date

from avant_core.access.models import Actor
from avant_core.results.services import page_clients_results
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.results.dto import ResultsOut
from avant_api.modules.results.period import default_period
from avant_api.shared.dto import PageOut, page_out


class ClientResultService:
    """O resultado mês a mês de cada Empresa cliente."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(
        self, actor: Actor, start: date | None, end: date | None, currency: str, page: int
    ) -> PageOut[ResultsOut]:
        """Uma página do ranking das Empresas cliente pelo resultado do período."""
        first, last = default_period(start, end, self._clock.now().date())
        found = page_clients_results(
            self._uows.trusted_uow(),
            actor=actor,
            start=first,
            end=last,
            currency=currency,
            clock=self._clock,
            page=page,
        )
        return page_out(found, ResultsOut.of)
