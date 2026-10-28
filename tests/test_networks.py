"""Networks do GAM contra o Postgres. O worker não roda aqui: conferimos o que a rota
enfileira e o estado que ela grava."""

from datetime import UTC, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.mcm.models import McmCandidate
from avant_core.gam.networks.enums import Delegation
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.tasks import SYNC_NETWORK, RecordingQueue
from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner, _owner_invite
from tests.test_internal import _staff
from tests.test_team import _member_client


def _queue(client: TestClient) -> RecordingQueue:
    queue = client.app.state.services.tasks  # type: ignore[attr-defined]
    assert isinstance(queue, RecordingQueue)
    return queue


def _second_owner(client: TestClient, engine: Engine, mailer: CapturingMailer) -> TestClient:
    token = _owner_invite(engine, mailer, "dono@outra.com", "Outra")
    other = TestClient(client.app)
    r = other.post(
        f"/api/v1/auth/invitations/{token}/accept",
        json={"name": "Outro", "password": PASSWORD},
    )
    assert r.status_code == 200, r.text
    return other


def test_connect_sync_and_disconnect(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = me["active_company_id"]
    assert client.get("/api/v1/networks").json() == {"items": [], "next_cursor": None}
    guide = client.get("/api/v1/networks/service-account").json()
    assert guide["email"].endswith(".iam.gserviceaccount.com") and guide["role"] == "Administrator"

    bad = client.post("/api/v1/networks", json={"network_code": "abc"}, headers=_csrf(client))
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_input"

    r = client.post("/api/v1/networks", json={"network_code": " 123 "}, headers=_csrf(client))
    assert r.status_code == 202, r.text
    network = r.json()
    assert network["network_code"] == "123" and network["status"] == "pending"
    assert network["connection_type"] == "service_account" and network["sites"] == 0
    assert _queue(client).sent == [(SYNC_NETWORK, (company_id, network["id"]))]

    # Conectar de novo a mesma network não duplica.
    again = client.post("/api/v1/networks", json={"network_code": "123"}, headers=_csrf(client))
    assert again.status_code == 202 and again.json()["id"] == network["id"]

    url = f"/api/v1/networks/{network['id']}"
    assert client.get(url).json()["last_runs"] == {}
    assert client.get(f"{url}/sync-runs").json()["items"] == []

    assert client.post(f"{url}/sync", headers=_csrf(client)).status_code == 202
    too_soon = client.post(f"{url}/sync", headers=_csrf(client))
    assert too_soon.status_code == 429
    assert too_soon.json()["error"]["code"] == "sync_too_soon"
    assert 0 < int(too_soon.headers["Retry-After"]) <= 600

    r = client.post(f"{url}/disconnect", headers=_csrf(client))
    assert r.status_code == 200 and r.json()["status"] == "disconnected"
    r = client.post(f"{url}/sync", headers=_csrf(client))
    assert r.status_code == 409 and r.json()["error"]["code"] == "network_disconnected"
    assert len(_queue(client).sent) == 3


def test_networks_are_isolated_per_company(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    network = client.post(
        "/api/v1/networks", json={"network_code": "123"}, headers=_csrf(client)
    ).json()

    other = _second_owner(client, engine, mailer)
    assert other.get("/api/v1/networks").json()["items"] == []
    assert other.get(f"/api/v1/networks/{network['id']}").status_code == 404
    taken = other.post("/api/v1/networks", json={"network_code": "123"}, headers=_csrf(other))
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "network_code_taken"


def test_networks_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")  # Financeiro: só network.view
    assert ana.get("/api/v1/networks").status_code == 200
    for method, path in (
        ("get", "/api/v1/networks/service-account"),
        ("post", "/api/v1/networks"),
    ):
        r = ana.request(method, path, json={"network_code": "1"}, headers=_csrf(ana))
        assert r.status_code == 403 and r.json()["error"]["code"] == "permission_denied"
    assert TestClient(client.app).get("/api/v1/networks").status_code == 401


def test_internal_assigns_unowned_mcm_network(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = me["active_company_id"]
    now = datetime.now(UTC)
    candidate = McmCandidate(
        network_code="456",
        email="outro-email@acai.com",
        account_status="APPROVED",
        first_seen_at=now,
        last_seen_at=now,
        display_name="Açaí",
        delegation=Delegation.MANAGE_ACCOUNT,
    )
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        uow.mcm_candidates.add(candidate)
        uow.commit()

    # Dono de Empresa cliente não enxerga o painel.
    assert client.get("/api/v1/internal/networks/unassigned").status_code == 403

    staff = _staff(client, engine)
    (item,) = staff.get("/api/v1/internal/networks/unassigned").json()["items"]
    assert item["network_code"] == "456" and item["delegation"] == "manage_account"
    r = staff.post(
        f"/api/v1/internal/networks/{item['id']}/assign",
        json={"company_id": company_id},
        headers=_csrf(staff),
    )
    assert r.status_code == 202, r.text
    assert r.json()["connection_type"] == "mcm" and r.json()["status"] == "pending"
    assert _queue(client).sent[-1] == (SYNC_NETWORK, (company_id, r.json()["id"]))
    assert staff.get("/api/v1/internal/networks/unassigned").json()["items"] == []
    (owned,) = client.get("/api/v1/networks").json()["items"]
    assert owned["network_code"] == "456"
