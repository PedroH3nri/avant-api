"""Dashboards contra o Postgres: CRUD, padrão, escolha da pessoa e widgets."""

import uuid
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_reports import YESTERDAY, _metrics
from tests.test_team import _member_client


def _kpi(metric: str, widget_id: str = "kpi") -> dict[str, Any]:
    """Widget de KPI de ontem, com a consulta no formato salvo."""
    day = YESTERDAY.isoformat()
    return {
        "id": widget_id,
        "type": "query",
        "x": 0,
        "y": 0,
        "w": 3,
        "h": 2,
        "chart_type": "kpi",
        "query": {
            "schema_version": 1,
            "source": "gam",
            "metrics": [metric],
            "period": {"preset": None, "start": day, "end": day},
            "dimensions": [],
            "filters": [],
            "compare": False,
            "order": [],
            "limit": 1000,
        },
    }


def _form(*widgets: dict[str, Any], **changes: Any) -> dict[str, Any]:
    """Um dashboard da Empresa inteira com os widgets dados."""
    body: dict[str, Any] = {
        "name": "Painel",
        "definition": {"schema_version": 1, "filters": {}, "widgets": list(widgets)},
        "visibility": "company",
    }
    body.update(changes)
    return body


def _template(key: str) -> str:
    """O id do modelo pronto que a migration semeou com a chave."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"avant:dashboard_template:{key}"))


def _run(client: TestClient, dashboard_id: str, widget_id: str = "kpi", **body: Any) -> Any:
    """Roda o widget e devolve a resposta."""
    return client.post(
        f"/api/v1/dashboards/{dashboard_id}/widgets/{widget_id}/run",
        json=body,
        headers=_csrf(client),
    )


def test_dashboards_of_a_client(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    ids = _metrics(engine, uuid.UUID(me["active_company_id"]))
    created = client.post("/api/v1/dashboards", json=_form(_kpi("revenue")), headers=_csrf(client))
    assert created.status_code == 201, created.text
    dashboard = created.json()
    assert dashboard["editable"] is True and dashboard["is_default"] is False
    ran = _run(client, dashboard["id"])
    assert ran.status_code == 200, ran.text
    assert ran.json()["totals"] == {"revenue": "36"}
    only_acai = _run(client, dashboard["id"], filters={"site": [str(ids["acai"])]})
    assert only_acai.json()["totals"] == {"revenue": "8"}

    templates = client.get("/api/v1/dashboards/templates").json()["items"]
    assert {item["key"] for item in templates} == {"overview", "by_site", "inventory_quality"}
    from_template = client.post(
        f"/api/v1/dashboards/templates/{_template('overview')}", headers=_csrf(client)
    )
    assert from_template.status_code == 201, from_template.text
    assert from_template.json()["visibility"] == "private"
    groone_only = client.post(
        f"/api/v1/dashboards/templates/{_template('groone_overview')}", headers=_csrf(client)
    )
    assert groone_only.status_code == 404

    empty_home = client.get("/api/v1/dashboards/home").json()
    assert empty_home["dashboard"] is None and empty_home["template"]["id"] == _template("overview")
    widgets = {item["id"]: item["type"] for item in empty_home["template"]["definition"]["widgets"]}
    assert widgets["account"] == "account"
    from_home = client.post(
        f"/api/v1/dashboards/templates/{_template('overview')}/widgets/revenue/run",
        json={},
        headers=_csrf(client),
    )
    assert from_home.status_code == 200, from_home.text
    assert set(from_home.json()["totals"]) == {"revenue"}
    other = client.post(
        f"/api/v1/dashboards/templates/{_template('groone_overview')}/widgets/revenue_groone/run",
        json={},
        headers=_csrf(client),
    )
    assert other.status_code == 404
    choice = {"dashboard_id": dashboard["id"]}
    marked = client.put("/api/v1/dashboards/default", json=choice, headers=_csrf(client))
    assert marked.status_code == 204, marked.text
    home = client.get("/api/v1/dashboards/home").json()["dashboard"]
    assert home["id"] == dashboard["id"] and home["is_default"] is True
    private = {"dashboard_id": from_template.json()["id"]}
    refused = client.put("/api/v1/dashboards/default", json=private, headers=_csrf(client))
    assert refused.status_code == 422

    listed = client.get("/api/v1/dashboards").json()
    assert listed["total"] == 2 and listed["default_id"] == dashboard["id"]
    assert listed["items"][0]["id"] == dashboard["id"]

    wrong = _form({**_kpi("revenue"), "x": 11})
    invalid = client.post("/api/v1/dashboards", json=wrong, headers=_csrf(client))
    assert invalid.status_code == 422
    assert invalid.json()["error"]["code"] == "invalid_input"


def test_members_see_shared_dashboards_but_need_manage_to_edit(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    shared = client.post("/api/v1/dashboards", json=_form(_kpi("revenue")), headers=_csrf(client))
    private = client.post(
        "/api/v1/dashboards",
        json=_form(_kpi("revenue"), visibility="private"),
        headers=_csrf(client),
    )
    shared_id, private_id = shared.json()["id"], private.json()["id"]
    ana = _member_client(client, mailer, "ana@acai.com")

    listed = ana.get("/api/v1/dashboards").json()
    assert [item["id"] for item in listed["items"]] == [shared_id]
    assert listed["items"][0]["editable"] is False
    assert ana.get(f"/api/v1/dashboards/{private_id}").status_code == 404
    assert _run(ana, shared_id).status_code == 200
    denied = ana.post("/api/v1/dashboards", json=_form(_kpi("revenue")), headers=_csrf(ana))
    assert denied.status_code == 403
    assert denied.json()["error"]["code"] == "permission_denied"
    edit = ana.put(f"/api/v1/dashboards/{shared_id}", json=_form(), headers=_csrf(ana))
    assert edit.status_code == 403
    assert ana.delete(f"/api/v1/dashboards/{shared_id}", headers=_csrf(ana)).status_code == 403

    chosen = ana.put(
        "/api/v1/dashboards/home", json={"dashboard_id": shared_id}, headers=_csrf(ana)
    )
    assert chosen.status_code == 204
    assert ana.get("/api/v1/dashboards/home").json()["dashboard"]["id"] == shared_id
    removed = client.delete(f"/api/v1/dashboards/{shared_id}", headers=_csrf(client))
    assert removed.status_code == 204
    assert ana.get("/api/v1/dashboards/home").json()["dashboard"] is None


def test_groone_dashboards_sum_every_client(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from tests.test_internal import _staff

    me = _onboard_owner(client, engine, mailer)
    company_id = me["active_company_id"]
    _metrics(engine, uuid.UUID(company_id))
    staff = _staff(client, engine)

    templates = staff.get("/api/v1/dashboards/templates").json()["items"]
    assert {item["key"] for item in templates} == {
        "groone_overview",
        "groone_by_manager",
        "groone_by_client",
    }
    created = staff.post(
        f"/api/v1/dashboards/templates/{_template('groone_overview')}", headers=_csrf(staff)
    )
    assert created.status_code == 201, created.text
    widgets = {item["id"]: item for item in created.json()["definition"]["widgets"]}
    assert widgets["goal"]["goal_scope"] == "team"

    groone = staff.post(
        "/api/v1/dashboards", json=_form(_kpi("revenue_groone")), headers=_csrf(staff)
    )
    assert groone.status_code == 201, groone.text
    everyone = _run(staff, groone.json()["id"])
    assert everyone.status_code == 200, everyone.text
    assert everyone.json()["totals"] == {"revenue_groone": "9"}
    nobody = _run(staff, groone.json()["id"], filters={"client": [str(uuid.uuid4())]})
    assert nobody.json()["totals"] == {"revenue_groone": "0"}
    goal = _run(staff, created.json()["id"], "goal")
    assert goal.status_code == 422

    by_client = {"client": [company_id]}
    refused = client.post(
        "/api/v1/dashboards",
        json=_form(_kpi("revenue"), definition={"schema_version": 1, "filters": by_client}),
        headers=_csrf(client),
    )
    assert refused.status_code == 422


def test_whole_dashboard_runs_in_one_request(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    ids = _metrics(engine, uuid.UUID(me["active_company_id"]))
    impressions = _kpi("impressions", "views")
    impressions["x"] = 3
    created = client.post(
        "/api/v1/dashboards", json=_form(_kpi("revenue"), impressions), headers=_csrf(client)
    ).json()
    ran = client.post(f"/api/v1/dashboards/{created['id']}/run", json={}, headers=_csrf(client))
    assert ran.status_code == 200, ran.text
    body = ran.json()
    assert body["results"]["kpi"]["totals"] == {"revenue": "36"}
    assert body["results"]["views"]["totals"] == {"impressions": "4500"} and body["errors"] == {}
    only_acai = client.post(
        f"/api/v1/dashboards/{created['id']}/run",
        json={"filters": {"site": [str(ids["acai"])]}},
        headers=_csrf(client),
    ).json()
    assert only_acai["results"]["kpi"]["totals"] == {"revenue": "8"}
    home = client.post(
        f"/api/v1/dashboards/templates/{_template('overview')}/run", json={}, headers=_csrf(client)
    )
    assert home.status_code == 200, home.text
    assert "revenue" in home.json()["results"]
    hidden = client.post(
        f"/api/v1/dashboards/templates/{_template('groone_overview')}/run",
        json={},
        headers=_csrf(client),
    )
    assert hidden.status_code == 404

    ana = _member_client(client, mailer, "ana@acai.com")
    ana_id = next(
        member["id"]
        for member in client.get("/api/v1/members").json()["items"]
        if member["user"]["name"] == "Ana"
    )
    role = client.post(
        "/api/v1/roles",
        json={"name": "Sem relatórios", "permissions": ["sites.view"]},
        headers=_csrf(client),
    ).json()
    client.patch(f"/api/v1/members/{ana_id}", json={"role_id": role["id"]}, headers=_csrf(client))
    denied = ana.post(f"/api/v1/dashboards/{created['id']}/run", json={}, headers=_csrf(ana))
    assert denied.status_code == 403
