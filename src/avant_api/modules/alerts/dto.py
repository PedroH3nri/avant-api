"""Formatos de entrada e saída dos alertas de métrica."""

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Any

from avant_core.alerts.models import AlertCheck, AlertEvent
from avant_core.alerts.services import AlertInput, AlertPreview, AlertView
from pydantic import BaseModel, Field

from avant_api.shared.dto import PageOut


class AlertIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    # Consulta, condição, valor e base (com schema_version), conferidos no avant-core.
    definition: dict[str, Any]
    # Quem recebe o e-mail: membros ativos da Empresa.
    recipient_user_ids: list[uuid.UUID] = Field(min_length=1, max_length=20)

    def input(self) -> AlertInput:
        """O formulário no formato do caso de uso."""
        return AlertInput(
            name=self.name,
            definition=self.definition,
            recipient_user_ids=tuple(self.recipient_user_ids),
        )


class AlertPreviewIn(BaseModel):
    definition: dict[str, Any]


class AlertMuteIn(BaseModel):
    # Até quando o alerta fica em silêncio (no máximo 90 dias); vazio tira o silêncio.
    until: datetime | None = None


class AlertEventOut(BaseModel):
    id: uuid.UUID
    # O cliente, network ou site que disparou (vazio para o total), com o nome da época.
    subject: str
    subject_label: str | None
    day: date
    value: Decimal
    baseline: Decimal | None
    fired_at: datetime
    resolved_at: datetime | None
    notified_at: datetime | None

    @classmethod
    def of(cls, event: AlertEvent) -> "AlertEventOut":
        """Monta o disparo."""
        return cls(
            id=event.id,
            subject=event.subject,
            subject_label=event.subject_label,
            day=event.day,
            value=event.value,
            baseline=event.baseline,
            fired_at=event.fired_at,
            resolved_at=event.resolved_at,
            notified_at=event.notified_at,
        )


class AlertOut(BaseModel):
    id: uuid.UUID
    name: str
    definition: dict[str, Any]
    recipient_user_ids: list[uuid.UUID]
    # Moeda dos valores em dinheiro da condição e do e-mail (a de quem criou).
    currency: str
    owner_user_id: uuid.UUID
    created_by: uuid.UUID | None
    created_at: datetime
    updated_at: datetime
    muted_until: datetime | None
    last_checked_at: datetime | None
    # Tem algum disparo que ainda não voltou ao normal.
    firing: bool
    last_event: AlertEventOut | None
    # A pessoa pode editar, silenciar e apagar (é a dona ou tem alerts.manage).
    editable: bool

    @classmethod
    def of(cls, view: AlertView) -> "AlertOut":
        """Monta o alerta com o estado dele."""
        alert = view.alert
        return cls(
            id=alert.id,
            name=alert.name,
            definition=alert.definition,
            recipient_user_ids=alert.recipient_user_ids,
            currency=alert.currency,
            owner_user_id=alert.owner_user_id,
            created_by=alert.created_by,
            created_at=alert.created_at,
            updated_at=alert.updated_at,
            muted_until=alert.muted_until,
            last_checked_at=alert.last_checked_at,
            firing=view.firing,
            last_event=AlertEventOut.of(view.last_event) if view.last_event else None,
            editable=view.can_edit,
        )


class AlertPageOut(PageOut[AlertOut]):
    """Uma página dos alertas que a pessoa vê."""


class AlertCheckOut(BaseModel):
    subject: str
    subject_label: str | None
    day: date
    value: Decimal | None
    baseline: Decimal | None
    # Variação em % contra a base (vazia sem base).
    change: Decimal | None
    firing: bool

    @classmethod
    def of(cls, check: AlertCheck) -> "AlertCheckOut":
        """Monta a conferência de um assunto."""
        return cls(
            subject=check.subject,
            subject_label=check.subject_label,
            day=check.day,
            value=check.value,
            baseline=check.baseline,
            change=check.change,
            firing=check.firing,
        )


class AlertPreviewOut(BaseModel):
    """O que o alerta mostraria se valesse hoje, os que disparam primeiro."""

    checks: list[AlertCheckOut]

    @classmethod
    def of(cls, preview: AlertPreview) -> "AlertPreviewOut":
        """Monta a prévia."""
        return cls(checks=[AlertCheckOut.of(check) for check in preview.checks])
