"""Regras de preço no painel do cliente, no interno e na rota pública dos floors contra o
Postgres: configuração do site, blocos, floor à mão, cache por site e hash e o país pelo IP."""

import os
import uuid
from datetime import UTC, date, datetime

import pytest
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.metrics.models import GamCounts, GamHourlyMetric
from avant_core.metrics.services import maintain_key_value_hourly_partitions
from avant_core.price_rules.catalog import CASCADE_CACHE_KEY, FLOOR_CACHE_KEY
from avant_core.price_rules.enums import BlockKind, PriceRuleModel
from avant_core.price_rules.models import PriceRule
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine

from avant_api.app import price_cascade_cache as service_module
from avant_api.app.container import Services
from avant_api.app.countries import FixedCountries
from tests.conftest import CapturingMailer
from tests.test_ad_tags import CONTENT, _site
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_rewards import _cache
from tests.test_team import _member_client

NOW = datetime(2026, 11, 10, 12, tzinfo=UTC)
HASH = "0a1b2c3d4e5f6071"


def _rule(engine: Engine, company_id: uuid.UUID, site_id: uuid.UUID) -> uuid.UUID:
    """Uma regra no ar do Content3 no Brasil, em dólar, com floor de 0,50."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        rule = PriceRule(
            company_id=company_id,
            site_id=site_id,
            content_hash=HASH,
            block="Content3",
            kind=BlockKind.CONTENT,
            country_code="BR",
            currency="USD",
            created_at=NOW,
            updated_at=NOW,
            floor_micros=500_000,
        )
        uow.price_rules.add(rule)
        uow.commit()
        return rule.id


def _hours(engine: Engine, company_id: uuid.UUID, site_id: uuid.UUID, day: date) -> None:
    """Duas horas do GAM do hash no Content3 do Brasil, numa partição criada pelo dono."""
    owner = create_engine(os.environ["AVANT_TEST_MIGRATIONS_URL"])
    maintain_key_value_hourly_partitions(
        SqlAlchemyUnitOfWork(owner, bypass_rls=True), clock=SystemClock()
    )
    owner.dispose()
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        site = uow.sites.get(site_id)
        assert site is not None and site.network_id is not None
        network_id = site.network_id
        rows = [
            GamHourlyMetric(
                company_id=company_id,
                network_id=network_id,
                date=day,
                hour=hour,
                custom_key="content_hash",
                custom_value=HASH,
                ad_unit_path="blog.com/Blog_Content3_20261028",
                country_code="BR",
                currency="USD",
                revenue_micros=400_000,
                counts=GamCounts(impressions=100, eligible_requests=200, responses_served=150),
                synced_at=NOW,
                site_id=site_id,
            )
            for hour in (8, 9)
        ]
        uow.gam_key_value_hourly.replace(network_id, [day], rows)
        uow.commit()


def test_price_rules_panel_internal_and_public_floors(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    site_id = _site(engine, company_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get(f"{base}/settings").status_code == 403

    view = client.get(f"{base}/settings").json()
    assert view["active"] is False and view["control_percent"] == 10
    assert view["domain"] == "blog.com"
    assert view["available_blocks"] == ["Anchor_Mobile", "Content3"]
    wrong = client.put(
        f"{base}/settings", json={"active": True, "control_percent": 60}, headers=_csrf(client)
    )
    assert wrong.status_code == 422
    saved = client.put(
        f"{base}/settings", json={"active": True, "control_percent": 10}, headers=_csrf(client)
    )
    assert saved.status_code == 200, saved.text
    blocks = client.put(
        f"{base}/blocks", json={"blocks": {"Content3": "automatic"}}, headers=_csrf(client)
    )
    assert blocks.json()["blocks"] == [{"block": "Content3", "model": "automatic"}]

    rule_id = _rule(engine, company_id, site_id)
    listed = client.get(base, params={"country": "BR"}).json()
    assert [item["id"] for item in listed["items"]] == [str(rule_id)]
    details = client.get(f"{base}/{rule_id}").json()
    sites = client.get("/api/v1/price-rules/sites", params={"q": "blog"}).json()
    assert [
        (row["domain"], row["active"], row["automatic_blocks"], row["active_rules"])
        for row in sites["items"]
    ] == [("blog.com", True, 1, 1)]
    assert sites["items"][0]["client"] is None
    assert ana.get("/api/v1/price-rules/sites").status_code == 403
    assert details["floor_micros"] == 500_000 and details["config"] is None
    assert details["tiers_micros"][0] == 500_000 and len(details["tiers_micros"]) == 200

    created = client.post(
        "/api/v1/ad-tags",
        json={"site_id": str(site_id), "name": "Principal"},
        headers=_csrf(client),
    )
    tag_id, key = created.json()["id"], created.json()["key"]
    draft = {"blocks": [CONTENT], "settings": {"price_rules": True}}
    client.put(
        f"/api/v1/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": draft},
        headers=_csrf(client),
    )
    published = client.post(f"/api/v1/ad-tags/{tag_id}/publish", json={}, headers=_csrf(client))
    assert published.status_code == 200, published.text

    services: Services = client.app.state.services  # type: ignore[attr-defined]
    services.countries = FixedCountries({"testclient": "BR"})
    visitor = TestClient(client.app)
    page = {"key": key, "hash": HASH}
    floors = visitor.get("/api/tag/prices", params=page)
    assert floors.headers["access-control-allow-origin"] == "*"
    assert floors.json() == {"control_percent": 10, "floors": {"Content3": "0.50"}, "cascades": {}}
    cache_key = FLOOR_CACHE_KEY.format(site_id=site_id, content_hash=HASH)
    assert cache_key in _cache(client).values
    assert visitor.get("/api/tag/prices", params={"key": key, "hash": "x y"}).status_code == 422
    nothing = visitor.get("/api/tag/prices", params={"key": "tg_nada", "hash": HASH})
    assert nothing.json() == {"control_percent": None, "floors": {}, "cascades": {}}

    manual = client.put(
        f"{base}/{rule_id}/floor", json={"floor_micros": 1_000_000}, headers=_csrf(client)
    )
    assert manual.json()["floor_micros"] == 1_010_000
    assert cache_key not in _cache(client).values
    assert visitor.get("/api/tag/prices", params=page).json()["floors"] == {"Content3": "1.01"}
    today = datetime.now(UTC).date().isoformat()
    history = client.get(f"{base}/{rule_id}/history", params={"start": "2026-11-01", "end": today})
    assert [entry["reason"] for entry in history.json()] == ["manual"]
    _hours(engine, company_id, site_id, datetime.now(UTC).date())
    period = {"start": today, "end": today}
    hours = client.get(f"{base}/{rule_id}/hours", params=period).json()
    assert [(row["hour"], row["eligible_requests"], row["pmr"]) for row in hours] == [
        (9, 200, 75.0),
        (8, 200, 75.0),
    ]
    assert hours[0]["ecpm_micros"] == 4_000_000
    assert ana.get(f"{base}/{rule_id}/hours", params=period).status_code == 403
    paused = client.patch(f"{base}/{rule_id}", json={"status": "paused"}, headers=_csrf(client))
    assert paused.json()["status"] == "paused"
    assert visitor.get("/api/tag/prices", params=page).json()["floors"] == {}

    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    assert client.get(f"{internal}/settings").status_code == 403
    staff = _staff(client, engine)
    assert staff.get(f"{internal}/settings").json()["active"] is True
    staff_floor = staff.put(
        f"{internal}/{rule_id}/floor", json={"floor_micros": 500_000}, headers=_csrf(staff)
    )
    assert staff_floor.status_code == 200, staff_floor.text
    staff_sites = staff.get("/api/v1/internal/price-rules/sites", params={"q": "blog.com"})
    assert [row["client"] is not None for row in staff_sites.json()["items"]] == [True]
    assert client.get("/api/v1/internal/price-rules/sites").status_code == 403
    staff_hours = staff.get(f"{internal}/{rule_id}/hours", params=period)
    assert len(staff_hours.json()) == 2
    assert client.get(f"{internal}/{rule_id}/hours", params=period).status_code == 403


def _cascade_rule(
    engine: Engine, company_id: uuid.UUID, site_id: uuid.UUID, country_code: str
) -> uuid.UUID:
    """Uma regra Cascata do Anchor_Mobile no país, em dólar, com o ponto de partida em 1,22."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        rule = PriceRule(
            company_id=company_id,
            site_id=site_id,
            content_hash="",
            block="Anchor_Mobile",
            kind=BlockKind.ANCHOR,
            country_code=country_code,
            currency="USD",
            created_at=NOW,
            updated_at=NOW,
            floor_micros=1_220_000,
            model=PriceRuleModel.CASCADE,
        )
        uow.price_rules.add(rule)
        uow.commit()
        return rule.id


