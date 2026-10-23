"""Chaves de API contra o Postgres: criar pela sessão, usar pelo Bearer, limites."""

import os

import pytest
import redis
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.limits import API_KEY, BucketRule, MemoryBucket, RedisBucket
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_team import _member_client


def _bearer(client: TestClient, token: str) -> TestClient:
    """Outro cliente, sem cookie: só a chave."""
    other = TestClient(client.app)
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
    actions = {e["action"] for e in client.get("/api/v1/audit").json()["items"]}
    assert {"api_key.created", "api_key.revoked"} <= actions


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
