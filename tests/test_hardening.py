"""Endurecimento da API: documentação fechada em produção, cabeçalhos, Redis fora do ar,
cookies da sessão, limite do Bearer por IP e segredos fora do log."""

import logging
from dataclasses import replace
from typing import Any

import pytest
from avant_core.access.services import authenticate_api_key
from avant_core.db.uow import SqlAlchemyUnitOfWork
from fastapi.testclient import TestClient
from sqlalchemy import Engine, text

from avant_api.app import security
from avant_api.app.limits import API_KEY_IP, Limiter, RedisCounter
from avant_api.app.logs import JsonFormatter, masked_path
from avant_api.app.middleware import CONTENT_SECURITY_POLICY, DOCS_CONTENT_SECURITY_POLICY
from avant_api.main import create_app
from avant_api.modules.auth.dependencies import auth_service
from tests.conftest import CapturingMailer, browser
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff

DOCS_PATHS = ("/api/docs", "/api/v1/openapi.json", "/api/docs/assets/swagger-ui-bundle.js")


@pytest.mark.parametrize("env", ["local", "production"])
def test_docs_only_for_the_groone_session_with_2fa(
    client: TestClient, engine: Engine, mailer: CapturingMailer, env: str
) -> None:
    services = client.app.state.services  # type: ignore[attr-defined]
    settings = services.settings.model_copy(update={"avant_env": env})
    app = create_app(replace(services, settings=settings))
    for path in DOCS_PATHS:
        anonymous = browser(app).get(path)
        assert anonymous.status_code == 401, path
        assert anonymous.headers["Content-Security-Policy"] == CONTENT_SECURITY_POLICY
    _onboard_owner(client, engine, mailer)
    owner = browser(app, cookies=client.cookies)
    for path in DOCS_PATHS:
        refused = owner.get(path)
        assert refused.status_code == 403 and refused.json()["error"]["code"] == "staff_only"
    staff = browser(app, cookies=_staff(client, engine).cookies)
    page = staff.get("/api/docs")
    assert page.status_code == 200 and "text/html" in page.headers["Content-Type"]
    assert page.headers["Content-Security-Policy"] == DOCS_CONTENT_SECURITY_POLICY
    assert page.headers["X-Frame-Options"] == "DENY"
    schema = staff.get("/api/v1/openapi.json")
    assert schema.status_code == 200 and "/api/v1/internal/clients" in schema.json()["paths"]
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        uow.session.execute(text("UPDATE sessions SET mfa_verified_at = NULL"))
        uow.commit()
    for path in DOCS_PATHS:
        unverified = staff.get(path)
        assert unverified.status_code == 403, path
        assert unverified.json()["error"]["code"] == "mfa_required"


def test_every_response_has_the_security_headers(client: TestClient) -> None:
    for response in (client.get("/api/v1/health"), client.get("/api/v1/nada")):
        assert response.headers["X-Content-Type-Options"] == "nosniff"
        assert response.headers["X-Frame-Options"] == "DENY"
        assert response.headers["Referrer-Policy"] == "no-referrer"


def test_redis_down_is_a_503_not_a_500(client: TestClient) -> None:
    services = client.app.state.services  # type: ignore[attr-defined]
    broken = replace(
        services, limiter=Limiter(RedisCounter.from_url("redis://127.0.0.1:1/0"), "teste")
    )
    app = browser(create_app(broken), raise_server_exceptions=False)
    response = app.post("/api/v1/auth/login", json={"email": "a@b.com", "password": "x" * 12})
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "service_unavailable"
    assert response.headers["Retry-After"] == "5"


def test_every_response_has_the_content_security_policy(client: TestClient) -> None:
    for response in (client.get("/api/v1/health"), client.get("/api/v1/nada")):
        assert response.headers["Content-Security-Policy"] == CONTENT_SECURITY_POLICY
    assert CONTENT_SECURITY_POLICY == "default-src 'none'; frame-ancestors 'none'"


def test_old_docs_paths_do_not_exist(client: TestClient) -> None:
    for path in ("/docs", "/redoc", "/openapi.json", "/docs/oauth2-redirect"):
        response = client.get(path)
        assert response.status_code == 404, path
        assert response.headers["Content-Security-Policy"] == CONTENT_SECURITY_POLICY


def test_masked_path_hides_the_invitation_token() -> None:
    token = "segredo-do-convite"
    assert masked_path(f"/api/v1/auth/invitations/{token}") == "/api/v1/auth/invitations/***"
    accept = masked_path(f"/api/v1/auth/invitations/{token}/accept")
    assert accept == "/api/v1/auth/invitations/***/accept"
    assert masked_path("/api/v1/invitations/123/resend") == "/api/v1/invitations/123/resend"


class _BrokenAuthService:
    """Service do login que quebra em qualquer chamada, para forçar um 500."""

    def preview_invitation(self, token: str) -> None:
        """Simula um erro inesperado ao ler o convite."""
        raise RuntimeError("falha inesperada")


