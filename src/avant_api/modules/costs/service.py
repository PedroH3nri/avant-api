"""Service dos custos: chama os casos de uso do avant-core e devolve os DTOs."""

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
from avant_core.shared.clock import Clock
from avant_core.shared.errors import InvalidFormula

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.costs.dto import CostIn, CostOut, FormulaCheckIn, FormulaCheckOut


class CostService:
    """Custos da Empresa ativa (aba Custos)."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(self, actor: Actor) -> list[CostOut]:
        """Custos da Empresa, do mês mais novo para o mais antigo."""
        costs = list_costs(self._uows.uow(actor.company_id), actor=actor)
        return [CostOut.of(cost) for cost in costs]

    def create(self, actor: Actor, body: CostIn) -> CostOut:
        """Cadastra um custo."""
        cost = create_cost(
            self._uows.uow(actor.company_id), actor=actor, data=_input(body), clock=self._clock
        )
        return CostOut.of(cost)

    def update(self, actor: Actor, cost_id: uuid.UUID, body: CostIn) -> CostOut:
        """Troca todos os campos de um custo."""
        cost = update_cost(
            self._uows.uow(actor.company_id),
            actor=actor,
            cost_id=cost_id,
            data=_input(body),
            clock=self._clock,
        )
        return CostOut.of(cost)

    def delete(self, actor: Actor, cost_id: uuid.UUID) -> None:
        """Apaga um custo; a auditoria guarda o que ele era."""
        delete_cost(
            self._uows.uow(actor.company_id), actor=actor, cost_id=cost_id, clock=self._clock
        )

    def check_formula(self, body: FormulaCheckIn) -> FormulaCheckOut:
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
