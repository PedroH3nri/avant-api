"""Conta pela API: recuperar e trocar senha, sessões, limite de tentativas e Google."""

import base64
import json
import os
import time
import uuid
from urllib.parse import parse_qs, urlparse

import pytest
from avant_core.identity.account import GoogleIdentity
from avant_core.mail import render_notice, render_password_reset
from avant_core.ports import Notice
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.errors import GoogleFailed
from avant_api.app.google import identity_from_id_token
from avant_api.app.limits import Limiter, MemoryCounter, RedisCounter, Rule
from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner

NEW = "outra-senha-456"
EMAIL = "dono@acai.com"


def _login(client: TestClient, password: str = PASSWORD) -> int:
    r = client.post("/api/v1/auth/login", json={"email": EMAIL, "password": password})
    status: int = r.status_code
    return status


def test_forgot_and_reset_password(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    forgot = client.post("/api/v1/auth/password/forgot", json={"email": "ninguem@x.com"})
    assert forgot.status_code == 202 and mailer.resets == []
    assert client.post("/api/v1/auth/password/forgot", json={"email": EMAIL}).status_code == 202
    ((to, token),) = mailer.resets
    assert to == EMAIL

    bad = client.post("/api/v1/auth/password/reset", json={"token": "x" * 20, "password": NEW})
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_token"
    r = client.post("/api/v1/auth/password/reset", json={"token": token, "password": NEW})
    assert r.status_code == 204, r.text
    assert client.get("/api/v1/auth/me").status_code == 401  # todas as sessões caíram
    assert mailer.notices == [(EMAIL, Notice.PASSWORD_CHANGED)]
    assert _login(client) == 401 and _login(client, NEW) == 200
    again = client.post("/api/v1/auth/password/reset", json={"token": token, "password": NEW})
    assert again.json()["error"]["code"] == "invalid_token"


def test_change_password_and_sessions(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    # Com IP de verdade: a coluna inet volta como IPv4Address e precisa virar texto.
    with TestClient(client.app, client=("203.0.113.7", 50000)) as other:
        assert (
            other.post(
                "/api/v1/auth/login", json={"email": EMAIL, "password": PASSWORD}
            ).status_code
            == 200
        )
        sessions = client.get("/api/v1/auth/sessions").json()
        assert len(sessions) == 2 and sum(s["current"] for s in sessions) == 1
        assert {s["ip"] for s in sessions} == {None, "203.0.113.7"}

        wrong = client.post(
            "/api/v1/auth/password/change",
            json={"current_password": "errada", "new_password": NEW},
            headers=_csrf(client),
        )
        assert wrong.status_code == 401
        ok = client.post(
            "/api/v1/auth/password/change",
            json={"current_password": PASSWORD, "new_password": NEW},
            headers=_csrf(client),
        )
        assert ok.status_code == 204, ok.text
        assert other.get("/api/v1/auth/me").status_code == 401
        assert client.get("/api/v1/auth/me").status_code == 200

        assert (
            other.post("/api/v1/auth/login", json={"email": EMAIL, "password": NEW}).status_code
            == 200
        )
        r = client.post("/api/v1/auth/sessions/revoke-others", headers=_csrf(client))
        assert r.json() == {"revoked": 1}
        assert other.get("/api/v1/auth/me").status_code == 401

    (current,) = client.get("/api/v1/auth/sessions").json()
    assert (
        client.delete(f"/api/v1/auth/sessions/{uuid.uuid4()}", headers=_csrf(client)).status_code
        == 404
    )
    r = client.delete(f"/api/v1/auth/sessions/{current['id']}", headers=_csrf(client))
    assert r.status_code == 204
    assert client.get("/api/v1/auth/me").status_code == 401


def test_login_attempts_are_limited(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    assert [_login(client, "errada") for _ in range(5)] == [401] * 5
    r = client.post("/api/v1/auth/login", json={"email": EMAIL, "password": PASSWORD})
    assert r.status_code == 429 and r.json()["error"]["code"] == "too_many_attempts"
    assert 0 < int(r.headers["Retry-After"]) <= 900


class FakeGoogle:
    def __init__(self, identity: GoogleIdentity) -> None:
        self.identity = identity

    def authorize_url(self, *, state: str, verifier: str, nonce: str) -> str:
        return f"https://google.test/auth?state={state}"

    def exchange(self, *, code: str, verifier: str, nonce: str) -> GoogleIdentity:
        if code != "bom":
            raise GoogleFailed("código recusado")
        return self.identity


def _google_round(
    client: TestClient, mode: str, code: str = "bom"
) -> tuple[str, dict[str, list[str]]]:
    start = client.get(f"/api/v1/auth/google/start?mode={mode}", follow_redirects=False)
    assert start.status_code == 302, start.text
    state = parse_qs(urlparse(start.headers["location"]).query)["state"][0]
    back = client.get(
        f"/api/v1/auth/google/callback?code={code}&state={state}", follow_redirects=False
    )
    assert back.status_code == 302
    url = urlparse(back.headers["location"])
    return url.path, parse_qs(url.query)


def test_google_link_and_login(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    services = client.app.state.services  # type: ignore[attr-defined]
    assert client.get("/api/v1/auth/google/start").status_code == 503
    _onboard_owner(client, engine, mailer)
    services.google = FakeGoogle(GoogleIdentity("g-1", EMAIL, True))
    try:
        assert client.get("/api/v1/auth/google").json() == {"available": True, "linked": False}
        # Sem ligar antes, o login com Google não entra.
        client.post("/api/v1/auth/logout", headers=_csrf(client))
        assert _google_round(client, "login") == ("/entrar", {"erro": ["google_not_linked"]})
        assert client.get("/api/v1/auth/me").status_code == 401

        assert _login(client) == 200
        assert _google_round(client, "link") == ("/configuracoes/conta", {"google": ["ligado"]})
        assert client.get("/api/v1/auth/google").json()["linked"] is True
        assert mailer.notices == [(EMAIL, Notice.GOOGLE_LINKED)]

        client.post("/api/v1/auth/logout", headers=_csrf(client))
        assert _google_round(client, "login") == ("/", {})
        assert client.get("/api/v1/auth/me").json()["user"]["email"] == EMAIL

        assert _google_round(client, "login", code="ruim")[1] == {"erro": ["google_failed"]}
        forged = client.get(
            "/api/v1/auth/google/callback?code=bom&state=outro", follow_redirects=False
        )
        assert "erro=google_failed" in forged.headers["location"]

        assert client.delete("/api/v1/auth/google", headers=_csrf(client)).status_code == 204
        assert client.get("/api/v1/auth/google").json()["linked"] is False

        services.google = FakeGoogle(GoogleIdentity("g-2", "nova@x.com", True))
        assert _google_round(client, "login")[1] == {"erro": ["no_access"]}
    finally:
        services.google = None


# --- Sem banco --------------------------------------------------------------------------


def _jwt(claims: dict[str, object]) -> str:
    part = base64.urlsafe_b64encode(json.dumps(claims).encode()).rstrip(b"=").decode()
    return f"e30.{part}.assinatura"


def test_id_token_claims() -> None:
    good = {
        "iss": "https://accounts.google.com",
        "aud": "cliente",
        "exp": time.time() + 60,
        "nonce": "n1",
        "sub": "123",
        "email": "ana@x.com",
        "email_verified": True,
    }
    identity = identity_from_id_token(_jwt(good), client_id="cliente", nonce="n1")
    assert identity == GoogleIdentity("123", "ana@x.com", True)
    for change in ({"aud": "outro"}, {"iss": "https://evil.com"}, {"exp": 1}, {"nonce": "n2"}):
        with pytest.raises(GoogleFailed):
            identity_from_id_token(_jwt({**good, **change}), client_id="cliente", nonce="n1")
    with pytest.raises(GoogleFailed):
        identity_from_id_token("lixo", client_id="cliente", nonce="n1")


def test_account_emails() -> None:
    msg = render_password_reset(link="https://avant.groone.com/redefinir-senha/abc", locale="es")
    assert "Restablecer" in msg.subject and "/redefinir-senha/abc" in msg.html
    for notice in Notice:
        for locale in ("pt", "en", "es", "fr"):
            m = render_notice(notice=notice, locale=locale)
            assert m.subject and m.text and "<script" not in m.html


def _limiter_round(limiter: Limiter) -> None:
    rule = Rule("teste", 2, 60)
    limiter.check((rule, "a"))
    limiter.fail((rule, "a"), (rule, None))
    limiter.fail((rule, "a"))
    with pytest.raises(Exception, match="muitas tentativas"):
        limiter.check((rule, "A"))
    limiter.check((rule, "b"))
    limiter.clear(rule, "a")
    limiter.check((rule, "a"))


def test_memory_limiter() -> None:
    _limiter_round(Limiter(MemoryCounter()))


@pytest.mark.skipif(
    not os.environ.get("AVANT_TEST_REDIS_URL"), reason="defina AVANT_TEST_REDIS_URL"
)
def test_redis_limiter() -> None:
    _limiter_round(
        Limiter(RedisCounter.from_url(os.environ["AVANT_TEST_REDIS_URL"]), f"teste:{uuid.uuid4()}")
    )
