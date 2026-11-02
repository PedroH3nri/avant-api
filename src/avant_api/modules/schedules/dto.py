"""Formatos de entrada e saída dos envios agendados."""

import uuid
from datetime import datetime
from typing import Literal

from avant_core.schedules.models import ScheduleDelivery
from avant_core.schedules.services import ScheduleInput, ScheduleView
from pydantic import BaseModel, Field

from avant_api.shared.dto import PageOut


class ScheduleIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    target: Literal["report", "dashboard"]
    # O relatório salvo ou o dashboard que vai no e-mail; a pessoa precisa vê-lo.
    target_id: uuid.UUID
    frequency: Literal["daily", "weekly", "monthly"]
    # Dia da semana (0 é segunda), só no semanal; dia do mês (1 a 28), só no mensal.
    weekday: int | None = Field(default=None, ge=0, le=6)
    month_day: int | None = Field(default=None, ge=1, le=28)
    # Hora cheia no fuso dado (nome IANA, como America/Sao_Paulo).
    hour: int = Field(ge=0, le=23)
    timezone: str = Field(min_length=1, max_length=64)
    # Quem recebe o e-mail: membros ativos da Empresa.
    recipient_user_ids: list[uuid.UUID] = Field(min_length=1, max_length=20)

    def input(self) -> ScheduleInput:
        """O formulário no formato do caso de uso."""
        return ScheduleInput(
            name=self.name,
            target=self.target,
            target_id=self.target_id,
            frequency=self.frequency,
            hour=self.hour,
            timezone=self.timezone,
            recipient_user_ids=tuple(self.recipient_user_ids),
            weekday=self.weekday,
            month_day=self.month_day,
        )


class SchedulePauseIn(BaseModel):
    paused: bool


class ScheduleDeliveryOut(BaseModel):
    scheduled_for: datetime
    sent_at: datetime
    # Quantos e-mails saíram (quem saiu da Empresa ou não vê relatórios fica de fora).
    recipients: int

    @classmethod
    def of(cls, delivery: ScheduleDelivery) -> "ScheduleDeliveryOut":
        """Monta o último envio que saiu."""
        return cls(
            scheduled_for=delivery.scheduled_for,
            sent_at=delivery.sent_at,
            recipients=delivery.recipients,
        )


class ScheduleOut(BaseModel):
    id: uuid.UUID
    name: str
    target: str
    target_id: uuid.UUID
    # Nome do relatório ou do dashboard (vazio se a pessoa não tem como saber).
    target_name: str | None
    frequency: str
    weekday: int | None
    month_day: int | None
    hour: int
    timezone: str
    recipient_user_ids: list[uuid.UUID]
    paused: bool
    next_run_at: datetime
    last_sent_at: datetime | None
    last_delivery: ScheduleDeliveryOut | None
    owner_user_id: uuid.UUID
    created_by: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
    # A pessoa pode editar, pausar e apagar (é a dona ou tem schedules.manage).
    editable: bool

    @classmethod
    def of(cls, view: ScheduleView) -> "ScheduleOut":
        """Monta o envio com o nome do que ele manda e o último envio."""
        schedule = view.schedule
        return cls(
            id=schedule.id,
            name=schedule.name,
            target=schedule.target.value,
            target_id=schedule.target_id,
            target_name=view.target_name,
            frequency=schedule.frequency.value,
            weekday=schedule.weekday,
            month_day=schedule.month_day,
            hour=schedule.hour,
            timezone=schedule.timezone,
            recipient_user_ids=schedule.recipient_user_ids,
            paused=schedule.paused,
            next_run_at=schedule.next_run_at,
            last_sent_at=schedule.last_sent_at,
            last_delivery=(
                ScheduleDeliveryOut.of(view.last_delivery) if view.last_delivery else None
            ),
            owner_user_id=schedule.owner_user_id,
            created_by=schedule.created_by,
            created_at=schedule.created_at,
            updated_at=schedule.updated_at,
            editable=view.can_edit,
        )


class SchedulePageOut(PageOut[ScheduleOut]):
    """Uma página dos envios que a pessoa vê."""