def _cascade_site(
    client: TestClient, engine: Engine, mailer: CapturingMailer, country_code: str
) -> tuple[uuid.UUID, str, TestClient]:
    """Site em dólar com a regra ligada, o Anchor_Mobile em Cascata, a tag no ar e o visitante no
    Brasil."""
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    site_id = _site(engine, company_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    client.put(
        f"{base}/settings", json={"active": True, "control_percent": 10}, headers=_csrf(client)
    )
    blocks = client.put(
        f"{base}/blocks", json={"blocks": {"Anchor_Mobile": "cascade"}}, headers=_csrf(client)
    )
    assert blocks.status_code == 200, blocks.text
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        settings = uow.price_rule_settings.get(site_id)
        assert settings is not None
        settings.currency = "USD"
        uow.commit()
    _cascade_rule(engine, company_id, site_id, country_code)
    created = client.post(
        "/api/v1/ad-tags",
        json={"site_id": str(site_id), "name": "Principal"},
        headers=_csrf(client),
    )
    tag_id, key = created.json()["id"], created.json()["key"]
    draft = {"blocks": [CONTENT], "settings": {"price_rules": True}}
    client.put(
        f"/api/v1/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": draft},
        headers=_csrf(client),
    )
    client.post(f"/api/v1/ad-tags/{tag_id}/publish", json={}, headers=_csrf(client))
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    services.countries = FixedCountries({"testclient": "BR"})
    return site_id, key, TestClient(client.app)


