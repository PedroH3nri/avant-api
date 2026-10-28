"""Service do resultado mês a mês da Empresa ativa."""

from datetime import date

from avant_core.access.models import Actor
from avant_core.results.services import company_results
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.results.dto import ResultsOut
from avant_api.modules.results.period import default_period


class ResultService:
    """Faturamento, deduções, receita, custos e resultado de cada mês."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def show(self, actor: Actor, start: date | None, end: date | None, currency: str) -> ResultsOut:
        """O resultado do período pedido, ou dos seis meses até o atual."""
        first, last = default_period(start, end, self._clock.now().date())
        results = company_results(
            self._uows.uow(actor.company_id),
            actor=actor,
            start=first,
            end=last,
            currency=currency,
            clock=self._clock,
        )
        return ResultsOut.of(results)
