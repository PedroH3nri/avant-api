"""Visões salvas das tabelas internas contra o Postgres: só a equipe Groone com 2FA."""

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff


def test_saved_views_crud_and_catalog(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    catalog = staff.get("/api/v1/internal/views/catalog/clients")
    assert catalog.status_code == 200, catalog.text
    assert "manager" in catalog.json()["columns"]
    assert {"key": "name", "direction": "asc"} in catalog.json()["sorts"]
    body = {
        "screen": "clients",
        "name": "Ativos por nome",
        "definition": {
            "columns": ["client", "status"],
            "filters": {"status": "active"},
            "sort": {"key": "name", "direction": "asc"},
        },
        "visibility": "company",
    }
    created = staff.post("/api/v1/internal/views", json=body, headers=_csrf(staff))
    assert created.status_code == 201, created.text
    view_id = created.json()["id"]
    assert created.json()["definition"]["schema_version"] == 1
    assert created.json()["editable"] is True
    listed = staff.get("/api/v1/internal/views", params={"screen": "clients"}).json()["items"]
    assert [item["id"] for item in listed] == [view_id]
    invoices = staff.get("/api/v1/internal/views", params={"screen": "invoices"})
    assert invoices.json()["items"] == []
    wrong = {**body, "definition": {"columns": ["revenue"]}}
    bad = staff.post("/api/v1/internal/views", json=wrong, headers=_csrf(staff))
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_input"
    changed = staff.put(
        f"/api/v1/internal/views/{view_id}",
        json={**body, "name": "Ativos", "visibility": "private"},
        headers=_csrf(staff),
    )
    assert changed.status_code == 200 and changed.json()["name"] == "Ativos"
    removed = staff.delete(f"/api/v1/internal/views/{view_id}", headers=_csrf(staff))
    assert removed.status_code == 204
    assert staff.get("/api/v1/internal/views", params={"screen": "clients"}).json()["items"] == []


def test_saved_views_are_staff_only(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    assert client.get("/api/v1/internal/views", params={"screen": "clients"}).status_code == 403
    assert client.get("/api/v1/internal/views/catalog/clients").status_code == 403


def test_clients_by_manager_and_name(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    for name in ("Zeta Visões", "alfa Visões"):
        profile = {"first_name": "Ana", "last_name": "Souza", "email": f"{name[:4]}@visoes.com"}
        r = staff.post(
            "/api/v1/internal/clients",
            json={"name": name, "seat_limit": 2, "profile": profile},
            headers=_csrf(staff),
        )
        assert r.status_code == 201, r.text
    by_name = staff.get(
        "/api/v1/internal/clients", params={"q": "visões", "sort": "name", "direction": "asc"}
    ).json()["items"]
    assert [item["name"] for item in by_name] == ["alfa Visões", "Zeta Visões"]
    nobody = staff.get(
        "/api/v1/internal/clients",
        params={"q": "visões", "manager": "00000000-0000-0000-0000-000000000001"},
    ).json()["items"]
    assert nobody == []
    assert staff.get("/api/v1/internal/clients", params={"sort": "revenue"}).status_code == 422
