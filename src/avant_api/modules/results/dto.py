"""DTOs de entrada e saída do domínio results. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import date
from decimal import Decimal

from avant_core.costs.model import CostKind
from avant_core.results.model import CostLine, MonthResult
from avant_core.results.service import CompanyResults, Totals
from pydantic import BaseModel

from avant_api.shared.dto import ContractClientRefOut


class CostLineOut(BaseModel):
    cost_id: uuid.UUID
    name: str
    kind: CostKind
    amount: Decimal

    @classmethod
    def of(cls, line: CostLine) -> "CostLineOut":
        """Monta a linha de um custo no mês."""
        return cls(cost_id=line.cost_id, name=line.name, kind=line.kind, amount=line.amount)


class MonthResultOut(BaseModel):
    month: date
    billing: Decimal
    deductions: Decimal
    revenue: Decimal
    costs: Decimal
    result: Decimal
    # O GAM ainda não fechou o mês (por volta do dia 15 do mês seguinte).
    deductions_pending: bool
    cost_lines: list[CostLineOut]

    @classmethod
    def of(cls, month: MonthResult) -> "MonthResultOut":
        """Monta o resultado de um mês."""
        return cls(
            month=month.month,
            billing=month.billing,
            deductions=month.deductions,
            revenue=month.revenue,
            costs=month.costs,
            result=month.result,
            deductions_pending=month.deductions_pending,
            cost_lines=[CostLineOut.of(line) for line in month.cost_lines],
        )


class ResultTotalsOut(BaseModel):
    billing: Decimal
    deductions: Decimal
    revenue: Decimal
    costs: Decimal
    result: Decimal

    @classmethod
    def of(cls, totals: Totals) -> "ResultTotalsOut":
        """Monta o total do período."""
        return cls(
            billing=totals.billing,
            deductions=totals.deductions,
            revenue=totals.revenue,
            costs=totals.costs,
            result=totals.result,
        )


class ResultsOut(BaseModel):
    company: ContractClientRefOut
    currency: str
    months: list[MonthResultOut]
    totals: ResultTotalsOut

    @classmethod
    def of(cls, results: CompanyResults) -> "ResultsOut":
        """Monta o resultado de uma Empresa no período."""
        return cls(
            company=ContractClientRefOut(id=results.company_id, name=results.company_name),
            currency=results.currency,
            months=[MonthResultOut.of(month) for month in results.months],
            totals=ResultTotalsOut.of(results.totals),
        )