def test_unexpected_error_log_hides_the_invitation_token(
    client: TestClient, caplog: pytest.LogCaptureFixture
) -> None:
    token = "tok-" + "s" * 40
    app = client.app
    app.dependency_overrides[auth_service] = _BrokenAuthService  # type: ignore[attr-defined]
    try:
        with caplog.at_level(logging.INFO):
            response = browser(app, raise_server_exceptions=False).get(
                f"/api/v1/auth/invitations/{token}"
            )
    finally:
        app.dependency_overrides.clear()  # type: ignore[attr-defined]
    assert response.status_code == 500
    (error,) = [record for record in caplog.records if record.getMessage() == "erro inesperado"]
    assert error.path == "/api/v1/auth/invitations/***"  # type: ignore[attr-defined]
    assert token not in _rendered(caplog)


def _rendered(caplog: pytest.LogCaptureFixture) -> str:
    """Os registros da API como saem no log de produção (JSON); o httpx é o cliente do teste."""
    formatter = JsonFormatter()
    server = [record for record in caplog.records if record.name != "httpx"]
    return "\n".join(formatter.format(record) for record in server)


def test_invalid_bearer_is_limited_per_ip_before_the_database(
    client: TestClient, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[str] = []

    def counting(*args: Any, **kwargs: Any) -> Any:
        """Conta cada consulta da chave no banco."""
        calls.append(kwargs["token"])
        return authenticate_api_key(*args, **kwargs)

    monkeypatch.setattr(security, "authenticate_api_key", counting)
    bearer = browser(client.app)
    bearer.headers["Authorization"] = "Bearer avk_" + "x" * 43
    codes = [bearer.get("/api/v1/sites").status_code for _ in range(API_KEY_IP.limit)]
    assert codes == [401] * API_KEY_IP.limit
    blocked = bearer.get("/api/v1/sites")
    assert blocked.status_code == 429
    assert blocked.json()["error"]["code"] == "too_many_attempts"
    assert int(blocked.headers["Retry-After"]) > 0
    assert len(calls) == API_KEY_IP.limit


def test_valid_key_never_holds_a_slot_of_the_ip_limit(
    client: TestClient, engine: Engine, mailer: CapturingMailer, monkeypatch: pytest.MonkeyPatch
) -> None:
    _onboard_owner(client, engine, mailer)
    created = client.post(
        "/api/v1/api-keys",
        json={"name": "ERP", "permissions": ["sites.view"]},
        headers=_csrf(client),
    ).json()
    services = client.app.state.services  # type: ignore[attr-defined]
    seen: list[int] = []

    def counting(*args: Any, **kwargs: Any) -> Any:
        """Lê o contador do IP enquanto a chave é conferida no banco."""
        seen.append(services.limiter.count(API_KEY_IP, "testclient"))
        return authenticate_api_key(*args, **kwargs)

    monkeypatch.setattr(security, "authenticate_api_key", counting)
    bearer = browser(client.app)
    bearer.headers["Authorization"] = f"Bearer {created['token']}"
    for _ in range(3):
        assert bearer.get("/api/v1/sites").status_code == 200
    assert seen == [0, 0, 0]
    assert services.limiter.count(API_KEY_IP, "testclient") == 0


def test_session_cookies_are_secure_httponly_and_samesite(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    client.post("/api/v1/auth/logout", headers=_csrf(client))
    login = client.post("/api/v1/auth/login", json={"email": "dono@acai.com", "password": PASSWORD})
    assert login.status_code == 200
    cookies = {
        cookie.split("=")[0]: cookie.lower() for cookie in login.headers.get_list("set-cookie")
    }
    session, csrf = cookies["__Host-avant_session"], cookies["__Host-avant_csrf"]
    assert "httponly" in session and "samesite=lax" in session and "secure" in session
    assert "httponly" not in csrf and "samesite=lax" in csrf and "secure" in csrf


def test_api_key_never_reaches_the_log(
    client: TestClient, engine: Engine, mailer: CapturingMailer, caplog: pytest.LogCaptureFixture
) -> None:
    _onboard_owner(client, engine, mailer)
    created = client.post(
        "/api/v1/api-keys",
        json={"name": "ERP", "permissions": ["sites.view"]},
        headers=_csrf(client),
    )
    token = created.json()["token"]
    bearer = browser(client.app, raise_server_exceptions=False)
    bearer.headers["Authorization"] = f"Bearer {token}"
    with caplog.at_level(logging.INFO):
        assert bearer.get("/api/v1/sites").status_code == 200
        assert bearer.get("/api/v1/members").status_code == 403
        assert bearer.get("/api/v1/nada").status_code == 404
    assert any(record.getMessage() == "request" for record in caplog.records)
    rendered = _rendered(caplog)
    assert token not in rendered and token[4:] not in rendered
