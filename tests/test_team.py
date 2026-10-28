"""Rotas de equipe contra o Postgres: Empresa, membros, convites, papéis e histórico."""

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import FINANCE, CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner


def _member_client(owner: TestClient, mailer: CapturingMailer, email: str) -> TestClient:
    """Convida com o papel Financeiro e aceita numa segunda sessão (outro navegador)."""
    r = owner.post(
        "/api/v1/invitations",
        json={"email": email, "role_id": str(FINANCE)},
        headers=_csrf(owner),
    )
    assert r.status_code == 201, r.text
    other = TestClient(owner.app)
    accepted = other.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Ana", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    return other


def test_company_and_members(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")

    company = ana.get("/api/v1/company").json()
    assert company["seats_used"] == 2 and company["seat_limit"] == 3
    denied = ana.patch("/api/v1/company", json={"name": "Outro"}, headers=_csrf(ana))
    assert denied.status_code == 403
    assert denied.json()["error"]["code"] == "permission_denied"
    assert ana.get("/api/v1/members").status_code == 403

    r = client.patch(
        "/api/v1/company",
        json={"name": "Açaí Mídia"},
        headers=_csrf(client),
    )
    assert r.status_code == 200 and r.json()["name"] == "Açaí Mídia"

    members = client.get("/api/v1/members").json()["items"]
    assert [m["user"]["email"] for m in members] == ["dono@acai.com", "ana@acai.com"]
    owner_id, ana_id = members[0]["id"], members[1]["id"]
    assert members[1]["role"]["key"] == "finance"

    r = client.patch(
        f"/api/v1/members/{owner_id}", json={"status": "suspended"}, headers=_csrf(client)
    )
    assert r.status_code == 409 and r.json()["error"]["code"] == "cannot_change_owner"

    r = client.patch(
        f"/api/v1/members/{ana_id}", json={"status": "suspended"}, headers=_csrf(client)
    )
    assert r.status_code == 200 and r.json()["status"] == "suspended"
    # Suspensa, Ana perde a Empresa ativa.
    assert ana.get("/api/v1/company").status_code == 403

    assert client.delete(f"/api/v1/members/{ana_id}", headers=_csrf(client)).status_code == 204
    assert [m["user"]["email"] for m in client.get("/api/v1/members").json()["items"]] == [
        "dono@acai.com"
    ]
    assert client.get("/api/v1/company").json()["seats_used"] == 1


def test_leave_company(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.post("/api/v1/members/me/leave", headers=_csrf(ana)).status_code == 204
    assert ana.get("/api/v1/auth/me").json()["companies"] == []
    r = client.post("/api/v1/members/me/leave", headers=_csrf(client))
    assert r.status_code == 409


def test_resend_and_cancel_invitation(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    inv = client.post(
        "/api/v1/invitations",
        json={"email": "bia@acai.com", "role_id": str(FINANCE)},
        headers=_csrf(client),
    ).json()
    old_token = mailer.sent[-1].token
    r = client.post(f"/api/v1/invitations/{inv['id']}/resend", headers=_csrf(client))
    assert r.status_code == 200 and mailer.sent[-1].token != old_token
    assert client.get(f"/api/v1/auth/invitations/{old_token}").status_code == 404

    assert (
        client.delete(f"/api/v1/invitations/{inv['id']}", headers=_csrf(client)).status_code == 204
    )
    r = client.delete(f"/api/v1/invitations/{inv['id']}", headers=_csrf(client))
    assert r.status_code == 409 and r.json()["error"]["code"] == "invitation_not_pending"
    assert client.get("/api/v1/invitations").json()["items"] == []


def test_roles_and_direct_permissions(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get("/api/v1/roles").status_code == 403

    perms = client.get("/api/v1/permissions").json()["items"]
    assert len(perms) == 25 and perms[0]["name"]["es"]

    r = client.post(
        "/api/v1/roles",
        json={
            "name": "Analista",
            "permissions": ["team.view", "sites.view"],
            "site_scope": "assigned",
        },
        headers=_csrf(client),
    )
    assert r.status_code == 201, r.text
    role = r.json()
    r = client.post(
        "/api/v1/roles",
        json={"name": "Ruim", "permissions": ["internal.clients.view"]},
        headers=_csrf(client),
    )
    assert r.status_code == 422 and r.json()["error"]["code"] == "invalid_permission"
    r = client.patch(f"/api/v1/roles/{FINANCE}", json={"name": "x"}, headers=_csrf(client))
    assert r.status_code == 409 and r.json()["error"]["code"] == "role_not_editable"

    ana_id = client.get("/api/v1/members", params={"q": "ana"}).json()["items"][0]["id"]
    client.patch(f"/api/v1/members/{ana_id}", json={"role_id": role["id"]}, headers=_csrf(client))
    # Com team.view do papel novo, Ana já vê a equipe.
    assert ana.get("/api/v1/members").status_code == 200

    r = client.put(
        f"/api/v1/members/{ana_id}/permissions",
        json={"permissions": [{"permission": "team.view", "effect": "deny"}]},
        headers=_csrf(client),
    )
    assert r.status_code == 200 and r.json()["permissions"][0]["effect"] == "deny"
    assert ana.get("/api/v1/members").status_code == 403

    r = client.delete(f"/api/v1/roles/{role['id']}", headers=_csrf(client))
    assert r.status_code == 409 and r.json()["error"]["code"] == "role_in_use"
    roles = {x["key"]: x["member_count"] for x in client.get("/api/v1/roles").json()["items"]}
    assert roles["analista"] == 1


def test_audit_log(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get("/api/v1/audit").status_code == 403
    first = client.get("/api/v1/audit", params={"limit": 2}).json()
    assert [e["action"] for e in first["items"]] == ["invitation.accepted", "invitation.created"]
    rest = client.get("/api/v1/audit", params={"cursor": first["next_cursor"]}).json()
    assert [e["action"] for e in rest["items"]] == ["company.owner_joined"]
    only = client.get("/api/v1/audit", params={"action": "invitation.created"}).json()
    assert len(only["items"]) == 1
    bad = client.get("/api/v1/audit", params={"cursor": "lixo"})
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_input"


def test_requires_session(client: TestClient) -> None:
    for path in ("/api/v1/company", "/api/v1/members", "/api/v1/roles", "/api/v1/audit"):
        assert client.get(path).status_code == 401
