"""Texto com byte nulo, que o Postgres recusa, volta 422 em vez de erro 500 (api#346)."""

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner


def test_null_byte_in_search_and_report_filter_is_invalid_input(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    found = client.get("/api/v1/sites", params={"q": "a\x00b"})
    assert found.status_code == 422, found.text
    assert found.json()["error"]["code"] == "validation_error"
    query = {
        "metrics": ["revenue"],
        "period": {"start": "2026-11-01", "end": "2026-11-19"},
        "dimensions": ["site"],
        "filters": [{"field": "country", "operator": "eq", "values": ["\x00"]}],
    }
    report = client.post("/api/v1/reports/query", json=query, headers=_csrf(client))
    assert report.status_code == 422, report.text
    assert client.get("/api/v1/sites", params={"q": "ab"}).status_code == 200


def test_public_page_url_with_brackets_is_just_not_found(client: TestClient) -> None:
    """URL com colchetes no reward e na tag não derruba a rota pública (core#442)."""
    for path in ("/api/reward/v2", "/api/tag/config"):
        response = client.get(path, params={"url": "[]"})
        assert response.status_code < 500, (path, response.text)
