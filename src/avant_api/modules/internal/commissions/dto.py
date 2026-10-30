"""Formatos da comissão da equipe Groone: regras, data de início, meses, prazos e desconto.

Dinheiro sai em dólar como texto com duas casas (a comissão é paga só em dólar).
"""

import uuid
from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from typing import Annotated

from avant_core.commissions.enums import CommissionEvent, CommissionStatus
from avant_core.commissions.models import (
    CommissionMonth,
    CommissionRule,
    MyCommissions,
    PersonMonth,
    WindowMonth,
)
from avant_core.commissions.services import RuleInput
from pydantic import BaseModel, Field

from avant_api.shared.dto import UserOut

MICROS = Decimal(1_000_000)
CENT = Decimal("0.01")
MONTH_PATTERN = r"^20\d{2}-(0[1-9]|1[0-2])$"


def dollars(micros: int) -> Decimal:
    """Micros de dólar em dólares com duas casas."""
    return (Decimal(micros) / MICROS).quantize(CENT, rounding=ROUND_HALF_UP)


class CommissionRuleIn(BaseModel):
    event: CommissionEvent
    percentage: Annotated[Decimal, Field(gt=0, le=100, decimal_places=2)]
    start_offset_days: int = Field(default=0, ge=0, le=365)
    # Vazio: sem prazo.
    duration_days: int | None = Field(default=None, ge=1, le=3650)
    # Só nos eventos de cliente, com prazo: o papel para onde o cliente vai no fim.
    transfer_to_role_id: uuid.UUID | None = None

    def input(self) -> RuleInput:
        """Os dados para o caso de uso do core."""
        return RuleInput(
            self.event,
            self.percentage,
            self.start_offset_days,
            self.duration_days,
            self.transfer_to_role_id,
        )


class CommissionRuleOut(BaseModel):
    id: uuid.UUID
    role_id: uuid.UUID
    event: CommissionEvent
    percentage: Decimal
    start_offset_days: int
    duration_days: int | None
    transfer_to_role_id: uuid.UUID | None

    @classmethod
    def of(cls, rule: CommissionRule) -> "CommissionRuleOut":
        """Monta a regra com o percentual em duas casas."""
        return cls(
            id=rule.id,
            role_id=rule.role_id,
            event=rule.event,
            percentage=rule.percentage.quantize(CENT),
            start_offset_days=rule.start_offset_days,
            duration_days=rule.duration_days,
            transfer_to_role_id=rule.transfer_to_role_id,
        )


class CommissionSettingsIn(BaseModel):
    # O dia seguinte ao último pago pelo Genius.
    starts_on: date


class CommissionSettingsOut(BaseModel):
    starts_on: date | None


class MonthIn(BaseModel):
    month: str = Field(pattern=MONTH_PATTERN)

    def first_day(self) -> date:
        """O primeiro dia do mês pedido."""
        year, number = self.month.split("-")
        return date(int(year), int(number), 1)


class AdjustmentIn(MonthIn):
    amount: Annotated[Decimal, Field(gt=0, max_digits=12, decimal_places=2)]
    reason: str = Field(min_length=1, max_length=500)


class CommissionMonthOut(BaseModel):
    month: date
    base: Decimal
    commission: Decimal
    deduction: Decimal
    adjustments: Decimal
    total: Decimal
    status: CommissionStatus

    @classmethod
    def of(cls, month: CommissionMonth) -> "CommissionMonthOut":
        """Monta os totais do mês em dólares."""
        return cls(
            month=month.month,
            base=dollars(month.base_micros),
            commission=dollars(month.commission_micros),
            deduction=dollars(month.deduction_micros),
            adjustments=dollars(month.adjustment_micros),
            total=dollars(month.total_micros),
            status=month.status,
        )


class WindowMonthOut(BaseModel):
    id: uuid.UUID
    event: CommissionEvent
    target_name: str
    company_id: uuid.UUID
    network_id: uuid.UUID | None
    site_id: uuid.UUID | None
    event_on: date
    starts_on: date | None
    ends_on: date | None
    stopped_on: date | None
    percentage: Decimal | None
    base: Decimal
    commission: Decimal
    deduction: Decimal

    @classmethod
    def of(cls, item: WindowMonth) -> "WindowMonthOut":
        """Monta o prazo com o que gerou no mês."""
        window = item.window
        return cls(
            id=window.id,
            event=window.event,
            target_name=item.target_name,
            company_id=window.company_id,
            network_id=window.network_id,
            site_id=window.site_id,
            event_on=window.event_on,
            starts_on=window.starts_on,
            ends_on=item.ends_on,
            stopped_on=window.stopped_on,
            percentage=item.percentage.quantize(CENT) if item.percentage is not None else None,
            base=dollars(item.base_micros),
            commission=dollars(item.commission_micros),
            deduction=dollars(item.deduction_micros),
        )


class MyCommissionsOut(BaseModel):
    windows: list[WindowMonthOut]
    month: CommissionMonthOut
    history: list[CommissionMonthOut]

    @classmethod
    def of(cls, mine: MyCommissions) -> "MyCommissionsOut":
        """Monta a tela Minha comissão."""
        return cls(
            windows=[WindowMonthOut.of(item) for item in mine.windows],
            month=CommissionMonthOut.of(mine.month),
            history=[CommissionMonthOut.of(item) for item in mine.history],
        )


class PersonMonthOut(BaseModel):
    user: UserOut
    role_name: str | None
    month: CommissionMonthOut

    @classmethod
    def of(cls, person: PersonMonth) -> "PersonMonthOut":
        """Monta a pessoa com os totais do mês."""
        return cls(
            user=UserOut.of(person.user),
            role_name=person.role_name,
            month=CommissionMonthOut.of(person.month),
        )
