"""Formatos de entrada e saída das invoices da equipe Groone, do catálogo e dos dados de
recebimento. Valores em dólares com duas casas, como na comissão."""

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Annotated

from avant_core.commissions.models import CommissionMonth
from avant_core.invoices.enums import InvoiceItemKind, InvoiceStatus
from avant_core.invoices.models import (
    InvoiceItem,
    InvoiceService,
    InvoiceSummary,
    InvoiceView,
    PayeeDetails,
)
from pydantic import BaseModel, Field

from avant_api.modules.internal.commissions.dto import dollars
from avant_api.shared.dto import FiscalDataOut, UserOut


class PayeeDetailsOut(FiscalDataOut):
    updated_at: datetime

    @classmethod
    def of_details(cls, details: PayeeDetails) -> "PayeeDetailsOut":
        """Os dados de recebimento da própria pessoa."""
        return cls(
            tax_type=details.tax_type,
            tax_id=details.tax_id,
            legal_name=details.legal_name,
            billing_phone_ddi=details.billing_phone_ddi,
            billing_phone=details.billing_phone,
            billing_address=details.billing_address,
            bank_name=details.bank_name,
            swift_code=details.swift_code,
            account_number=details.account_number,
            routing_number=details.routing_number,
            updated_at=details.updated_at,
        )


class InvoiceServiceIn(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=500)


class InvoiceServiceOut(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, service: InvoiceService) -> "InvoiceServiceOut":
        """Um serviço do catálogo."""
        return cls(
            id=service.id,
            title=service.title,
            description=service.description,
            created_at=service.created_at,
            updated_at=service.updated_at,
        )


class InvoiceServiceOptionOut(BaseModel):
    id: uuid.UUID
    title: str
    description: str


class ServiceItemIn(BaseModel):
    service_id: uuid.UUID
    description: str = Field(default="", max_length=500)
    amount: Annotated[Decimal, Field(gt=0, le=1_000_000, max_digits=9, decimal_places=2)]


class ReturnIn(BaseModel):
    reason: str = Field(min_length=1, max_length=500)


class AvailableMonthOut(BaseModel):
    month: date
    commission: Decimal
    deduction: Decimal
    adjustments: Decimal
    total: Decimal

    @classmethod
    def of(cls, month: CommissionMonth) -> "AvailableMonthOut":
        """Um mês com a comissão validada que ainda pode virar invoice."""
        return cls(
            month=month.month,
            commission=dollars(month.commission_micros),
            deduction=dollars(month.deduction_micros),
            adjustments=dollars(month.adjustment_micros),
            total=dollars(month.total_micros),
        )


class InvoiceSummaryOut(BaseModel):
    id: uuid.UUID
    number: str
    month: date
    status: InvoiceStatus
    owner: UserOut
    total: Decimal
    created_at: datetime
    issued_at: datetime | None
    paid_at: datetime | None
    returned: bool

    @classmethod
    def of(cls, summary: InvoiceSummary) -> "InvoiceSummaryOut":
        """Uma invoice na lista, com o total e a dona."""
        invoice = summary.invoice
        return cls(
            id=invoice.id,
            number=invoice.number,
            month=invoice.month,
            status=invoice.status,
            owner=UserOut.of(summary.owner),
            total=dollars(summary.total_micros),
            created_at=invoice.created_at,
            issued_at=invoice.issued_at,
            paid_at=invoice.paid_at,
            returned=invoice.returned_reason is not None,
        )


class InvoiceItemOut(BaseModel):
    id: uuid.UUID
    kind: InvoiceItemKind
    title: str
    description: str
    amount: Decimal
    locked: bool
    service_id: uuid.UUID | None

    @classmethod
    def of(cls, item: InvoiceItem) -> "InvoiceItemOut":
        """Uma linha da invoice, com a cópia do nome e do valor."""
        return cls(
            id=item.id,
            kind=item.kind,
            title=item.title,
            description=item.description,
            amount=dollars(item.amount_micros),
            locked=item.locked,
            service_id=item.service_id,
        )


class ReturnedOut(BaseModel):
    at: datetime
    by: str | None
    reason: str


class InvoiceOut(BaseModel):
    id: uuid.UUID
    number: str
    month: date
    status: InvoiceStatus
    owner: UserOut
    role_name: str | None
    items: list[InvoiceItemOut]
    total: Decimal
    created_at: datetime
    issued_at: datetime | None
    paid_at: datetime | None
    returned: ReturnedOut | None
    # A cópia feita na emissão; vazia em rascunho.
    payee: FiscalDataOut | None

    @classmethod
    def of(cls, view: InvoiceView) -> "InvoiceOut":
        """A invoice inteira para a tela."""
        invoice = view.invoice
        returned = (
            ReturnedOut(
                at=invoice.returned_at,
                by=view.returned_by_name,
                reason=invoice.returned_reason,
            )
            if invoice.returned_at and invoice.returned_reason
            else None
        )
        return cls(
            id=invoice.id,
            number=invoice.number,
            month=invoice.month,
            status=invoice.status,
            owner=UserOut.of(view.owner),
            role_name=view.role_name,
            items=[InvoiceItemOut.of(item) for item in view.items],
            total=dollars(view.total_micros),
            created_at=invoice.created_at,
            issued_at=invoice.issued_at,
            paid_at=invoice.paid_at,
            returned=returned,
            payee=FiscalDataOut(**invoice.payee) if invoice.payee else None,
        )
