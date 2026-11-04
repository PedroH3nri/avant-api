"""Endurecimento da API: documentação fechada em produção, cabeçalhos e Redis fora do ar."""

from dataclasses import replace

from fastapi.testclient import TestClient

from avant_api.app.limits import Limiter, RedisCounter
from avant_api.main import create_app


def test_docs_are_closed_in_production(client: TestClient) -> None:
    services = client.app.state.services  # type: ignore[attr-defined]
    assert client.get("/api/docs").status_code == 200
    production = replace(
        services, settings=services.settings.model_copy(update={"avant_env": "production"})
    )
    closed = TestClient(create_app(production))
    assert closed.get("/api/docs").status_code == 404
    assert closed.get("/api/v1/openapi.json").status_code == 404


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
    app = TestClient(create_app(broken), raise_server_exceptions=False)
    response = app.post("/api/v1/auth/login", json={"email": "a@b.com", "password": "x" * 12})
    assert response.status_code == 503
    assert response.json()["error"]["code"] == "service_unavailable"
    assert response.headers["Retry-After"] == "5"
