"""Metas da equipe Groone contra o Postgres: modelos, meta do papel e andamento."""

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff

MONTHS = [str(1000 + index) for index in range(12)]


def _template(staff: TestClient, **extra: object) -> dict:  # type: ignore[type-arg]
    """Cadastra um modelo de meta de 2026."""
    body: dict[str, object] = {"name": "Comercial 2026", "year": 2026, "months": MONTHS}
    body.update(extra)
    response = staff.post("/api/v1/internal/goal-templates", json=body, headers=_csrf(staff))
    assert response.status_code == 201, response.text
    return response.json()  # type: ignore[no-any-return]


def test_goal_templates_and_role_goal(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    template = _template(staff)
    assert template["months"][9] == "1009.00" and template["currency"] == "USD"
    company = _template(staff, name="Groone 2026", is_company_goal=True)
    taken = staff.post(
        "/api/v1/internal/goal-templates",
        json={"name": "Outra", "year": 2026, "months": MONTHS, "is_company_goal": True},
        headers=_csrf(staff),
    )
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "company_goal_taken"
    short = staff.post(
        "/api/v1/internal/goal-templates",
        json={"name": "Curta", "year": 2026, "months": MONTHS[:11]},
        headers=_csrf(staff),
    )
    assert short.status_code == 422
    listed = staff.get("/api/v1/internal/goal-templates").json()["items"]
    assert {item["name"] for item in listed} == {"Comercial 2026", "Groone 2026"}

    renamed = staff.put(
        f"/api/v1/internal/goal-templates/{template['id']}",
        json={"name": "Comercial", "year": 2026, "months": MONTHS},
        headers=_csrf(staff),
    )
    assert renamed.status_code == 200 and renamed.json()["name"] == "Comercial"

    role = next(
        item for item in staff.get("/api/v1/roles").json()["items"] if item["key"] == "groone_admin"
    )
    set_goal = staff.put(
        f"/api/v1/internal/roles/{role['id']}/goal",
        json={"goal_template_id": template["id"], "goal_mode": "split"},
        headers=_csrf(staff),
    )
    assert set_goal.status_code == 204, set_goal.text
    goals = staff.get("/api/v1/internal/role-goals").json()["items"]
    assert goals == [
        {"role_id": role["id"], "goal_template_id": template["id"], "goal_mode": "split"}
    ]
    cleared = staff.put(
        f"/api/v1/internal/roles/{role['id']}/goal",
        json={"goal_template_id": None, "goal_mode": "split"},
        headers=_csrf(staff),
    )
    assert cleared.status_code == 204
    assert staff.get("/api/v1/internal/role-goals").json()["items"] == []

    deleted = staff.delete(f"/api/v1/internal/goal-templates/{company['id']}", headers=_csrf(staff))
    assert deleted.status_code == 204


def test_goal_progress_routes(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    staff = _staff(client, engine)
    _template(staff, name="Groone 2026", is_company_goal=True)
    team = staff.get("/api/v1/internal/goals?month=2026-10")
    assert team.status_code == 200, team.text
    body = team.json()
    assert body["month"] == "2026-10"
    assert body["company"]["goal"] == "1009.00" and body["company"]["done"] == "0.00"
    assert [person["name"] for person in body["people"]] == ["Admin"]
    mine = staff.get("/api/v1/internal/goals/me?month=2026-10")
    assert mine.status_code == 200 and mine.json()["progress"]["goal"] is None
    assert staff.get("/api/v1/internal/goals?month=2026-13").status_code == 422

    _onboard_owner(client, engine, mailer)
    for response in (
        client.get("/api/v1/internal/goals"),
        client.get("/api/v1/internal/goals/me"),
        client.get("/api/v1/internal/goal-templates"),
    ):
        assert response.status_code == 403, response.text
