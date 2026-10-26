"""Custos da Empresa (aba Custos): /api/v1/costs.

Ver pede ``costs.view``; criar, editar e apagar pedem ``costs.manage``. A conferência da
fórmula responde a prévia do formulário sem gravar nada.
"""

import uuid

from avant_core.company.application import Actor
from avant_core.costs.application import (
    CostInput,
    create_cost,
    delete_cost,
    list_costs,
    update_cost,
)
from avant_core.costs.formula import parse_formula
from avant_core.shared.errors import InvalidFormula
from fastapi import APIRouter, Depends, status

from avant_api.deps import get_services, require
from avant_api.schemas import CostIn, CostOut, FormulaCheckIn, FormulaCheckOut, ItemsOut
from avant_api.services import Services

router = APIRouter(tags=["costs"])


@router.get("/costs")
def index(
    actor: Actor = Depends(require("costs.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[CostOut]:
    """Custos da Empresa, do mês mais novo para o mais antigo."""
    costs = list_costs(services.uow(actor.company_id), actor=actor)
    return ItemsOut(items=[CostOut.of(cost) for cost in costs])


@router.post("/costs", status_code=status.HTTP_201_CREATED)
def create(
    body: CostIn,
    actor: Actor = Depends(require("costs.manage")),
    services: Services = Depends(get_services),
) -> CostOut:
    """Cadastra um custo."""
    cost = create_cost(
        services.uow(actor.company_id), actor=actor, data=_input(body), clock=services.clock
    )
    return CostOut.of(cost)


@router.put("/costs/{cost_id}")
def update(
    cost_id: uuid.UUID,
    body: CostIn,
    actor: Actor = Depends(require("costs.manage")),
    services: Services = Depends(get_services),
) -> CostOut:
    """Troca todos os campos de um custo."""
    cost = update_cost(
        services.uow(actor.company_id),
        actor=actor,
        cost_id=cost_id,
        data=_input(body),
        clock=services.clock,
    )
    return CostOut.of(cost)


@router.delete("/costs/{cost_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    cost_id: uuid.UUID,
    actor: Actor = Depends(require("costs.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Apaga um custo; a auditoria guarda o que ele era."""
    delete_cost(services.uow(actor.company_id), actor=actor, cost_id=cost_id, clock=services.clock)


@router.post("/costs/formula")
def check_formula(
    body: FormulaCheckIn,
    _: Actor = Depends(require("costs.view")),
) -> FormulaCheckOut:
    """Confere a fórmula e calcula com os valores de exemplo, sem gravar."""
    try:
        formula = parse_formula(body.formula)
    except InvalidFormula as error:
        return FormulaCheckOut(valid=False, error=str(error))
    value = formula.evaluate({"faturamento": body.billing, "receita": body.revenue})
    return FormulaCheckOut(valid=True, value=value, variables=sorted(formula.variables))


def _input(body: CostIn) -> CostInput:
    """O formulário no formato do caso de uso."""
    return CostInput(
        name=body.name,
        kind=body.kind,
        currency=body.currency,
        start_month=body.start_month,
        end_month=body.end_month,
        amount=body.amount,
        formula=body.formula,
    )
