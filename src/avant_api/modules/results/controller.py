"""Resultado da Empresa ativa mês a mês: /api/v1/results (``results.view``).

O resultado de todas as Empresas cliente fica no painel interno (``/internal/results``).
Sem período, vêm os seis meses até o atual; sem moeda, o dólar.
"""

from datetime import date

from avant_core.company.service import Actor
from avant_core.money.model import BASE_CURRENCY
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require
from avant_api.modules.results.dependencies import result_service
from avant_api.modules.results.dto import ResultsOut
from avant_api.modules.results.service import ResultService

router = APIRouter(tags=["results"])


@router.get("/results")
def show(
    start: date | None = None,
    end: date | None = None,
    currency: str = Query(default=BASE_CURRENCY, min_length=3, max_length=3),
    actor: Actor = Depends(require("results.view")),
    service: ResultService = Depends(result_service),
) -> ResultsOut:
    """Faturamento, deduções, receita, custos e resultado de cada mês do período."""
    return service.show(actor, start, end, currency)
