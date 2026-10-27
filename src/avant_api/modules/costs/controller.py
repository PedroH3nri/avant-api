"""Custos da Empresa (aba Custos): /api/v1/costs.

Ver pede ``costs.view``; criar, editar e apagar pedem ``costs.manage``. A conferência da
fórmula responde a prévia do formulário sem gravar nada.
"""

import uuid

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require
from avant_api.modules.costs.dependencies import cost_service
from avant_api.modules.costs.dto import CostIn, CostOut, FormulaCheckIn, FormulaCheckOut
from avant_api.modules.costs.service import CostService
from avant_api.shared.dto import ItemsOut

router = APIRouter(tags=["costs"])


@router.get("/costs")
def index(
    actor: Actor = Depends(require("costs.view")),
    service: CostService = Depends(cost_service),
) -> ItemsOut[CostOut]:
    """Custos da Empresa, do mês mais novo para o mais antigo."""
    return ItemsOut(items=service.list_all(actor))


@router.post("/costs", status_code=status.HTTP_201_CREATED)
def create(
    body: CostIn,
    actor: Actor = Depends(require("costs.manage")),
    service: CostService = Depends(cost_service),
) -> CostOut:
    """Cadastra um custo."""
    return service.create(actor, body)


@router.put("/costs/{cost_id}")
def update(
    cost_id: uuid.UUID,
    body: CostIn,
    actor: Actor = Depends(require("costs.manage")),
    service: CostService = Depends(cost_service),
) -> CostOut:
    """Troca todos os campos de um custo."""
    return service.update(actor, cost_id, body)


@router.delete("/costs/{cost_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    cost_id: uuid.UUID,
    actor: Actor = Depends(require("costs.manage")),
    service: CostService = Depends(cost_service),
) -> None:
    """Apaga um custo; a auditoria guarda o que ele era."""
    service.delete(actor, cost_id)


@router.post("/costs/formula")
def check_formula(
    body: FormulaCheckIn,
    _: Actor = Depends(require("costs.view")),
    service: CostService = Depends(cost_service),
) -> FormulaCheckOut:
    """Confere a fórmula e calcula com os valores de exemplo, sem gravar."""
    return service.check_formula(body)
