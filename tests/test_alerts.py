"""Alertas de métrica contra o Postgres: CRUD, prévia, silêncio, disparos e permissões."""

import uuid
from datetime import UTC, datetime, timedelta
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_reports import _metrics
from tests.test_team import _member_client


def _definition(
    metric: str = "revenue", condition: str = "below", value: str = "1000"
) -> dict[str, Any]:
    """Regra do alerta no formato salvo: a métrica no total, abaixo de um valor."""
    return {
        "schema_version": 1,
        "query": {
            "schema_version": 1,
            "source": "gam",
            "metrics": [metric],
            "period": {"preset": "yesterday", "start": None, "end": None},
            "dimensions": [],
            "filters": [],
            "compare": False,
            "order": [],
            "limit": 1000,
        },
        "condition": condition,
        "value": value,
        "baseline": None,
    }


def _form(recipients: list[str], **changes: Any) -> dict[str, Any]:
    """Um alerta com a regra padrão para as pessoas dadas."""
    body: dict[str, Any] = {
        "name": "Receita baixa",
        "definition": _definition(),
        "recipient_user_ids": recipients,
    }
    body.update(changes)
    return body


def test_alerts_of_a_client(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    owner_id = me["user"]["id"]

    preview = client.post(
        "/api/v1/alerts/preview", json={"definition": _definition()}, headers=_csrf(client)
    )
    assert preview.status_code == 200, preview.text
    [check] = preview.json()["checks"]
    assert check["firing"] is True and check["subject"] == ""

    created = client.post("/api/v1/alerts", json=_form([owner_id]), headers=_csrf(client))
    assert created.status_code == 201, created.text
    alert = created.json()
    assert alert["editable"] is True and alert["firing"] is False
    assert alert["currency"] == "USD" and alert["last_event"] is None

    listed = client.get("/api/v1/alerts", params={"q": "receita"}).json()
    assert listed["total"] == 1 and listed["items"][0]["id"] == alert["id"]

    changed = _form(
        [owner_id], name="Receita alta", definition=_definition(condition="above", value="1")
    )
    updated = client.put(f"/api/v1/alerts/{alert['id']}", json=changed, headers=_csrf(client))
    assert updated.status_code == 200, updated.text
    assert updated.json()["definition"]["condition"] == "above"

    until = (datetime.now(UTC) + timedelta(days=1)).isoformat()
    muted = client.put(
        f"/api/v1/alerts/{alert['id']}/mute", json={"until": until}, headers=_csrf(client)
    )
    assert muted.status_code == 200 and muted.json()["muted_until"] is not None
    too_long = (datetime.now(UTC) + timedelta(days=120)).isoformat()
    refused = client.put(
        f"/api/v1/alerts/{alert['id']}/mute", json={"until": too_long}, headers=_csrf(client)
    )
    assert refused.status_code == 422

    events = client.get(f"/api/v1/alerts/{alert['id']}/events").json()
    assert events["total"] == 0

    internal_metric = _form([owner_id], definition=_definition("revenue_groone"))
    invalid = client.post("/api/v1/alerts", json=internal_metric, headers=_csrf(client))
    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "invalid_input"
    stranger = client.post("/api/v1/alerts", json=_form([str(uuid.uuid4())]), headers=_csrf(client))
    assert stranger.status_code == 422

    removed = client.delete(f"/api/v1/alerts/{alert['id']}", headers=_csrf(client))
    assert removed.status_code == 204
    assert client.get(f"/api/v1/alerts/{alert['id']}").status_code == 404


def test_members_without_alerts_manage_only_see_what_they_receive(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    ana_id = ana.get("/api/v1/auth/me").json()["user"]["id"]
    owner_id = me["user"]["id"]
    mine = client.post("/api/v1/alerts", json=_form([owner_id]), headers=_csrf(client)).json()
    shared = client.post(
        "/api/v1/alerts", json=_form([owner_id, ana_id], name="Com a Ana"), headers=_csrf(client)
    ).json()

    listed = ana.get("/api/v1/alerts").json()
    assert [item["id"] for item in listed["items"]] == [shared["id"]]
    assert listed["items"][0]["editable"] is False
    assert ana.get(f"/api/v1/alerts/{mine['id']}").status_code == 404
    denied = ana.post("/api/v1/alerts", json=_form([ana_id]), headers=_csrf(ana))
    assert denied.status_code == 403
    assert denied.json()["error"]["code"] == "permission_denied"
    preview = ana.post(
        "/api/v1/alerts/preview", json={"definition": _definition()}, headers=_csrf(ana)
    )
    assert preview.status_code == 403
    edit = ana.put(f"/api/v1/alerts/{shared['id']}", json=_form([ana_id]), headers=_csrf(ana))
    assert edit.status_code == 403
    assert ana.delete(f"/api/v1/alerts/{shared['id']}", headers=_csrf(ana)).status_code == 403


def test_groone_alerts_preview_every_client(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from tests.test_internal import _staff

    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    staff = _staff(client, engine)
    staff_id = staff.get("/api/v1/auth/me").json()["user"]["id"]
    definition = _definition("revenue_groone")
    definition["query"]["dimensions"] = ["client"]
    definition["value"] = "1000000"
    preview = staff.post(
        "/api/v1/alerts/preview", json={"definition": definition}, headers=_csrf(staff)
    )
    assert preview.status_code == 200, preview.text
    created = staff.post(
        "/api/v1/alerts", json=_form([staff_id], definition=definition), headers=_csrf(staff)
    )
    assert created.status_code == 201, created.text
