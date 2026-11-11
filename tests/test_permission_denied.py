"""Rotas de Empresa que recusam com 403 quem não tem a permissão: documentos, networks,
membros, permissões diretas, papéis e custos."""

import uuid
from datetime import UTC, datetime

from fastapi.testclient import TestClient
from httpx import Response
from sqlalchemy import Engine

from avant_api.app.tasks import SYNC_NETWORK, RecordingQueue
from tests.conftest import FINANCE, CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_client_documents import PDF, _manage_inventory
from tests.test_costs_results import _marketing_client
from tests.test_team import _member_client

THIS_MONTH = datetime.now(UTC).date().replace(day=1)


def _queue(client: TestClient) -> RecordingQueue:
    """O fake da fila do worker que a aplicação de teste usa."""
    queue = client.app.state.services.tasks  # type: ignore[attr-defined]
    assert isinstance(queue, RecordingQueue)
    return queue


def _assert_denied(response: Response) -> None:
    """Confere que a resposta é 403 por falta de permissão."""
    assert response.status_code == 403, response.text
    assert response.json()["error"]["code"] == "permission_denied"


def test_documents_need_company_edit(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _manage_inventory(engine, uuid.UUID(me["companies"][0]["id"]))
    finance = _member_client(client, mailer, "ana@acai.com")
    upload_headers = {**_csrf(finance), "Content-Type": "application/octet-stream"}

    _assert_denied(finance.get("/api/v1/company/documents"))
    _assert_denied(
        finance.put(
            "/api/v1/company/documents/identity",
            params={"name": "rg.pdf"},
            content=PDF,
            headers=upload_headers,
        )
    )
    _assert_denied(finance.get("/api/v1/company/documents/identity/file"))
    assert client.get("/api/v1/company/documents").json()["documents"] == []


def test_network_sync_and_disconnect_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    network = client.post(
        "/api/v1/networks", json={"network_code": "123"}, headers=_csrf(client)
    ).json()
    finance = _member_client(client, mailer, "ana@acai.com")
    url = f"/api/v1/networks/{network['id']}"
    syncs_before = [task for task in _queue(client).sent if task[0] == SYNC_NETWORK]
    status_before = client.get(url).json()["status"]

    _assert_denied(finance.post(f"{url}/sync", headers=_csrf(finance)))
    _assert_denied(finance.post(f"{url}/disconnect", headers=_csrf(finance)))
    assert [task for task in _queue(client).sent if task[0] == SYNC_NETWORK] == syncs_before
    assert client.get(url).json()["status"] == status_before != "disconnected"


def test_member_writes_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    finance = _member_client(client, mailer, "ana@acai.com")
    _member_client(client, mailer, "bia@acai.com")
    members = client.get("/api/v1/members").json()["items"]
    bia_id = next(member["id"] for member in members if member["user"]["email"] == "bia@acai.com")
    url = f"/api/v1/members/{bia_id}"
    granted = client.put(
        f"{url}/permissions",
        json={"permissions": [{"permission": "sites.view", "effect": "allow"}]},
        headers=_csrf(client),
    )
    assert granted.status_code == 200, granted.text
    before = client.get(url).json()

    _assert_denied(finance.patch(url, json={"status": "suspended"}, headers=_csrf(finance)))
    _assert_denied(finance.delete(url, headers=_csrf(finance)))
    _assert_denied(
        finance.put(
            f"{url}/permissions",
            json={"permissions": [{"permission": "team.view", "effect": "allow"}]},
            headers=_csrf(finance),
        )
    )
    after = client.get(url).json()
    assert after == before
    assert after["status"] == "active"
    assert after["permissions"] == [
        {"permission": "sites.view", "effect": "allow", "expires_at": None}
    ]
    assert len(client.get("/api/v1/members").json()["items"]) == 3


def test_role_writes_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    role = client.post(
        "/api/v1/roles",
        json={"name": "Analista", "permissions": ["sites.view"]},
        headers=_csrf(client),
    ).json()
    finance = _member_client(client, mailer, "ana@acai.com")
    body = {"name": "Outro", "permissions": ["sites.view"]}
    finance_name = next(
        item["name"]
        for item in client.get("/api/v1/roles").json()["items"]
        if item["id"] == str(FINANCE)
    )

    _assert_denied(finance.post("/api/v1/roles", json=body, headers=_csrf(finance)))
    _assert_denied(
        finance.patch(f"/api/v1/roles/{role['id']}", json={"name": "x"}, headers=_csrf(finance))
    )
    _assert_denied(finance.delete(f"/api/v1/roles/{role['id']}", headers=_csrf(finance)))
    _assert_denied(
        finance.patch(f"/api/v1/roles/{FINANCE}", json={"name": "x"}, headers=_csrf(finance))
    )
    roles = {item["id"]: item for item in client.get("/api/v1/roles").json()["items"]}
    assert "Outro" not in str([item["name"] for item in roles.values()])
    assert roles[role["id"]]["name"]["pt"] == "Analista"
    assert roles[role["id"]]["permissions"] == ["sites.view"]
    assert roles[str(FINANCE)]["name"] == finance_name


def test_cost_writes_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    body = {
        "name": "Servidor",
        "kind": "recurring",
        "currency": "USD",
        "start_month": THIS_MONTH.isoformat(),
        "amount": "100.50",
    }
    cost = client.post("/api/v1/costs", json=body, headers=_csrf(client)).json()
    marketing = _marketing_client(client, mailer)
    url = f"/api/v1/costs/{cost['id']}"

    _assert_denied(marketing.post("/api/v1/costs", json=body, headers=_csrf(marketing)))
    _assert_denied(marketing.put(url, json=body | {"amount": "1"}, headers=_csrf(marketing)))
    _assert_denied(marketing.delete(url, headers=_csrf(marketing)))
    (kept,) = client.get("/api/v1/costs").json()["items"]
    assert kept["amount"] == "100.5"
