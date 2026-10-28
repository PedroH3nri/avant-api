"""Métricas personalizadas contra o Postgres: CRUD, conferência, catálogo e consulta."""

from datetime import UTC, datetime

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_costs_results import _marketing_client

RPM = {"name": "RPM por clique", "formula": "revenue / clicks * 1000", "format": "currency"}


def test_custom_metrics_crud_check_catalog_and_query(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    marketing = _marketing_client(client, mailer)

    created = client.post("/api/v1/custom-metrics", json=RPM, headers=_csrf(client))
    assert created.status_code == 201, created.text
    metric = created.json()
    assert (metric["key"], metric["query_key"]) == ("rpm_por_clique", "custom.rpm_por_clique")
    assert (metric["decimals"], metric["sources"]) == (2, ["gam", "gam_key_values"])

    forbidden = marketing.post("/api/v1/custom-metrics", json=RPM, headers=_csrf(marketing))
    assert forbidden.status_code == 403
    listed = marketing.get("/api/v1/custom-metrics").json()["items"]
    assert [item["key"] for item in listed] == ["rpm_por_clique"]

    bad = client.post(
        "/api/v1/custom-metrics",
        json={**RPM, "name": "Quebrada", "formula": "revenue_gross / 2"},
        headers=_csrf(client),
    )
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_formula"

    check = client.post(
        "/api/v1/custom-metrics/validate",
        json={**RPM, "formula": "revenue / page_views * 1000"},
        headers=_csrf(client),
    ).json()
    assert check == {
        "valid": True,
        "code": None,
        "error": None,
        "variables": ["page_views", "revenue"],
        "value": None,
    }
    broken = client.post(
        "/api/v1/custom-metrics/validate",
        json={**RPM, "formula": "revenue $ 2"},
        headers=_csrf(client),
    ).json()
    assert broken["valid"] is False and broken["code"] == "invalid_formula"
    assert "posição 9" in broken["error"]

    double = client.post(
        "/api/v1/custom-metrics",
        json={"name": "Dobro", "formula": "custom.rpm_por_clique * 2", "format": "number"},
        headers=_csrf(client),
    )
    assert double.status_code == 201, double.text
    renamed = client.put(
        f"/api/v1/custom-metrics/{metric['id']}",
        json={**RPM, "name": "RPM", "decimals": 4},
        headers=_csrf(client),
    )
    assert renamed.status_code == 200, renamed.text
    assert (renamed.json()["key"], renamed.json()["decimals"]) == ("rpm_por_clique", 4)
    in_use = client.delete(f"/api/v1/custom-metrics/{metric['id']}", headers=_csrf(client))
    assert in_use.status_code == 409
    assert in_use.json()["error"]["code"] == "custom_metric_in_use"

    catalog = client.get("/api/v1/metrics/catalog").json()
    assert [item["query_key"] for item in catalog["custom_metrics"]] == [
        "custom.dobro",
        "custom.rpm_por_clique",
    ]
    assert "page_rpm" in {item["key"] for item in catalog["metrics"]}

    today = datetime.now(UTC).date().isoformat()
    result = client.post(
        "/api/v1/reports/query",
        json={
            "metrics": ["custom.rpm_por_clique", "page_rpm"],
            "period": {"start": today, "end": today},
        },
        headers=_csrf(client),
    )
    assert result.status_code == 200, result.text
    assert result.json()["totals"] == {"custom.rpm_por_clique": None, "page_rpm": None}

    gone = client.delete(f"/api/v1/custom-metrics/{double.json()['id']}", headers=_csrf(client))
    assert gone.status_code == 204
