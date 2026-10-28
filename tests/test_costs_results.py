"""Aba Custos e resultado mês a mês contra o Postgres, com e sem permissão."""

import uuid
from datetime import UTC, datetime
from decimal import Decimal

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.contracts.models import Contract
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from avant_core.metrics.models import GamCounts, GamDailyMetric, McmEarning
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff

MARKETING = uuid.uuid5(uuid.NAMESPACE_URL, "avant:role:marketing")
NOW = datetime.now(UTC)
THIS_MONTH = NOW.date().replace(day=1)


def _marketing_client(owner: TestClient, mailer: CapturingMailer) -> TestClient:
    """Convida com o papel Marketing (sem custos nem resultado) e aceita em outra sessão."""
    invited = owner.post(
        "/api/v1/invitations",
        json={"email": "mkt@acai.com", "role_id": str(MARKETING)},
        headers=_csrf(owner),
    )
    assert invited.status_code == 201, invited.text
    other = TestClient(owner.app)
    accepted = other.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Bia", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    return other


def _month_of_revenue(engine: Engine, company_id: uuid.UUID) -> None:
    """Uma network MCM com revshare de 20%, US$ 1.000 brutos no mês e US$ 50 de dedução."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "123", ConnectionType.MCM, NOW)
        uow.networks.add(network)
        uow.contracts.add(Contract(company_id, network.id, Decimal("20"), NOW))
        uow.gam_metrics.upsert_daily(
            [
                GamDailyMetric(
                    company_id=company_id,
                    network_id=network.id,
                    date=THIS_MONTH,
                    ad_unit_path="topo",
                    country_code="BR",
                    device="desktop",
                    revenue_micros=1_000_000_000,
                    counts=GamCounts(impressions=1000),
                    synced_at=NOW,
                )
            ]
        )
        uow.mcm_earnings.upsert(
            [
                McmEarning(
                    company_id=company_id,
                    network_id=network.id,
                    month=THIS_MONTH,
                    delegation=None,
                    currency="USD",
                    total_earnings_micros=1_000_000_000,
                    deductions_micros=50_000_000,
                    child_payment_micros=760_000_000,
                    parent_payment_micros=190_000_000,
                    synced_at=NOW,
                )
            ]
        )
        uow.commit()


def test_costs_crud_and_formula_check(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    marketing = _marketing_client(client, mailer)
    assert marketing.get("/api/v1/costs").status_code == 403

    created = client.post(
        "/api/v1/costs",
        json={
            "name": "Servidor",
            "kind": "recurring",
            "currency": "USD",
            "start_month": THIS_MONTH.isoformat(),
            "amount": "100.50",
        },
        headers=_csrf(client),
    )
    assert created.status_code == 201, created.text
    cost = created.json()
    assert cost["amount"] == "100.5" and cost["formula"] is None
    bad = client.post(
        "/api/v1/costs",
        json={
            "name": "Imposto",
            "kind": "formula",
            "currency": "USD",
            "start_month": THIS_MONTH.isoformat(),
            "formula": "lucro * 2",
        },
        headers=_csrf(client),
    )
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_formula"

    updated = client.put(
        f"/api/v1/costs/{cost['id']}",
        json={
            "name": "Imposto",
            "kind": "formula",
            "currency": "USD",
            "start_month": THIS_MONTH.isoformat(),
            "formula": "faturamento * 6%",
        },
        headers=_csrf(client),
    )
    assert updated.status_code == 200, updated.text
    assert updated.json()["amount"] is None
    listed = client.get("/api/v1/costs").json()["items"]
    assert [item["name"] for item in listed] == ["Imposto"]

    check = client.post(
        "/api/v1/costs/formula",
        json={"formula": "max(100; faturamento * 6%)", "billing": "1000"},
        headers=_csrf(client),
    ).json()
    assert check == {"valid": True, "value": "100", "error": None, "variables": ["faturamento"]}
    broken = client.post(
        "/api/v1/costs/formula", json={"formula": "1 +"}, headers=_csrf(client)
    ).json()
    assert broken["valid"] is False and broken["error"]

    gone = client.delete(f"/api/v1/costs/{cost['id']}", headers=_csrf(client))
    assert gone.status_code == 204
    assert client.get("/api/v1/costs").json()["items"] == []


def test_results_for_the_company_and_for_groone(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    _month_of_revenue(engine, company_id)
    client.post(
        "/api/v1/costs",
        json={
            "name": "Imposto",
            "kind": "formula",
            "currency": "USD",
            "start_month": THIS_MONTH.isoformat(),
            "formula": "faturamento * 10%",
        },
        headers=_csrf(client),
    )
    result = client.get("/api/v1/results", params={"start": THIS_MONTH.isoformat()})
    assert result.status_code == 200, result.text
    body = result.json()
    assert body["currency"] == "USD" and len(body["months"]) == 1
    month = body["months"][0]
    assert (month["billing"], month["deductions"], month["revenue"]) == (
        "800.00",
        "40.00",
        "760.00",
    )
    assert (month["costs"], month["result"]) == ("80.00", "680.00")
    assert month["cost_lines"][0]["name"] == "Imposto"
    assert len(client.get("/api/v1/results").json()["months"]) == 6
    wrong = client.get("/api/v1/results", params={"currency": "EUR"})
    assert wrong.status_code == 409

    marketing = _marketing_client(client, mailer)
    assert marketing.get("/api/v1/results").status_code == 403
    assert client.get("/api/v1/internal/results").status_code == 403

    staff = _staff(client, engine)
    clients = staff.get(
        "/api/v1/internal/results", params={"start": THIS_MONTH.isoformat()}
    ).json()["items"]
    assert [(item["company"]["id"], item["totals"]["result"]) for item in clients] == [
        (str(company_id), "680.00")
    ]
