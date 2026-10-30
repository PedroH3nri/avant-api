"""Service das invoices da equipe Groone: chama os casos de uso do avant-core e devolve os DTOs.

As invoices, o catálogo e os dados de recebimento só existem para a Company Groone (RLS só com
o bypass, como a comissão), então tudo usa o Unit of Work sem RLS; o core confere a Company
Groone, a dona da invoice e as permissões.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.invoices.enums import InvoiceStatus
from avant_core.invoices.services import (
    add_service_item,
    all_invoices,
    available_months,
    confirm_payment,
    create_invoice,
    create_service,
    delete_draft,
    delete_service,
    get_invoice,
    get_my_payee_details,
    issue_invoice,
    my_invoices,
    page_services,
    remove_service_item,
    return_to_draft,
    service_options,
    update_my_payee_details,
    update_service,
    update_service_item,
)
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.company.dto import FiscalDataIn
from avant_api.modules.internal.invoices.dto import (
    AvailableMonthOut,
    InvoiceOut,
    InvoiceServiceIn,
    InvoiceServiceOptionOut,
    InvoiceServiceOut,
    InvoiceSummaryOut,
    PayeeDetailsOut,
    ServiceItemIn,
)
from avant_api.modules.internal.invoices.invoice_pdf import render_invoice
from avant_api.shared.dto import PageOut, page_out


class InvoiceService:
    """Dados de recebimento, catálogo de serviços e o ciclo da invoice até o pagamento."""

    def __init__(self, uows: UnitOfWorkFactory, mailer: Mailer, clock: Clock) -> None:
        self._uows = uows
        self._mailer = mailer
        self._clock = clock

    def payee_details(self, actor: Actor) -> PayeeDetailsOut | None:
        """Os dados de recebimento de quem pede, ou nada se ainda não preencheu."""
        found = get_my_payee_details(self._uows.trusted_uow(), actor=actor)
        return PayeeDetailsOut.of_details(found) if found else None

    def save_payee_details(self, actor: Actor, body: FiscalDataIn) -> PayeeDetailsOut:
        """Grava os dados de recebimento de quem pede."""
        saved = update_my_payee_details(
            self._uows.trusted_uow(), actor=actor, data=body.to_data(), clock=self._clock
        )
        return PayeeDetailsOut.of_details(saved)

    def services(self, actor: Actor, page: int) -> PageOut[InvoiceServiceOut]:
        """Uma página do catálogo de serviços."""
        found = page_services(self._uows.trusted_uow(), actor=actor, page=page)
        return page_out(found, InvoiceServiceOut.of)

    def service_options(self, actor: Actor) -> list[InvoiceServiceOptionOut]:
        """Todos os serviços, leves, para o seletor da linha."""
        found = service_options(self._uows.trusted_uow(), actor=actor)
        return [
            InvoiceServiceOptionOut(id=item.id, title=item.title, description=item.description)
            for item in found
        ]

    def create_service(self, actor: Actor, body: InvoiceServiceIn) -> InvoiceServiceOut:
        """Cria um serviço no catálogo."""
        created = create_service(
            self._uows.trusted_uow(),
            actor=actor,
            title=body.title,
            description=body.description,
            clock=self._clock,
        )
        return InvoiceServiceOut.of(created)

    def update_service(
        self, actor: Actor, service_id: uuid.UUID, body: InvoiceServiceIn
    ) -> InvoiceServiceOut:
        """Muda um serviço; as invoices que já o usam não mudam."""
        updated = update_service(
            self._uows.trusted_uow(),
            actor=actor,
            service_id=service_id,
            title=body.title,
            description=body.description,
            clock=self._clock,
        )
        return InvoiceServiceOut.of(updated)

    def delete_service(self, actor: Actor, service_id: uuid.UUID) -> None:
        """Exclui um serviço do catálogo; as linhas guardam a própria cópia."""
        delete_service(
            self._uows.trusted_uow(), actor=actor, service_id=service_id, clock=self._clock
        )

    def available_months(self, actor: Actor) -> list[AvailableMonthOut]:
        """Os meses de quem pede com a comissão validada e ainda sem invoice."""
        found = available_months(self._uows.trusted_uow(), actor=actor)
        return [AvailableMonthOut.of(month) for month in found]

    def mine(self, actor: Actor, page: int) -> PageOut[InvoiceSummaryOut]:
        """As invoices de quem pede, da mais nova."""
        found = my_invoices(self._uows.trusted_uow(), actor=actor, page=page)
        return page_out(found, InvoiceSummaryOut.of)

    def all(
        self,
        actor: Actor,
        page: int,
        status: InvoiceStatus | None,
        month: date | None,
        user_id: uuid.UUID | None,
    ) -> PageOut[InvoiceSummaryOut]:
        """As invoices da equipe, com os filtros do financeiro."""
        found = all_invoices(
            self._uows.trusted_uow(),
            actor=actor,
            page=page,
            status=status,
            month=month,
            user_id=user_id,
        )
        return page_out(found, InvoiceSummaryOut.of)

    def create(self, actor: Actor, month: date) -> InvoiceOut:
        """Cria a invoice do mês com a comissão validada e devolve ela inteira."""
        created = create_invoice(
            self._uows.trusted_uow(), actor=actor, month=month, clock=self._clock
        )
        return self.get(actor, created.id)

    def get(self, actor: Actor, invoice_id: uuid.UUID) -> InvoiceOut:
        """A invoice inteira, com as linhas e o total."""
        return InvoiceOut.of(
            get_invoice(self._uows.trusted_uow(), actor=actor, invoice_id=invoice_id)
        )

    def pdf(self, actor: Actor, invoice_id: uuid.UUID) -> tuple[str, bytes]:
        """O nome do arquivo e o PDF da invoice."""
        view = get_invoice(self._uows.trusted_uow(), actor=actor, invoice_id=invoice_id)
        return f"{view.invoice.number}.pdf", render_invoice(view)

    def delete(self, actor: Actor, invoice_id: uuid.UUID) -> None:
        """Exclui o rascunho; a comissão do mês volta a validada."""
        delete_draft(
            self._uows.trusted_uow(), actor=actor, invoice_id=invoice_id, clock=self._clock
        )

    def add_item(self, actor: Actor, invoice_id: uuid.UUID, body: ServiceItemIn) -> InvoiceOut:
        """Soma uma linha de serviço ao rascunho."""
        add_service_item(
            self._uows.trusted_uow(),
            actor=actor,
            invoice_id=invoice_id,
            service_id=body.service_id,
            description=body.description,
            amount=body.amount,
            clock=self._clock,
        )
        return self.get(actor, invoice_id)

    def update_item(
        self, actor: Actor, invoice_id: uuid.UUID, item_id: uuid.UUID, body: ServiceItemIn
    ) -> InvoiceOut:
        """Troca o serviço, a descrição ou o valor de uma linha do rascunho."""
        update_service_item(
            self._uows.trusted_uow(),
            actor=actor,
            invoice_id=invoice_id,
            item_id=item_id,
            service_id=body.service_id,
            description=body.description,
            amount=body.amount,
            clock=self._clock,
        )
        return self.get(actor, invoice_id)

    def remove_item(self, actor: Actor, invoice_id: uuid.UUID, item_id: uuid.UUID) -> InvoiceOut:
        """Tira uma linha de serviço do rascunho."""
        remove_service_item(
            self._uows.trusted_uow(),
            actor=actor,
            invoice_id=invoice_id,
            item_id=item_id,
            clock=self._clock,
        )
        return self.get(actor, invoice_id)

    def issue(self, actor: Actor, invoice_id: uuid.UUID) -> InvoiceOut:
        """Emite a invoice com a cópia dos dados de recebimento."""
        issue_invoice(
            self._uows.trusted_uow(), actor=actor, invoice_id=invoice_id, clock=self._clock
        )
        return self.get(actor, invoice_id)

    def return_to_draft(self, actor: Actor, invoice_id: uuid.UUID, reason: str) -> InvoiceOut:
        """Devolve para rascunho com o motivo; a dona recebe um e-mail."""
        return_to_draft(
            self._uows.trusted_uow(),
            actor=actor,
            invoice_id=invoice_id,
            reason=reason,
            mailer=self._mailer,
            clock=self._clock,
        )
        return self.get(actor, invoice_id)

    def pay(self, actor: Actor, invoice_id: uuid.UUID) -> InvoiceOut:
        """Confirma o pagamento; a comissão do mês fica paga."""
        confirm_payment(
            self._uows.trusted_uow(), actor=actor, invoice_id=invoice_id, clock=self._clock
        )
        return self.get(actor, invoice_id)
