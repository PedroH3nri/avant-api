"""Fluxo ponta a ponta: convite de dono, aceite, login, convite de equipe."""

import uuid

from avant_core.company.application import slugify
from avant_core.company.domain import Company, CompanyStatus, Invitation, InvitationKind
from avant_core.company.profile import ClientProfile
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.shared.clock import SystemClock
from avant_core.shared.tokens import new_token
from fastapi.testclient import TestClient
from sqlalchemy import Engine, text

from tests.conftest import FINANCE, CapturingMailer

PASSWORD = "senha-forte-123"


def _owner_invite(
    engine: Engine, mailer: CapturingMailer, email: str, name: str = "Açaí Sites"
) -> str:
    """A Groone cadastra o cliente pendente e manda o convite de dono; devolve o token."""
    staff = uuid.uuid4()
    with engine.begin() as conn:
        conn.execute(
            text(
                "INSERT INTO users (id, email, name, locale, status)"
                " VALUES (:id, :e, 'Staff', 'pt', 'active')"
            ),
            {"id": staff, "e": f"staff-{staff}@groone.com"},
        )
    token, token_hash = new_token()
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        # Entidade criada depois do Unit of Work, que liga as dataclasses às tabelas.
        company = Company(
            name=name,
            owner_user_id=None,
            seat_limit=3,
            slug=slugify(name),
            status=CompanyStatus.PENDING,
        )
        uow.companies.add(company)
        uow.client_profiles.add(ClientProfile(company.id, "Dono", name, email))
        uow.invitations.add(
            Invitation.for_owner(
                company_id=company.id,
                email=email,
                token_hash=token_hash,
                invited_by=staff,
                now=SystemClock().now(),
            )
        )
        uow.commit()
    mailer.send_invitation(
        to=email, token=token, kind=InvitationKind.OWNER, company_name=name, locale="pt"
    )
    return mailer.sent[-1].token


def _csrf(client: TestClient) -> dict[str, str]:
    return {"X-CSRF-Token": client.cookies["avant_csrf"]}


def _onboard_owner(client: TestClient, engine: Engine, mailer: CapturingMailer) -> dict:  # type: ignore[type-arg]
    token = _owner_invite(engine, mailer, "dono@acai.com")
    preview = client.get(f"/api/v1/auth/invitations/{token}")
    assert preview.status_code == 200
    assert preview.json()["kind"] == "owner" and preview.json()["account_exists"] is False
    r = client.post(
        f"/api/v1/auth/invitations/{token}/accept",
        json={"name": "Dono", "password": PASSWORD},
    )
    assert r.status_code == 200, r.text
    return r.json()  # type: ignore[no-any-return]


def test_health_and_metrics(client: TestClient) -> None:
    assert client.get("/api/v1/health").json() == {"status": "ok"}
    assert client.get("/api/v1/ready").json()["checks"] == {"database": "ok"}
    body = client.get("/api/v1/metrics").text
    assert "avant_http_requests_total" in body
    assert 'route="/api/v1/health"' in body


def test_owner_onboarding_and_login(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    assert me["user"]["email"] == "dono@acai.com"
    assert me["companies"][0]["slug"] == "acai-sites"
    assert me["companies"][0]["is_owner"] is True
    assert me["companies"][0]["is_internal"] is False
    assert me["permissions"] == ["*"] and me["site_scope"] == "all"
    assert client.cookies.get("avant_session")

    assert client.post("/api/v1/auth/logout", headers=_csrf(client)).status_code == 204
    assert client.get("/api/v1/auth/me").status_code == 401

    bad = client.post("/api/v1/auth/login", json={"email": "dono@acai.com", "password": "x"})
    assert bad.status_code == 401
    assert bad.json()["error"]["code"] == "invalid_credentials"
    ok = client.post("/api/v1/auth/login", json={"email": "DONO@acai.com", "password": PASSWORD})
    assert ok.status_code == 200 and ok.json()["mfa_required"] is False
    assert client.get("/api/v1/auth/me").json()["active_company_id"] == me["active_company_id"]


def test_csrf_is_required_for_writes(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    r = client.post("/api/v1/invitations", json={"email": "ana@acai.com", "role_id": str(FINANCE)})
    assert r.status_code == 403
    assert r.json()["error"]["code"] == "csrf_failed"


def test_team_invitation_flow(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    body = {"email": "ana@acai.com", "role_id": str(FINANCE)}
    r = client.post("/api/v1/invitations", json=body, headers=_csrf(client))
    assert r.status_code == 201, r.text
    dup = client.post("/api/v1/invitations", json=body, headers=_csrf(client))
    assert dup.status_code == 409 and dup.json()["error"]["code"] == "already_member"
    pending = client.get("/api/v1/invitations").json()["items"]
    assert [i["email"] for i in pending] == ["ana@acai.com"]

    # Ana abre o link num navegador sem sessão.
    token = mailer.sent[-1].token
    client.cookies.clear()
    preview = client.get(f"/api/v1/auth/invitations/{token}").json()
    assert preview["company_name"] == "Açaí Sites"
    assert preview["role_name"]["pt"] == "Financeiro"
    weak = client.post(
        f"/api/v1/auth/invitations/{token}/accept", json={"name": "Ana", "password": "curta"}
    )
    assert weak.status_code == 422 and weak.json()["error"]["code"] == "weak_password"
    me = client.post(
        f"/api/v1/auth/invitations/{token}/accept", json={"name": "Ana", "password": PASSWORD}
    ).json()
    assert me["permissions"] == [
        "costs.manage",
        "costs.view",
        "network.view",
        "reports.view",
        "results.view",
        "sites.view",
    ]
    assert me["site_scope"] == "assigned"

    # O papel financeiro não convida nem vê a equipe.
    r = client.post(
        "/api/v1/invitations",
        json={"email": "x@acai.com", "role_id": str(FINANCE)},
        headers=_csrf(client),
    )
    assert r.status_code == 403 and r.json()["error"]["code"] == "permission_denied"


def test_seat_limit(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)  # 3 vagas, o dono ocupa uma
    codes = [
        client.post(
            "/api/v1/invitations",
            json={"email": f"p{i}@acai.com", "role_id": str(FINANCE)},
            headers=_csrf(client),
        ).status_code
        for i in range(3)
    ]
    assert codes == [201, 201, 409]


def test_validation_error_format(client: TestClient) -> None:
    r = client.post("/api/v1/auth/login", json={"email": "não é e-mail"})
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validation_error"
    assert client.get("/api/v1/nada").json()["error"]["code"] == "not_found"
