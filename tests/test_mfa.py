"""2FA pela API: ativar, entrar com código, recuperação e a regra da equipe Groone."""

from avant_core.company.model import Company, Membership
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity import totp
from avant_core.identity.model import CredentialProvider, User, UserCredential
from avant_core.identity.passwords import Argon2PasswordHasher
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner


def _now_code(secret: str) -> str:
    return totp.code_at(secret, totp.step_at(SystemClock().now()))


def _enable(client: TestClient) -> tuple[str, list[str]]:
    setup = client.post("/api/v1/auth/mfa/setup", headers=_csrf(client))
    assert setup.status_code == 200, setup.text
    secret = setup.json()["secret"]
    assert setup.json()["uri"].startswith("otpauth://totp/")
    r = client.post(
        "/api/v1/auth/mfa/confirm", json={"code": _now_code(secret)}, headers=_csrf(client)
    )
    assert r.status_code == 200, r.text
    return secret, r.json()["recovery_codes"]


def test_login_with_mfa(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    _, recovery = _enable(client)
    assert client.get("/api/v1/auth/me").json()["mfa_enabled"] is True
    client.post("/api/v1/auth/logout", headers=_csrf(client))

    r = client.post("/api/v1/auth/login", json={"email": "dono@acai.com", "password": PASSWORD})
    assert r.json() == {"mfa_required": True, "me": None}
    assert client.get("/api/v1/auth/me").status_code == 401  # pré-sessão não abre o painel

    wrong = client.post("/api/v1/auth/mfa/verify", json={"code": "000000"})
    assert wrong.status_code == 422 and wrong.json()["error"]["code"] == "invalid_mfa_code"
    ok = client.post("/api/v1/auth/mfa/verify", json={"code": recovery[0]})
    assert ok.status_code == 200, ok.text
    assert ok.json()["user"]["email"] == "dono@acai.com"
    assert client.get("/api/v1/auth/me").status_code == 200


def test_client_can_disable(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    _, recovery = _enable(client)
    r = client.request(
        "DELETE", "/api/v1/auth/mfa", json={"code": recovery[1]}, headers=_csrf(client)
    )
    assert r.status_code == 204, r.text
    assert client.get("/api/v1/auth/me").json()["mfa_enabled"] is False


def test_staff_must_set_up_mfa_first(client: TestClient, engine: Engine) -> None:
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        staff = User(email="ana@groone.com", name="Ana")
        uow.users.add(staff)
        uow.credentials.add(
            UserCredential(
                user_id=staff.id,
                provider=CredentialProvider.PASSWORD,
                secret_hash=Argon2PasswordHasher().hash(PASSWORD),
            )
        )
        groone = Company(
            name="Groone",
            owner_user_id=staff.id,
            seat_limit=None,
            slug="groone",
            is_internal=True,
        )
        uow.companies.add(groone)
        uow.memberships.add(
            Membership(
                company_id=groone.id, user_id=staff.id, role_id=None, joined_at=SystemClock().now()
            )
        )
        uow.commit()

    me = client.post(
        "/api/v1/auth/login", json={"email": "ana@groone.com", "password": PASSWORD}
    ).json()["me"]
    assert me["is_staff"] and me["mfa_setup_required"]
    blocked = client.get("/api/v1/invitations")
    assert blocked.status_code == 403 and blocked.json()["error"]["code"] == "mfa_required"

    _, recovery = _enable(client)
    assert client.get("/api/v1/invitations").status_code == 200
    r = client.request(
        "DELETE", "/api/v1/auth/mfa", json={"code": recovery[0]}, headers=_csrf(client)
    )
    assert r.status_code == 403 and r.json()["error"]["code"] == "mfa_required"
