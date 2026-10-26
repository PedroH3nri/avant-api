"""Catálogo de métricas e consultas de relatório contra o Postgres."""

import csv
import io
import uuid
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.domain import ConnectionType, Contract, Network, Site
from avant_core.metrics.domain import GamCounts, GamDailyMetric
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_team import _member_client

NOW = datetime.now(UTC)
YESTERDAY = NOW.date() - timedelta(days=1)


def _metrics(engine: Engine, company_id: uuid.UUID) -> dict[str, uuid.UUID]:
    """Uma network com dois sites e um dia de métricas em cada, mais uma linha sem site."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "123", ConnectionType.SERVICE_ACCOUNT, NOW)
        uow.networks.add(network)
        uow.contracts.add(Contract(company_id, network.id, Decimal("20"), NOW))
        acai = Site(company_id, "acai.com.br", network.id, "s1", NOW, "APPROVED")
        blog = Site(company_id, "=blog.com", network.id, "s2", NOW, "APPROVED")
        for site in (acai, blog):
            uow.sites.add(site)
        rows = [
            _row(company_id, network.id, YESTERDAY, acai.id, 10_000_000, 1000, "BR"),
            _row(company_id, network.id, YESTERDAY, blog.id, 30_000_000, 3000, "US"),
            _row(company_id, network.id, YESTERDAY, None, 5_000_000, 500, "BR"),
            _row(
                company_id, network.id, YESTERDAY - timedelta(days=1), acai.id, 2_000_000, 100, "BR"
            ),
        ]
        uow.gam_metrics.upsert_daily(rows)
        uow.commit()
        return {"network": network.id, "acai": acai.id, "blog": blog.id}


def _row(
    company_id: uuid.UUID,
    network_id: uuid.UUID,
    day: date,
    site_id: uuid.UUID | None,
    revenue: int,
    impressions: int,
    country: str,
) -> GamDailyMetric:
    """Uma linha diária com a receita bruta (o contrato ativo dá 20% para a Groone)."""
    return GamDailyMetric(
        company_id=company_id,
        network_id=network_id,
        date=day,
        ad_unit_path=f"{site_id}/{country}",
        country_code=country,
        device="desktop",
        revenue_micros=revenue,
        counts=GamCounts(impressions=impressions, clicks=impressions // 100),
        synced_at=NOW,
        site_id=site_id,
    )


def _day(dimensions: list[str] | None = None, **extra: object) -> dict[str, object]:
    """Consulta de ontem com receita, impressões e eCPM."""
    body: dict[str, object] = {
        "metrics": ["revenue", "impressions", "ecpm"],
        "period": {"start": YESTERDAY.isoformat(), "end": YESTERDAY.isoformat()},
        "dimensions": dimensions or [],
    }
    body.update(extra)
    return body


def test_catalog_hides_internal_metrics(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    response = client.get("/api/v1/metrics/catalog")
    assert response.status_code == 200, response.text
    catalog = response.json()
    keys = {metric["key"] for metric in catalog["metrics"]}
    assert {"revenue", "ecpm", "ctr"} <= keys and "revenue_gross" not in keys
    revenue = next(metric for metric in catalog["metrics"] if metric["key"] == "revenue")
    assert revenue["label"] == {"pt": "Receita", "en": "Revenue", "es": "Ingresos"}
    date_dimension = next(item for item in catalog["dimensions"] if item["key"] == "date")
    assert date_dimension["filterable"] is False


def test_query_totals_rows_and_member_sites(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    ids = _metrics(engine, uuid.UUID(me["active_company_id"]))

    response = client.post(
        "/api/v1/reports/query",
        json=_day(["site"], order=[{"field": "revenue"}], compare=True),
        headers=_csrf(client),
    )
    assert response.status_code == 200, response.text
    result = response.json()
    assert result["totals"] == {"revenue": "36", "impressions": "4500", "ecpm": "8.000000"}
    assert [row["dimensions"]["site"] for row in result["rows"]] == [
        str(ids["blog"]),
        str(ids["acai"]),
        None,
    ]
    assert result["labels"]["site"][str(ids["acai"])] == "acai.com.br"
    assert result["previous_totals"]["revenue"] == "1.6"
    assert result["rows"][1]["previous"]["impressions"] == "100"

    ana = _member_client(client, mailer, "ana@acai.com")
    assert (
        ana.post("/api/v1/reports/query", json=_day(), headers=_csrf(ana)).json()["totals"][
            "revenue"
        ]
        == "0"
    )
    ana_id = next(
        member["id"]
        for member in client.get("/api/v1/members").json()["items"]
        if member["user"]["name"] == "Ana"
    )
    assigned = client.put(
        f"/api/v1/members/{ana_id}/sites",
        json={"site_ids": [str(ids["acai"])]},
        headers=_csrf(client),
    )
    assert assigned.status_code == 200, assigned.text
    totals = ana.post("/api/v1/reports/query", json=_day(), headers=_csrf(ana)).json()["totals"]
    assert totals["revenue"] == "8" and totals["impressions"] == "1000"


def test_query_refuses_bad_definitions_and_internal_metrics(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    for body in (
        _day(metrics=["revenue_gross"]),
        _day(["custom_key"]),
        _day(period={"start": "2024-01-01", "end": YESTERDAY.isoformat()}),
        _day(filters=[{"field": "site", "operator": "eq", "values": ["x"]}]),
    ):
        response = client.post("/api/v1/reports/query", json=body, headers=_csrf(client))
        assert response.status_code == 422, response.text
        assert response.json()["error"]["code"] == "invalid_input"
    invalid = client.post("/api/v1/reports/query", json=_day(limit=0), headers=_csrf(client)).json()
    assert invalid["error"]["code"] == "validation_error"


def test_query_needs_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    ana_id = next(
        member["id"]
        for member in client.get("/api/v1/members").json()["items"]
        if member["user"]["name"] == "Ana"
    )
    denied_role = client.post(
        "/api/v1/roles",
        json={"name": "Sem relatórios", "permissions": ["sites.view"]},
        headers=_csrf(client),
    )
    assert denied_role.status_code == 201, denied_role.text
    changed = client.patch(
        f"/api/v1/members/{ana_id}",
        json={"role_id": denied_role.json()["id"]},
        headers=_csrf(client),
    )
    assert changed.status_code == 200, changed.text
    for response in (
        ana.get("/api/v1/metrics/catalog"),
        ana.post("/api/v1/reports/query", json=_day(), headers=_csrf(ana)),
        ana.post("/api/v1/reports/query/export", json=_day(), headers=_csrf(ana)),
    ):
        assert response.status_code == 403
        assert response.json()["error"]["code"] == "permission_denied"


def test_export_csv_uses_names_and_escapes_formulas(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    response = client.post(
        "/api/v1/reports/query/export?locale=en",
        json=_day(["site"], order=[{"field": "revenue"}]),
        headers=_csrf(client),
    )
    assert response.status_code == 200, response.text
    assert response.headers["content-type"].startswith("text/csv")
    rows = list(csv.reader(io.StringIO(response.text)))
    assert rows[0] == ["Site", "Revenue", "Impressions", "eCPM"]
    assert rows[1] == ["'=blog.com", "24", "3000", "8"]
    assert rows[2] == ["acai.com.br", "8", "1000", "8"]
    assert rows[3] == ["", "4", "500", "8"]


def test_reports_rate_limit(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    statuses = [
        client.post("/api/v1/reports/query", json=_day(), headers=_csrf(client)).status_code
        for _ in range(12)
    ]
    assert statuses[:10] == [200] * 10 and statuses[-1] == 429


def test_page_views_query_by_hour(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from avant_core.metrics.domain import PageViewHourly

    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    ids = _metrics(engine, company_id)
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        uow.page_views.upsert_hourly(
            [
                PageViewHourly(
                    company_id,
                    ids["network"],
                    "acai.com.br",
                    YESTERDAY,
                    hour,
                    "Brazil",
                    views,
                    NOW,
                    site_id=ids["acai"],
                )
                for hour, views in ((9, 120), (10, 80))
            ]
        )
        uow.commit()

    catalog = client.get("/api/v1/metrics/catalog").json()
    page_views = next(metric for metric in catalog["metrics"] if metric["key"] == "page_views")
    assert page_views["sources"] == ["page_views"]
    hour = next(item for item in catalog["dimensions"] if item["key"] == "hour")
    assert hour["sources"] == ["page_views"] and hour["filterable"] is False

    body = _day(["hour"], source="page_views", metrics=["page_views"])
    response = client.post("/api/v1/reports/query", json=body, headers=_csrf(client))
    assert response.status_code == 200, response.text
    result = response.json()
    assert result["totals"] == {"page_views": "200"}
    assert [
        (row["dimensions"]["hour"], row["metrics"]["page_views"]) for row in result["rows"]
    ] == [
        ("9", "120"),
        ("10", "80"),
    ]
    mixed = client.post(
        "/api/v1/reports/query",
        json=_day(source="page_views", metrics=["revenue"]),
        headers=_csrf(client),
    )
    assert mixed.status_code == 422 and mixed.json()["error"]["code"] == "invalid_input"


def test_display_currency_and_query_in_another_currency(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from avant_core.money.application import store_exchange_rates
    from avant_core.shared.clock import SystemClock

    me = _onboard_owner(client, engine, mailer)
    assert me["display_currency"] == "USD"
    company_id = uuid.UUID(me["active_company_id"])
    _metrics(engine, company_id)

    currencies = {item["code"]: item for item in client.get("/api/v1/currencies").json()}
    assert currencies["USD"]["available"] is True and currencies["BRL"]["available"] is False
    unavailable = client.post(
        "/api/v1/reports/query", json=_day(currency="BRL"), headers=_csrf(client)
    )
    assert unavailable.status_code == 409
    assert unavailable.json()["error"]["code"] == "currency_unavailable"

    store_exchange_rates(
        SqlAlchemyUnitOfWork(engine, bypass_rls=True),
        day=YESTERDAY,
        rates={"BRL": Decimal("5")},
        clock=SystemClock(),
    )
    assert client.get("/api/v1/currencies").json()[1]["available"] is True
    saved = client.put(
        "/api/v1/auth/preferences", json={"display_currency": "brl"}, headers=_csrf(client)
    )
    assert saved.status_code == 200 and saved.json() == {"display_currency": "BRL"}
    assert client.get("/api/v1/auth/me").json()["display_currency"] == "BRL"
    wrong = client.put(
        "/api/v1/auth/preferences", json={"display_currency": "XAU"}, headers=_csrf(client)
    )
    assert wrong.status_code == 422 and wrong.json()["error"]["code"] == "unsupported_currency"

    result = client.post("/api/v1/reports/query", json=_day(currency="BRL"), headers=_csrf(client))
    assert result.status_code == 200, result.text
    assert result.json()["currency"] == "BRL"
    assert result.json()["totals"]["revenue"] == "180"
    in_dollars = client.post("/api/v1/reports/query", json=_day(), headers=_csrf(client)).json()
    assert in_dollars["currency"] == "USD" and in_dollars["totals"]["revenue"] == "36"