def test_prices_returns_cascade_ladder_for_country(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _, key, visitor = _cascade_site(client, engine, mailer, "BR")
    response = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert response.json()["cascades"] == {"Anchor_Mobile": ["1.22", "1.13", "1.05"]}
    assert response.json()["floors"] == {}


def test_prices_cascades_empty_without_rule_in_country(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, key, visitor = _cascade_site(client, engine, mailer, "MX")
    response = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert response.json()["cascades"] == {}
    assert CASCADE_CACHE_KEY.format(site_id=site_id) in _cache(client).values


def test_prices_cascades_cached_per_site(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, key, visitor = _cascade_site(client, engine, mailer, "BR")
    first = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert first.json()["cascades"] == {"Anchor_Mobile": ["1.22", "1.13", "1.05"]}
    assert CASCADE_CACHE_KEY.format(site_id=site_id) in _cache(client).values
    base = f"/api/v1/sites/{site_id}/price-rules"
    client.put(
        f"{base}/blocks", json={"blocks": {"Anchor_Mobile": "automatic"}}, headers=_csrf(client)
    )
    other = visitor.get("/api/tag/prices", params={"key": key, "hash": "ffffffffffffffff"})
    assert other.json()["cascades"] == {"Anchor_Mobile": ["1.22", "1.13", "1.05"]}


def test_prices_cascade_failure_keeps_floors(
    client: TestClient, engine: Engine, mailer: CapturingMailer, monkeypatch: pytest.MonkeyPatch
) -> None:
    site_id, key, visitor = _cascade_site(client, engine, mailer, "BR")

    def broken(*args: object, **kwargs: object) -> dict[str, dict[str, list[str]]]:
        """Simula a falha do banco na busca da escada."""
        raise RuntimeError("banco fora")

    monkeypatch.setattr(service_module, "public_price_cascades", broken)
    response = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert response.status_code == 200
    assert response.json() == {"control_percent": 10, "floors": {}, "cascades": {}}
    assert CASCADE_CACHE_KEY.format(site_id=site_id) not in _cache(client).values
    _cache(client).values[CASCADE_CACHE_KEY.format(site_id=site_id)] = "{quebrado"
    monkeypatch.undo()
    again = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert again.json()["cascades"] == {"Anchor_Mobile": ["1.22", "1.13", "1.05"]}


def test_prices_cascades_empty_when_price_rules_off(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, key, visitor = _cascade_site(client, engine, mailer, "BR")
    off = client.put(
        f"/api/v1/sites/{site_id}/price-rules/settings",
        json={"active": False, "control_percent": 10},
        headers=_csrf(client),
    )
    assert off.status_code == 200, off.text
    response = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
    assert response.json() == {"control_percent": None, "floors": {}, "cascades": {}}


def test_prices_cascades_cache_not_a_dict_is_a_miss(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, key, visitor = _cascade_site(client, engine, mailer, "BR")
    for invalid in ("[]", "null", "5", '"texto"'):
        _cache(client).values[CASCADE_CACHE_KEY.format(site_id=site_id)] = invalid
        response = visitor.get("/api/tag/prices", params={"key": key, "hash": HASH})
        assert response.status_code == 200
        assert response.json()["cascades"] == {"Anchor_Mobile": ["1.22", "1.13", "1.05"]}
