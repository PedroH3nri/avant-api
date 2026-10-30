"""Invoices da equipe Groone contra o Postgres: dados de recebimento, catálogo, rascunho,
emissão, devolução com e-mail, pagamento, PDF e permissões."""

import uuid
from datetime import UTC, date, datetime
from decimal import Decimal

from avant_core.commissions.enums import CommissionEvent, CommissionStatus
from avant_core.commissions.models import CommissionWindow, DailyCommission
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.ports import Notice
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_commissions import _support
from tests.test_internal import _staff

MONTH = "2026-09"
PAYEE = {
    "tax_type": "BR_PF",
    "tax_id": "529.982.247-25",
    "legal_name": "Admin Groone",
    "billing_phone_ddi": "55",
    "billing_phone": "11988880000",
    "billing_address": "Rua Exemplo, 200",
    "bank_name": "Banco Exemplo",
    "swift_code": "EXMPBRSP",
    "account_number": "98765-4",
    "routing_number": "0001",
}


def _validated_month(engine: Engine, user_id: str) -> None:
    """Um dia de comissão validado em setembro para a pessoa, num prazo da própria Groone."""
    now = datetime(2026, 10, 15, tzinfo=UTC)
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        groone = uow.companies.internal()
        assert groone is not None
        window = CommissionWindow(
            CommissionEvent.CLIENT_CREATED,
            groone.id,
            date(2026, 9, 1),
            now,
            user_id=uuid.UUID(user_id),
            starts_on=date(2026, 9, 1),
        )
        uow.commission_windows.add(window)
        uow.daily_commissions.add(
            DailyCommission(
                window.id,
                date(2026, 9, 10),
                uuid.UUID(user_id),
                Decimal("5"),
                10_000_000,
                500_000_000,
                CommissionStatus.VALIDATED,
                now,
            )
        )
        uow.commit()


def test_invoice_lifecycle(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    staff = _staff(client, engine)
    me = staff.get("/api/v1/auth/me").json()["user"]["id"]
    _validated_month(engine, me)
    base = "/api/v1/internal"
    assert staff.get(f"{base}/payment-details").json() is None
    company_doc = {**PAYEE, "tax_type": "BR_PJ", "tax_id": "11.222.333/0001-81"}
    refused = staff.put(f"{base}/payment-details", json=company_doc, headers=_csrf(staff))
    assert refused.status_code == 422
    saved = staff.put(f"{base}/payment-details", json=PAYEE, headers=_csrf(staff))
    assert saved.status_code == 200, saved.text
    service = staff.post(
        f"{base}/invoice-services",
        json={"title": "Training", "description": "Client training."},
        headers=_csrf(staff),
    )
    assert service.status_code == 201, service.text
    taken = staff.post(f"{base}/invoice-services", json={"title": "training"}, headers=_csrf(staff))
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "invoice_service_taken"
    options = staff.get(f"{base}/invoice-services/options").json()["items"]
    assert [item["title"] for item in options] == ["Training"]
    months = staff.get(f"{base}/invoices/mine/available-months").json()["items"]
    assert [item["month"] for item in months] == ["2026-09-01"]
    created = staff.post(f"{base}/invoices", json={"month": MONTH}, headers=_csrf(staff))
    assert created.status_code == 201, created.text
    invoice = created.json()
    assert invoice["items"][0]["title"] == "New Client Acquisition Commission"
    assert invoice["items"][0]["locked"] and invoice["total"] == "500.00"
    again = staff.post(f"{base}/invoices", json={"month": MONTH}, headers=_csrf(staff))
    assert again.status_code == 409 and again.json()["error"]["code"] == "invoice_exists"
    url = f"{base}/invoices/{invoice['id']}"
    locked = staff.put(
        f"{url}/items/{invoice['items'][0]['id']}",
        json={"service_id": service.json()["id"], "amount": "1.00"},
        headers=_csrf(staff),
    )
    assert locked.status_code == 409 and locked.json()["error"]["code"] == "item_locked"
    added = staff.post(
        f"{url}/items",
        json={"service_id": service.json()["id"], "description": "20 hours", "amount": "300"},
        headers=_csrf(staff),
    )
    assert added.status_code == 201 and added.json()["total"] == "800.00"
    issued = staff.post(f"{url}/issue", headers=_csrf(staff))
    assert issued.status_code == 200 and issued.json()["status"] == "issued"
    assert issued.json()["payee"]["legal_name"] == "Admin Groone"
    late = staff.delete(url, headers=_csrf(staff))
    assert late.status_code == 409 and late.json()["error"]["code"] == "invoice_not_draft"
    returned = staff.post(
        f"{url}/return", json={"reason": "Training was 2 hours."}, headers=_csrf(staff)
    )
    assert returned.status_code == 200 and returned.json()["status"] == "draft"
    assert returned.json()["returned"]["reason"] == "Training was 2 hours."
    assert returned.json()["returned"]["by"]
    assert mailer.notices[-1][1] == Notice.INVOICE_RETURNED
    staff.post(f"{url}/issue", headers=_csrf(staff))
    paid = staff.post(f"{url}/pay", headers=_csrf(staff))
    assert paid.status_code == 200 and paid.json()["status"] == "paid"
    pdf = staff.get(f"{url}/pdf")
    assert pdf.status_code == 200 and pdf.headers["content-type"] == "application/pdf"
    assert (
        pdf.content.startswith(b"%PDF") and invoice["number"] in pdf.headers["content-disposition"]
    )
    team = staff.get(f"{base}/invoices?status=paid&month={MONTH}").json()
    assert [item["number"] for item in team["items"]] == [invoice["number"]]
    mine = staff.get(f"{base}/invoices/mine").json()
    assert mine["total"] == 1 and mine["items"][0]["total"] == "800.00"
    deleted = staff.delete(f"{base}/invoice-services/{service.json()['id']}", headers=_csrf(staff))
    assert deleted.status_code == 204
    assert staff.get(url).json()["items"][-1]["title"] == "Training"


def test_who_sees_and_changes_invoices(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    me = staff.get("/api/v1/auth/me").json()["user"]["id"]
    _validated_month(engine, me)
    base = "/api/v1/internal"
    invoice = staff.post(f"{base}/invoices", json={"month": MONTH}, headers=_csrf(staff)).json()
    support = _support(client, staff, mailer)
    assert support.get(f"{base}/invoices").status_code == 403
    assert support.get(f"{base}/invoices/{invoice['id']}").status_code == 404
    assert support.get(f"{base}/invoices/{invoice['id']}/pdf").status_code == 404
    assert support.get(f"{base}/invoices/mine").json()["total"] == 0
    for method, url, body in (
        ("post", f"{base}/invoice-services", {"title": "Other"}),
        ("post", f"{base}/invoices/{invoice['id']}/pay", None),
        ("post", f"{base}/invoices/{invoice['id']}/return", {"reason": "x"}),
    ):
        found = getattr(support, method)(url, json=body, headers=_csrf(support))
        assert found.status_code == 403, (url, found.text)
    stolen = support.post(f"{base}/invoices/{invoice['id']}/issue", headers=_csrf(support))
    assert stolen.status_code == 404
    owner = TestClient(client.app)
    _onboard_owner(owner, engine, mailer)
    assert owner.get(f"{base}/invoices/mine").status_code == 403
    assert owner.get(f"{base}/payment-details").status_code == 403
