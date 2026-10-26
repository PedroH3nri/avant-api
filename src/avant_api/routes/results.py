"""Resultado da Empresa ativa mês a mês: /api/v1/results (``results.view``).

O resultado de todas as Empresas cliente fica no painel interno (``/internal/results``).
Sem período, vêm os seis meses até o atual; sem moeda, o dólar.
"""

from datetime import date

from avant_core.company.application import Actor
from avant_core.money.domain import BASE_CURRENCY
from avant_core.results.application import company_results
from fastapi import APIRouter, Depends, Query

from avant_api.deps import get_services, require
from avant_api.schemas import ResultsOut
from avant_api.services import Services

router = APIRouter(tags=["results"])

DEFAULT_MONTHS = 6


@router.get("/results")
def show(
    start: date | None = None,
    end: date | None = None,
    currency: str = Query(default=BASE_CURRENCY, min_length=3, max_length=3),
    actor: Actor = Depends(require("results.view")),
    services: Services = Depends(get_services),
) -> ResultsOut:
    """Faturamento, deduções, receita, custos e resultado de cada mês do período."""
    first, last = default_period(start, end, services.clock.now().date())
    results = company_results(
        services.uow(actor.company_id),
        actor=actor,
        start=first,
        end=last,
        currency=currency,
        clock=services.clock,
    )
    return ResultsOut.of(results)


def default_period(start: date | None, end: date | None, today: date) -> tuple[date, date]:
    """O período pedido, ou os ``DEFAULT_MONTHS`` meses até o atual."""
    last = end or today
    if start is not None:
        return start, last
    index = last.year * 12 + last.month - DEFAULT_MONTHS
    return date(index // 12, index % 12 + 1, 1), last
