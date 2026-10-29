"""Resultado dos clientes: /api/v1/internal/results."""

from datetime import date

from avant_core.access.models import Actor
from avant_core.money.catalog import BASE_CURRENCY
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require_staff
from avant_api.modules.internal.results.dependencies import client_result_service
from avant_api.modules.internal.results.service import ClientResultService
from avant_api.modules.results.dto import ResultsOut
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/results")
def results(
    start: date | None = None,
    end: date | None = None,
    currency: str = Query(default=BASE_CURRENCY, min_length=3, max_length=3),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.results.view")),
    service: ClientResultService = Depends(client_result_service),
) -> PageOut[ResultsOut]:
    """Uma página do ranking das Empresas cliente pelo resultado do período, o maior primeiro."""
    return service.list_all(actor, start, end, currency, page)
