"""Envios agendados contra o Postgres: CRUD, pausa, regras de horário e permissões."""

from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_saved_reports import _report
from tests.test_team import _member_client


def _form(target_id: str, recipients: list[str], **changes: Any) -> dict[str, Any]:
    """Um envio semanal (segunda, 9h de São Paulo) do relatório dado."""
    body: dict[str, Any] = {
        "name": "Resumo semanal",
        "target": "report",
        "target_id": target_id,
        "frequency": "weekly",
        "weekday": 0,
        "hour": 9,
        "timezone": "America/Sao_Paulo",
        "recipient_user_ids": recipients,
    }
    body.update(changes)
    return body


def test_schedules_of_a_client(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    owner_id = me["user"]["id"]
    report = client.post("/api/v1/reports", json=_report(), headers=_csrf(client)).json()

    created = client.post(
        "/api/v1/schedules", json=_form(report["id"], [owner_id]), headers=_csrf(client)
    )
    assert created.status_code == 201, created.text
    schedule = created.json()
    assert schedule["editable"] is True and schedule["paused"] is False
    assert schedule["target_name"] == report["name"] and schedule["last_delivery"] is None
    assert schedule["next_run_at"].endswith(("12:00:00Z", "12:00:00+00:00"))

    listed = client.get("/api/v1/schedules", params={"q": "semanal"}).json()
    assert listed["total"] == 1 and listed["items"][0]["id"] == schedule["id"]

    monthly = _form(report["id"], [owner_id], frequency="monthly", weekday=None, month_day=5)
    updated = client.put(f"/api/v1/schedules/{schedule['id']}", json=monthly, headers=_csrf(client))
    assert updated.status_code == 200, updated.text
    assert updated.json()["month_day"] == 5 and updated.json()["weekday"] is None

    paused = client.put(
        f"/api/v1/schedules/{schedule['id']}/pause", json={"paused": True}, headers=_csrf(client)
    )
    assert paused.status_code == 200 and paused.json()["paused"] is True

    bad_zone = _form(report["id"], [owner_id], timezone="Marte/Base")
    refused = client.post("/api/v1/schedules", json=bad_zone, headers=_csrf(client))
    assert refused.status_code == 422
    assert refused.json()["error"]["code"] == "invalid_input"
    no_day = _form(report["id"], [owner_id], weekday=None)
    assert client.post("/api/v1/schedules", json=no_day, headers=_csrf(client)).status_code == 422
    missing = _form("00000000-0000-0000-0000-000000000001", [owner_id])
    assert client.post("/api/v1/schedules", json=missing, headers=_csrf(client)).status_code == 404

    removed = client.delete(f"/api/v1/schedules/{schedule['id']}", headers=_csrf(client))
    assert removed.status_code == 204
    assert client.get(f"/api/v1/schedules/{schedule['id']}").status_code == 404


def test_members_without_schedules_manage_only_see_what_they_receive(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    ana_id = ana.get("/api/v1/auth/me").json()["user"]["id"]
    owner_id = me["user"]["id"]
    report = client.post("/api/v1/reports", json=_report(), headers=_csrf(client)).json()
    mine = client.post(
        "/api/v1/schedules", json=_form(report["id"], [owner_id]), headers=_csrf(client)
    ).json()
    shared = client.post(
        "/api/v1/schedules",
        json=_form(report["id"], [owner_id, ana_id], name="Com a Ana"),
        headers=_csrf(client),
    ).json()

    listed = ana.get("/api/v1/schedules").json()
    assert [item["id"] for item in listed["items"]] == [shared["id"]]
    assert listed["items"][0]["editable"] is False
    assert ana.get(f"/api/v1/schedules/{mine['id']}").status_code == 404
    denied = ana.post("/api/v1/schedules", json=_form(report["id"], [ana_id]), headers=_csrf(ana))
    assert denied.status_code == 403
    assert denied.json()["error"]["code"] == "permission_denied"
    pause = ana.put(
        f"/api/v1/schedules/{shared['id']}/pause", json={"paused": True}, headers=_csrf(ana)
    )
    assert pause.status_code == 403
    assert ana.delete(f"/api/v1/schedules/{shared['id']}", headers=_csrf(ana)).status_code == 403
