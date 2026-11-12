"""Chaves de API contra o Postgres: criar pela sessão, usar pelo Bearer, limites."""

import os
import secrets
from datetime import timedelta

import pytest
import redis
from avant_core.access.models import ApiKey
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.shared.clock import SystemClock
from avant_core.shared.tokens import hash_token
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.limits import API_KEY, BucketRule, RedisBucket
from tests.conftest import FINANCE, CapturingMailer, browser, run_password_reset_tasks
from tests.fakes import MemoryBucket
from tests.test_api import PASSWORD, _csrf, _onboard_owner, _owner_invite
from tests.test_team import _member_client


def _bearer(client: TestClient, token: str) -> TestClient:
    """Outro cliente, sem cookie: só a chave."""
    other = browser(client.app)
    other.headers["Authorization"] = f"Bearer {token}"
    return other


def _create(client: TestClient, **body: object) -> dict:  # type: ignore[type-arg]
    payload = {"name": "ERP", "permissions": ["sites.view", "reports.view"]} | body
    r = client.post("/api/v1/api-keys", json=payload, headers=_csrf(client))
    assert r.status_code == 201, r.text
    return r.json()  # type: ignore[no-any-return]


def test_create_use_and_revoke(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    created = _create(client, expires_in_days=30)
    token = created["token"]
    assert token.startswith("avk_") and created["prefix"] == token[4:12]
    assert created["owner"]["name"] == "Dono" and created["permissions"] == [
        "reports.view",
        "sites.view",
    ]
    (listed,) = client.get("/api/v1/api-keys").json()["items"]
    assert "token" not in listed and listed["id"] == created["id"]

    key = _bearer(client, token)
    r = key.get("/api/v1/sites")
    assert r.status_code == 200 and r.json()["items"] == []
    assert r.headers["X-RateLimit-Limit"] == "20" and int(r.headers["X-RateLimit-Remaining"]) < 20
    # A chave só tem o que escolheu, mesmo sendo do dono.
    assert key.get("/api/v1/members").json()["error"]["code"] == "permission_denied"
    assert key.get("/api/v1/networks").status_code == 403

    # Rotas só da sessão.
    assert key.get("/api/v1/auth/me").status_code == 401
    again = key.post("/api/v1/api-keys", json={"name": "x", "permissions": ["sites.view"]})
    assert again.status_code == 401
    assert key.post("/api/v1/members/me/leave").status_code == 401

    bad = _bearer(client, "avk_" + "x" * 43).get("/api/v1/sites")
    assert bad.status_code == 401 and bad.json()["error"]["code"] == "not_authenticated"

    # Escrita pela chave não pede CSRF.
    assert key.delete(f"/api/v1/api-keys/{created['id']}").status_code == 204
    assert key.get("/api/v1/sites").status_code == 401
    (revoked,) = client.get("/api/v1/api-keys").json()["items"]
    assert revoked["revoked_at"] is not None and revoked["last_used_at"] is not None
    entries = client.get("/api/v1/audit").json()["items"]
    assert {"api_key.created", "api_key.revoked"} <= {entry["action"] for entry in entries}
    (by_key,) = [entry for entry in entries if entry["action"] == "api_key.revoked"]
    assert by_key["actor_kind"] == "api_key" and by_key["actor_api_key_id"] == created["id"]
    (by_owner,) = [entry for entry in entries if entry["action"] == "api_key.created"]
    assert by_owner["actor_kind"] == "member" and by_owner["actor_api_key_id"] is None


def test_permissions_on_keys(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")  # Financeiro: sem api_keys.manage
    denied = ana.post(
        "/api/v1/api-keys", json={"name": "x", "permissions": ["sites.view"]}, headers=_csrf(ana)
    )
    assert denied.status_code == 403 and denied.json()["error"]["code"] == "permission_denied"
    assert ana.get("/api/v1/api-keys").json()["items"] == []

    owner_key = _create(client)
    other = ana.delete(f"/api/v1/api-keys/{owner_key['id']}", headers=_csrf(ana))
    assert other.status_code == 403

    r = client.post(
        "/api/v1/api-keys",
        json={"name": "x", "permissions": ["api_keys.manage"]},
        headers=_csrf(client),
    )
    assert r.status_code == 422 and r.json()["error"]["code"] == "invalid_permission"
    r = client.post(
        "/api/v1/api-keys",
        json={"name": "x", "permissions": ["sites.view"], "expires_in_days": 400},
        headers=_csrf(client),
    )
    assert r.status_code == 422


def test_rate_limit(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    key = _bearer(client, _create(client)["token"])
    codes = [key.get("/api/v1/api-keys").status_code for _ in range(API_KEY.burst + 1)]
    assert codes[:-1] == [200] * API_KEY.burst
    r = key.get("/api/v1/api-keys")
    assert r.status_code == 429 and r.json()["error"]["code"] == "rate_limited"
    assert int(r.headers["Retry-After"]) >= 1 and r.headers["X-RateLimit-Remaining"] == "0"


RULE = BucketRule(rate=2.0, burst=3, abuse_limit=2, block_seconds=30)


def _exercise(bucket: MemoryBucket | RedisBucket, subject: str) -> None:
    t = 1000.0
    assert [bucket.take(subject, RULE, t).allowed for _ in range(3)] == [True, True, True]
    denied = bucket.take(subject, RULE, t)
    assert not denied.allowed and denied.retry_after == 1
    assert bucket.take(subject, RULE, t + 0.5).allowed  # meio segundo: uma ficha de volta
    bucket.take(subject, RULE, t + 0.5)
    blocked = bucket.take(subject, RULE, t + 0.5)  # terceira recusa no minuto: bloqueio
    assert not blocked.allowed and blocked.retry_after == 30


def test_memory_bucket() -> None:
    bucket = MemoryBucket()
    _exercise(bucket, "a")
    assert not bucket.take("a", RULE, 1000.5 + 29).allowed
    assert bucket.take("a", RULE, 1000.5 + 31).allowed
    assert bucket.take("b", RULE, 1000.0).allowed  # cada chave com o seu balde


@pytest.mark.skipif(not os.environ.get("AVANT_TEST_REDIS_URL"), reason="sem Redis de teste")
def test_redis_bucket() -> None:
    client = redis.Redis.from_url(os.environ["AVANT_TEST_REDIS_URL"])
    prefix = "avant:test:bucket"
    for k in client.scan_iter(f"{prefix}:*"):
        client.delete(k)
    _exercise(RedisBucket(client, prefix=prefix), "a")
    assert client.ttl(f"{prefix}:a:blocked") > 0


def _keys_in_two_companies(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> list[str]:
    """O dono da Açaí entra também na Bacuri e tem uma chave em cada Empresa."""
    _onboard_owner(client, engine, mailer)
    tokens = [_create(client)["token"]]
    bacuri = browser(client.app)
    invite = _owner_invite(engine, mailer, "dono@bacuri.com", "Bacuri Sites")
    opened = bacuri.post(
        f"/api/v1/auth/invitations/{invite}/accept", json={"name": "Bia", "password": PASSWORD}
    )
    assert opened.status_code == 200, opened.text
    invited = bacuri.post(
        "/api/v1/invitations",
        json={"email": "dono@acai.com", "role_id": str(FINANCE)},
        headers=_csrf(bacuri),
    )
    assert invited.status_code == 201, invited.text
    accepted = client.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept", json={}, headers=_csrf(client)
    )
    assert accepted.status_code == 200, accepted.text
    tokens.append(_insert_key(engine, opened.json()["active_company_id"], "dono@acai.com"))
    for key_token in tokens:
        assert _bearer(client, key_token).get("/api/v1/company").status_code != 401
    return tokens


def _insert_key(engine: Engine, company_id: str, email: str) -> str:
    """Grava direto no banco uma chave da pessoa na Empresa e devolve o token."""
    token = "avk_" + secrets.token_urlsafe(32)[:43].ljust(43, "x")
    now = SystemClock().now()
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        user = uow.users.get_by_email(email)
        assert user is not None
        membership = next(
            membership
            for membership in uow.memberships.list_for_user(user.id)
            if str(membership.company_id) == company_id
        )
        uow.api_keys.add(
            ApiKey(
                company_id=membership.company_id,
                membership_id=membership.id,
                name="Bacuri",
                prefix=token[4:12],
                secret_hash=hash_token(token),
                permissions=["reports.view"],
                created_at=now,
                expires_at=now + timedelta(days=30),
            )
        )
        uow.commit()
    return token


def test_change_password_revokes_keys_in_every_company(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    tokens = _keys_in_two_companies(client, engine, mailer)
    body = {"current_password": PASSWORD, "new_password": "outra-senha-456"}
    changed = client.post("/api/v1/auth/password/change", json=body, headers=_csrf(client))
    assert changed.status_code == 204, changed.text
    for key_token in tokens:
        assert _bearer(client, key_token).get("/api/v1/company").status_code == 401


def test_reset_password_revokes_keys_in_every_company(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    tokens = _keys_in_two_companies(client, engine, mailer)
    client.post("/api/v1/auth/password/forgot", json={"email": "dono@acai.com"})
    run_password_reset_tasks(client)
    body = {"token": mailer.resets[-1][1], "password": "outra-senha-456"}
    assert client.post("/api/v1/auth/password/reset", json=body).status_code == 204
    for key_token in tokens:
        assert _bearer(client, key_token).get("/api/v1/company").status_code == 401
