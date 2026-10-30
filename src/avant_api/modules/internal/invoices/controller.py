"""Invoices da equipe Groone: /api/v1/internal/invoices, /invoice-services e /payment-details.

Cada pessoa da equipe vê e muda os próprios dados de recebimento e as próprias invoices (o core
confere a dona). Ver as da equipe pede ``internal.invoices.view`` ou ``.manage``; devolver e
confirmar o pagamento pedem ``internal.invoices.manage``; o catálogo pede
``internal.invoices.services`` para mudar.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.invoices.enums import InvoiceStatus
from avant_core.invoices.services import MANAGE, SERVICES
from fastapi import APIRouter, Depends, Query, Response, status

from avant_api.app.security import require_staff, require_staff_member
from avant_api.modules.company.dto import FiscalDataIn
from avant_api.modules.internal.commissions.dto import MONTH_PATTERN, MonthIn
from avant_api.modules.internal.invoices.dependencies import invoice_service
from avant_api.modules.internal.invoices.dto import (
    AvailableMonthOut,
    InvoiceOut,
    InvoiceServiceIn,
    InvoiceServiceOptionOut,
    InvoiceServiceOut,
    InvoiceSummaryOut,
    PayeeDetailsOut,
    ReturnIn,
    ServiceItemIn,
)
from avant_api.modules.internal.invoices.service import InvoiceService
from avant_api.shared.dto import ItemsOut, PageOut

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/payment-details")
def payment_details(
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> PayeeDetailsOut | None:
    """Os dados de recebimento de quem pede (vazio enquanto não preencheu)."""
    return service.payee_details(actor)


@router.put("/payment-details")
def save_payment_details(
    body: FiscalDataIn,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> PayeeDetailsOut:
    """Grava os dados de recebimento; só documento de pessoa física (422 com outro)."""
    return service.save_payee_details(actor, body)


@router.get("/invoice-services")
def services(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> PageOut[InvoiceServiceOut]:
    """O catálogo de serviços, 10 por página, do mais novo."""
    return service.services(actor, page)


@router.get("/invoice-services/options")
def service_options(
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> ItemsOut[InvoiceServiceOptionOut]:
    """Todos os serviços, leves, para o seletor da linha da invoice."""
    return ItemsOut(items=service.service_options(actor))


@router.post("/invoice-services", status_code=status.HTTP_201_CREATED)
def create_service(
    body: InvoiceServiceIn,
    actor: Actor = Depends(require_staff(SERVICES)),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceServiceOut:
    """Cria um serviço (409 ``invoice_service_taken`` se o nome já existe)."""
    return service.create_service(actor, body)


@router.put("/invoice-services/{service_id}")
def update_service(
    service_id: uuid.UUID,
    body: InvoiceServiceIn,
    actor: Actor = Depends(require_staff(SERVICES)),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceServiceOut:
    """Muda o nome ou a descrição; invoices que já usam o serviço não mudam."""
    return service.update_service(actor, service_id, body)


@router.delete("/invoice-services/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: uuid.UUID,
    actor: Actor = Depends(require_staff(SERVICES)),
    service: InvoiceService = Depends(invoice_service),
) -> None:
    """Exclui o serviço do catálogo; as linhas das invoices guardam a própria cópia."""
    service.delete_service(actor, service_id)


@router.get("/invoices/mine")
def mine(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> PageOut[InvoiceSummaryOut]:
    """As invoices de quem pede, 10 por página, da mais nova."""
    return service.mine(actor, page)


@router.get("/invoices/mine/available-months")
def available_months(
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> ItemsOut[AvailableMonthOut]:
    """Os meses com a comissão toda validada e ainda sem invoice, do mais novo."""
    return ItemsOut(items=service.available_months(actor))


@router.post("/invoices", status_code=status.HTTP_201_CREATED)
def create(
    body: MonthIn,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Cria a invoice do mês de quem pede; a comissão validada entra e passa a emitida
    (409 ``invoice_exists`` ou ``commission_not_validated``)."""
    return service.create(actor, body.first_day())


@router.get("/invoices")
def team(
    page: int = Query(default=1, ge=1),
    invoice_status: InvoiceStatus | None = Query(default=None, alias="status"),
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    user_id: uuid.UUID | None = None,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> PageOut[InvoiceSummaryOut]:
    """As invoices da equipe (``internal.invoices.view`` ou ``.manage``), com filtros."""
    first_day = MonthIn(month=month).first_day() if month else None
    return service.all(actor, page, invoice_status, first_day, user_id)


@router.get("/invoices/{invoice_id}")
def get(
    invoice_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """A invoice inteira; de outra pessoa, só para quem vê as da equipe (senão 404)."""
    return service.get(actor, invoice_id)


@router.get("/invoices/{invoice_id}/pdf", response_class=Response)
def pdf(
    invoice_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> Response:
    """O PDF da invoice, em inglês, para baixar."""
    filename, content = service.pdf(actor, invoice_id)
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return Response(content, media_type="application/pdf", headers=headers)


@router.delete("/invoices/{invoice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    invoice_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> None:
    """Exclui o próprio rascunho (409 ``invoice_not_draft`` depois de emitida)."""
    service.delete(actor, invoice_id)


@router.post("/invoices/{invoice_id}/items", status_code=status.HTTP_201_CREATED)
def add_item(
    invoice_id: uuid.UUID,
    body: ServiceItemIn,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Soma uma linha de serviço ao próprio rascunho, com o valor livre."""
    return service.add_item(actor, invoice_id, body)


@router.put("/invoices/{invoice_id}/items/{item_id}")
def update_item(
    invoice_id: uuid.UUID,
    item_id: uuid.UUID,
    body: ServiceItemIn,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Muda uma linha de serviço (409 ``item_locked`` nas linhas da comissão)."""
    return service.update_item(actor, invoice_id, item_id, body)


@router.delete("/invoices/{invoice_id}/items/{item_id}")
def remove_item(
    invoice_id: uuid.UUID,
    item_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Tira uma linha de serviço do próprio rascunho e devolve a invoice."""
    return service.remove_item(actor, invoice_id, item_id)


@router.post("/invoices/{invoice_id}/issue")
def issue(
    invoice_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Emite o próprio rascunho (409 ``payee_details_missing`` sem os dados de recebimento)."""
    return service.issue(actor, invoice_id)


@router.post("/invoices/{invoice_id}/return")
def return_to_draft(
    invoice_id: uuid.UUID,
    body: ReturnIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Devolve a invoice emitida para rascunho com o motivo; a dona recebe um e-mail."""
    return service.return_to_draft(actor, invoice_id, body.reason)


@router.post("/invoices/{invoice_id}/pay")
def pay(
    invoice_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: InvoiceService = Depends(invoice_service),
) -> InvoiceOut:
    """Confirma o pagamento da invoice emitida (409 ``invoice_not_issued`` fora disso)."""
    return service.pay(actor, invoice_id)
