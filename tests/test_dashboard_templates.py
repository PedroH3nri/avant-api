"""Modelos prontos de dashboard contra o Postgres: gestão no painel interno e quem vê cada um."""

from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import FINANCE, CapturingMailer, browser
from tests.test_api import _csrf, _onboard_owner
from tests.test_commissions import _support
from tests.test_internal import _staff
from tests.test_team import _member_client

URL = "/api/v1/internal/dashboard-templates"
NOTE = {"id": "nota", "type": "text", "x": 0, "y": 0, "w": 4, "h": 2, "text": "Bem-vindo"}


def _form(**changes: Any) -> dict[str, Any]:
    """Um modelo dos clientes com uma nota, limitado ao papel Financeiro."""
    body: dict[str, Any] = {
        "name": {"pt": "Financeiro", "en": "Finance", "es": ""},
        "definition": {"schema_version": 1, "filters": {}, "widgets": [NOTE]},
        "audience": "clients",
        "role_ids": [str(FINANCE)],
    }
    body.update(changes)
    return body


def test_staff_manage_templates_and_clients_see_them_by_role(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    staff = _staff(client, engine)

    listed = staff.get(URL).json()["items"]
    assert {item["audience"] for item in listed} == {"groone", "clients"}
    assert sum(item["is_home"] for item in listed) == 2
    roles = staff.get(f"{URL}/roles").json()
    assert str(FINANCE) in {role["id"] for role in roles["clients"]}
    assert "groone_support" not in {role["id"] for role in roles["clients"]}

    created = staff.post(URL, json=_form(), headers=_csrf(staff))
    assert created.status_code == 201, created.text
    template = created.json()
    assert template["name"] == {"pt": "Financeiro", "en": "Finance", "es": "Financeiro"}
    assert template["is_home"] is False
    seen = {item["id"] for item in ana.get("/api/v1/dashboards/templates").json()["items"]}
    assert template["id"] in seen
    staff_seen = staff.get("/api/v1/dashboards/templates").json()["items"]
    assert template["id"] not in {item["id"] for item in staff_seen}

    marked = staff.put(f"{URL}/{template['id']}/home", headers=_csrf(staff))
    assert marked.status_code == 200 and marked.json()["is_home"] is True
    home = ana.get("/api/v1/dashboards/home").json()
    assert home["dashboard"] is None and home["template"]["id"] == template["id"]

    other_roles = _form(role_ids=[roles["groone"][0]["id"]])
    refused = staff.put(f"{URL}/{template['id']}", json=other_roles, headers=_csrf(staff))
    assert refused.status_code == 422
    goal = {"id": "meta", "type": "goal", "x": 0, "y": 2, "w": 4, "h": 2, "goal_scope": "team"}
    with_goal = _form(definition={"schema_version": 1, "filters": {}, "widgets": [goal]})
    assert staff.post(URL, json=with_goal, headers=_csrf(staff)).status_code == 422

    moved = staff.put(
        f"{URL}/{template['id']}", json=_form(audience="groone", role_ids=[]), headers=_csrf(staff)
    )
    assert moved.status_code == 200, moved.text
    assert moved.json()["is_home"] is False and moved.json()["audience"] == "groone"
    fallback = ana.get("/api/v1/dashboards/home").json()["template"]
    assert fallback["id"] != template["id"]
    assert staff.get(f"{URL}/{template['id']}").json()["audience"] == "groone"

    removed = staff.delete(f"{URL}/{template['id']}", headers=_csrf(staff))
    assert removed.status_code == 204
    assert staff.get(f"{URL}/{template['id']}").status_code == 404


def test_templates_need_the_permission_and_the_groone_company(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    owner = browser(client.app)
    _onboard_owner(owner, engine, mailer)
    staff = _staff(client, engine)
    support = _support(client, staff, mailer)
    for person in (owner, support):
        assert person.get(URL).status_code == 403
        assert person.post(URL, json=_form(), headers=_csrf(person)).status_code == 403
    denied = support.get(f"{URL}/roles")
    assert denied.status_code == 403 and denied.json()["error"]["code"] == "permission_denied"
