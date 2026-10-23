"""Painel interno contra o Postgres: só a equipe Groone com 2FA verificado."""

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity.passwords import Argon2PasswordHasher
from avant_core.internal.bootstrap import bootstrap_groone
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_mfa import _enable


def _staff(client: TestClient, engine: Engine) -> TestClient:
    bootstrap_groone(
        SqlAlchemyUnitOfWork(engine, bypass_rls=True),
        email="admin@groone.com",
        name="Admin",
        password=PASSWORD,
        hasher=Argon2PasswordHasher(),
        clock=SystemClock(),
    )
    staff = TestClient(client.app)
    r = staff.post("/api/v1/auth/login", json={"email": "admin@groone.com", "password": PASSWORD})
    assert r.status_code == 200 and r.json()["me"]["mfa_setup_required"] is True
    # Sem 2FA, nem o painel interno abre.
    assert staff.get("/api/v1/internal/clients").status_code == 403
    _enable(staff)  # a confirmação marca esta sessão como verificada
    return staff


def test_internal_clients(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    staff = _staff(client, engine)
    r = staff.post(
        "/api/v1/internal/clients",
        json={"email": "dono@novo.com", "seat_limit": 2, "plan": "external"},
        headers=_csrf(staff),
    )
    assert r.status_code == 201, r.text
    invitation_id = r.json()["id"]
    assert [
        i["email"] for i in staff.get("/api/v1/internal/owner-invitations").json()["items"]
    ] == ["dono@novo.com"]
    r = staff.post(
        f"/api/v1/internal/owner-invitations/{invitation_id}/resend", headers=_csrf(staff)
    )
    assert r.status_code == 200
    owner = TestClient(client.app)
    accepted = owner.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Dono", "password": PASSWORD, "company": {"name": "Novo Portal"}},
    )
    assert accepted.status_code == 200, accepted.text

    clients = staff.get("/api/v1/internal/clients", params={"q": "portal"}).json()["items"]
    assert [c["name"] for c in clients] == ["Novo Portal"]
    company_id = clients[0]["id"]
    detail = staff.get(f"/api/v1/internal/clients/{company_id}").json()
    assert detail["owner"]["email"] == "dono@novo.com" and len(detail["members"]) == 1

    r = staff.patch(
        f"/api/v1/internal/clients/{company_id}", json={"seat_limit": 5}, headers=_csrf(staff)
    )
    assert r.status_code == 200 and r.json()["seat_limit"] == 5
    assert (
        staff.post(
            f"/api/v1/internal/clients/{company_id}/suspend", headers=_csrf(staff)
        ).status_code
        == 204
    )
    assert owner.get("/api/v1/company").status_code == 403  # suspensa: some para o dono
    staff.post(f"/api/v1/internal/clients/{company_id}/reactivate", headers=_csrf(staff))
    assert owner.get("/api/v1/company").status_code == 200

    actions = [
        e["action"]
        for e in staff.get(f"/api/v1/internal/clients/{company_id}/audit").json()["items"]
    ]
    assert actions[:3] == ["company.reactivated", "company.suspended", "company.updated"]


def test_client_owner_cannot_reach_internal(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    r = client.get("/api/v1/internal/clients")
    assert r.status_code == 403 and r.json()["error"]["code"] == "staff_only"
    assert client.get("/api/v1/internal/users", params={"q": "dono"}).status_code == 403


def test_internal_people_and_staff(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    staff = _staff(client, engine)
    (person,) = staff.get("/api/v1/internal/users", params={"q": "acai"}).json()["items"]
    assert person["companies"][0]["slug"] == "acai-sites"
    user_id = person["user"]["id"]
    assert (
        staff.post(f"/api/v1/internal/users/{user_id}/disable", headers=_csrf(staff)).status_code
        == 204
    )
    assert client.get("/api/v1/auth/me").status_code == 401  # sessões encerradas
    staff.post(f"/api/v1/internal/users/{user_id}/enable", headers=_csrf(staff))
    r = staff.post(f"/api/v1/internal/users/{user_id}/reset-mfa", headers=_csrf(staff))
    assert r.status_code == 204

    members = staff.get("/api/v1/internal/staff").json()["items"]
    assert [m["user"]["email"] for m in members] == ["admin@groone.com"]
    roles = staff.get("/api/v1/roles").json()["items"]
    support = next(x for x in roles if x["key"] == "groone_support")
    r = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "suporte@groone.com", "role_id": support["id"]},
        headers=_csrf(staff),
    )
    assert r.status_code == 201, r.text
