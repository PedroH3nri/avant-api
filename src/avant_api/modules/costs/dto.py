"""DTOs de entrada e saída do domínio costs. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import date, datetime
from decimal import Decimal

from avant_core.costs.domain import MICROS, Cost, CostKind
from pydantic import BaseModel, Field


class CostIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    kind: CostKind
    currency: str = Field(min_length=3, max_length=3)
    # Qualquer dia do mês vale; o avant-core guarda o primeiro.
    start_month: date
    end_month: date | None = None
    # Valor na moeda do custo (de um mês só e recorrente).
    amount: Decimal | None = Field(default=None, ge=0, max_digits=18, decimal_places=6)
    # Conta sobre ``faturamento`` e ``receita`` do mês (tipo fórmula).
    formula: str | None = Field(default=None, max_length=300)


class CostOut(BaseModel):
    id: uuid.UUID
    name: str
    kind: CostKind
    currency: str
    start_month: date
    end_month: date | None
    amount: Decimal | None
    formula: str | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, cost: Cost) -> "CostOut":
        """Monta o custo com o valor fora de micros."""
        return cls(
            id=cost.id,
            name=cost.name,
            kind=cost.kind,
            currency=cost.currency,
            start_month=cost.start_month,
            end_month=cost.end_month,
            amount=None if cost.amount_micros is None else Decimal(cost.amount_micros) / MICROS,
            formula=cost.formula,
            created_at=cost.created_at,
            updated_at=cost.updated_at,
        )


class FormulaCheckIn(BaseModel):
    formula: str = Field(max_length=300)
    # Valores de exemplo para a prévia do formulário.
    billing: Decimal = Field(default=Decimal(10000), max_digits=18, decimal_places=6)
    revenue: Decimal = Field(default=Decimal(9000), max_digits=18, decimal_places=6)


class FormulaCheckOut(BaseModel):
    valid: bool
    value: Decimal | None = None
    # Onde a fórmula quebrou, em português.
    error: str | None = None
    variables: list[str] = Field(default_factory=list)
