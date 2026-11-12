"""Regras de preço no painel do cliente, no interno e na rota pública dos floors contra o
Postgres: configuração do site, blocos, floor à mão, cache por site e hash e o país pelo IP."""

import os
import uuid
from datetime import UTC, date, datetime

import pytest
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import AdUnit
from avant_core.metrics.models import GamCounts, GamHourlyMetric
from avant_core.metrics.services import maintain_key_value_hourly_partitions
from avant_core.price_rules.catalog import CASCADE_CACHE_KEY, FLOOR_CACHE_KEY
from avant_core.price_rules.enums import (
    BlockKind,
    PriceRuleAction,
    PriceRuleModel,
    PriceRuleReason,
)
from avant_core.price_rules.models import PriceRule, PriceRuleHistoryEntry
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine

from avant_api.app import price_cascade_cache as service_module
from avant_api.app.container import Services
from avant_api.app.countries import FixedCountries
from tests.conftest import CapturingMailer, browser
from tests.test_ad_tags import CONTENT, _site
from tests.test_api import PASSWORD, _csrf, _onboard_owner
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
    visitor = browser(client.app)
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
    return site_id, key, browser(client.app)


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
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        for rule in uow.price_rules.list_for_site(site_id):
            rule.floor_micros = 2_000_000
        uow.commit()
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


CASCADE_BLOCK_PATH = "blog.com/Blog_Anchor_Mobile_20261028"


def _company_of(engine: Engine, site_id: uuid.UUID) -> uuid.UUID:
    """A Empresa dona do site."""
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        site = uow.sites.get(site_id)
        assert site is not None
        return site.company_id


def _try_hours(engine: Engine, site_id: uuid.UUID, day: date) -> None:
    """Duas horas da groone_try no Anchor_Mobile do Brasil: tentativas 1 e 3 com números."""
    company_id = _company_of(engine, site_id)
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
                custom_key="groone_try",
                custom_value=attempt,
                ad_unit_path=CASCADE_BLOCK_PATH,
                country_code="BR",
                currency="USD",
                revenue_micros=400_000,
                counts=GamCounts(impressions=10, eligible_requests=100, responses_served=50),
                synced_at=NOW,
                site_id=site_id,
            )
            for hour in (8, 9)
            for attempt in ("1", "3")
        ]
        uow.gam_key_value_hourly.replace(network_id, [day], rows)
        uow.commit()


def test_cascade_hours_return_four_tries_per_hour(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    company_id = _company_of(engine, site_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = client.get(base, params={"model": "cascade"}).json()["items"][0]["id"]
    today = datetime.now(UTC).date()
    _try_hours(engine, site_id, today)
    period = {"start": today.isoformat(), "end": today.isoformat()}
    rows = client.get(f"{base}/{rule_id}/cascade-hours", params=period).json()
    assert [row["hour"] for row in rows] == [9, 8]
    assert rows[0]["floor_micros"] == 0 and rows[0]["date"] == today.isoformat()
    assert [try_["eligible_requests"] for try_ in rows[0]["tries"]] == [100, 0, 100, 0]
    assert [try_["impressions"] for try_ in rows[0]["tries"]] == [10, 0, 10, 0]
    assert set(rows[0]["tries"][0]) == {
        "eligible_requests",
        "responses_served",
        "impressions",
        "revenue_micros",
    }
    assert client.get(f"{base}/{rule_id}/hours", params=period).status_code == 404
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get(f"{base}/{rule_id}/cascade-hours", params=period).status_code == 403
    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    assert client.get(f"{internal}/{rule_id}/cascade-hours", params=period).status_code == 403
    staff = _staff(client, engine)
    staff_rows = staff.get(f"{internal}/{rule_id}/cascade-hours", params=period)
    assert staff_rows.status_code == 200 and len(staff_rows.json()) == 2
    assert staff.get(f"{internal}/{rule_id}/hours", params=period).status_code == 404
    automatic = _rule(engine, company_id, site_id)
    missing = client.get(f"{base}/{automatic}/cascade-hours", params=period)
    assert missing.status_code == 404
    assert "error" in missing.json()
    assert staff.get(f"{internal}/{automatic}/cascade-hours", params=period).status_code == 404


def test_model_filter_and_field_on_rules(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    company_id = _company_of(engine, site_id)
    _rule(engine, company_id, site_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    everything = client.get(base).json()["items"]
    assert sorted(item["model"] for item in everything) == ["automatic", "cascade"]
    cascade = client.get(base, params={"model": "cascade"}).json()["items"]
    assert [item["model"] for item in cascade] == ["cascade"]
    automatic = client.get(base, params={"model": "automatic"}).json()["items"]
    assert [item["model"] for item in automatic] == ["automatic"]
    assert client.get(base, params={"model": "outro"}).status_code == 422
    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    staff = _staff(client, engine)
    staff_cascade = staff.get(internal, params={"model": "cascade"}).json()["items"]
    assert [item["model"] for item in staff_cascade] == ["cascade"]


def _offerwall_unit(engine: Engine, site_id: uuid.UUID) -> None:
    """Põe um bloco Offerwall no site, que não recebe regra."""
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        site = uow.sites.get(site_id)
        assert site is not None and site.network_id is not None
        name = "Blog_Offerwall_20261028"
        uow.ad_units.add(
            AdUnit(
                site.company_id,
                site.network_id,
                "t9",
                name,
                NOW,
                ad_unit_code=name,
                site_id=site_id,
            )
        )
        uow.commit()


def test_blocks_accept_both_models_and_recommend_one(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    _offerwall_unit(engine, site_id)
    staff = _staff(client, engine)
    bases = [
        (client, f"/api/v1/sites/{site_id}/price-rules"),
        (staff, f"/api/v1/internal/sites/{site_id}/price-rules"),
    ]
    for caller, base in bases:
        view = caller.get(f"{base}/settings").json()
        assert view["available_blocks"] == ["Anchor_Mobile", "Content3", "Offerwall"]
        assert view["recommended_models"] == {"Anchor_Mobile": "cascade", "Content3": "automatic"}
        swapped = {"Anchor_Mobile": "automatic", "Content3": "cascade"}
        saved = caller.put(f"{base}/blocks", json={"blocks": swapped}, headers=_csrf(caller))
        assert saved.status_code == 200, saved.text
        assert saved.json()["blocks"] == [
            {"block": "Anchor_Mobile", "model": "automatic"},
            {"block": "Content3", "model": "cascade"},
        ]
        assert saved.json()["recommended_models"] == view["recommended_models"]
        refused = caller.put(
            f"{base}/blocks", json={"blocks": {"Offerwall": "automatic"}}, headers=_csrf(caller)
        )
        assert refused.status_code == 422
        assert "error" in refused.json()


def _config(**changes: object) -> dict[str, object]:
    """O corpo do PUT da config, com os valores da Cascata e os ajustes pedidos."""
    body: dict[str, object] = {
        "pmr_floor": 60,
        "pmr_emergency": 30,
        "min_eligible_requests": 100,
        "floor_min_micros": 100_000,
        "floor_max_micros": 5_000_000,
        "step_size": 1,
        "automatic": True,
    }
    body.update(changes)
    return body


def test_config_drop_tiers_keeps_stored_value_when_omitted(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = client.get(base, params={"model": "cascade"}).json()["items"][0]["id"]
    url = f"{base}/{rule_id}/config"
    first = client.put(url, json=_config(), headers=_csrf(client))
    assert first.status_code == 200, first.text
    assert first.json()["config"]["drop_tiers"] == 2
    three = client.put(url, json=_config(drop_tiers=3), headers=_csrf(client))
    assert three.json()["config"]["drop_tiers"] == 3
    kept = client.put(url, json=_config(pmr_floor=55), headers=_csrf(client))
    assert kept.json()["config"]["drop_tiers"] == 3
    assert kept.json()["config"]["pmr_floor"] == 55.0
    one = client.put(url, json=_config(drop_tiers=1), headers=_csrf(client))
    assert one.json()["config"]["drop_tiers"] == 1
    assert client.get(f"{base}/{rule_id}").json()["config"]["drop_tiers"] == 1
    for invalid in (4, 0):
        refused = client.put(url, json=_config(drop_tiers=invalid), headers=_csrf(client))
        assert refused.status_code == 422
    internal = f"/api/v1/internal/sites/{site_id}/price-rules/{rule_id}/config"
    staff = _staff(client, engine)
    staff_three = staff.put(internal, json=_config(drop_tiers=3), headers=_csrf(staff))
    assert staff_three.json()["config"]["drop_tiers"] == 3
    staff_kept = staff.put(internal, json=_config(pmr_floor=50), headers=_csrf(staff))
    assert staff_kept.json()["config"]["drop_tiers"] == 3


def test_history_serialises_cascade_reasons(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    company_id = _company_of(engine, site_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = uuid.UUID(client.get(base, params={"model": "cascade"}).json()["items"][0]["id"])
    today = datetime.now(UTC)
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        for hour, reason in enumerate(
            (PriceRuleReason.FILLS_FIRST, PriceRuleReason.FILLS_LATE, PriceRuleReason.NO_NEW_DATA)
        ):
            uow.price_rules.save_history(
                PriceRuleHistoryEntry(
                    company_id=company_id,
                    rule_id=rule_id,
                    date=today.date(),
                    hour=hour,
                    action=PriceRuleAction.HOLD,
                    reason=reason,
                    floor_before_micros=1_220_000,
                    floor_applied_micros=1_220_000,
                    created_at=today,
                    data_date=today.date() if hour == 0 else None,
                    data_hour=7 if hour == 0 else None,
                )
            )
        uow.commit()
    period = {"start": today.date().isoformat(), "end": today.date().isoformat()}
    history = client.get(f"{base}/{rule_id}/history", params=period)
    by_reason = {entry["reason"]: entry for entry in history.json()}
    assert sorted(by_reason) == ["fills_first", "fills_late", "no_new_data"]
    assert by_reason["fills_first"]["data_date"] == today.date().isoformat()
    assert by_reason["fills_first"]["data_hour"] == 7
    assert by_reason["no_new_data"]["data_date"] is None
    assert by_reason["no_new_data"]["data_hour"] is None


def _seed_caches(client: TestClient, site_id: uuid.UUID, *hashes: str) -> tuple[str, list[str]]:
    """Põe a escada e os floors dos hashes no cache; devolve as duas chaves."""
    cascade_key = CASCADE_CACHE_KEY.format(site_id=site_id)
    floor_keys = [FLOOR_CACHE_KEY.format(site_id=site_id, content_hash=item) for item in hashes]
    _cache(client).values[cascade_key] = "{}"
    for key in floor_keys:
        _cache(client).values[key] = "{}"
    return cascade_key, floor_keys


def _present(client: TestClient, cascade_key: str, floor_keys: list[str]) -> tuple[bool, bool]:
    """Se a escada e os floors ainda estão no cache."""
    values = _cache(client).values
    return cascade_key in values, all(key in values for key in floor_keys)


def test_cascade_rule_changes_forget_only_the_cascades(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = client.get(base, params={"model": "cascade"}).json()["items"][0]["id"]
    staff = _staff(client, engine)
    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    calls = [
        (client, f"{base}/{rule_id}/floor", "put", {"floor_micros": 1_050_000}),
        (client, f"{base}/{rule_id}", "patch", {"status": "paused"}),
        (client, f"{base}/{rule_id}/config", "put", _config()),
        (staff, f"{internal}/{rule_id}/floor", "put", {"floor_micros": 1_130_000}),
        (staff, f"{internal}/{rule_id}", "patch", {"status": "active"}),
        (staff, f"{internal}/{rule_id}/config", "put", _config()),
    ]
    for caller, url, verb, body in calls:
        cascade_key, floor_keys = _seed_caches(client, site_id, HASH)
        response = getattr(caller, verb)(url, json=body, headers=_csrf(caller))
        assert response.status_code == 200, (url, response.text)
        assert _present(client, cascade_key, floor_keys) == (False, True), url


def test_automatic_rule_changes_forget_only_the_floors(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    company_id = _company_of(engine, site_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = _rule(engine, company_id, site_id)
    staff = _staff(client, engine)
    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    calls = [
        (client, f"{base}/{rule_id}/floor", "put", {"floor_micros": 1_050_000}),
        (client, f"{base}/{rule_id}", "patch", {"status": "paused"}),
        (client, f"{base}/{rule_id}/config", "put", _config()),
        (staff, f"{internal}/{rule_id}/floor", "put", {"floor_micros": 1_130_000}),
        (staff, f"{internal}/{rule_id}", "patch", {"status": "active"}),
        (staff, f"{internal}/{rule_id}/config", "put", _config()),
    ]
    for caller, url, verb, body in calls:
        cascade_key, floor_keys = _seed_caches(client, site_id, HASH)
        response = getattr(caller, verb)(url, json=body, headers=_csrf(caller))
        assert response.status_code == 200, (url, response.text)
        assert _present(client, cascade_key, floor_keys) == (True, False), url


def test_blocks_and_settings_forget_floors_and_cascades(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    company_id = _company_of(engine, site_id)
    _rule(engine, company_id, site_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    internal = f"/api/v1/internal/sites/{site_id}/price-rules"
    staff = _staff(client, engine)
    blocks = {"blocks": {"Anchor_Mobile": "cascade", "Content3": "automatic"}}
    settings = {"active": True, "control_percent": 20}
    calls = [
        (client, f"{base}/blocks", blocks),
        (client, f"{base}/settings", settings),
        (staff, f"{internal}/blocks", blocks),
        (staff, f"{internal}/settings", settings),
    ]
    for caller, url, body in calls:
        cascade_key, floor_keys = _seed_caches(client, site_id, HASH, "")
        response = caller.put(url, json=body, headers=_csrf(caller))
        assert response.status_code == 200, (url, response.text)
        assert _present(client, cascade_key, floor_keys) == (False, False), url
    _offerwall_unit(engine, site_id)
    cascade_key, floor_keys = _seed_caches(client, site_id, HASH)
    refused = client.put(
        f"{base}/blocks",
        json={"blocks": {"Offerwall": "automatic"}},
        headers=_csrf(client),
    )
    assert refused.status_code == 422
    assert _present(client, cascade_key, floor_keys) == (True, True)


def test_config_save_needs_manage_without_view(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, _, _ = _cascade_site(client, engine, mailer, "BR")
    base = f"/api/v1/sites/{site_id}/price-rules"
    rule_id = client.get(base, params={"model": "cascade"}).json()["items"][0]["id"]
    url = f"{base}/{rule_id}/config"
    stored = client.put(url, json=_config(drop_tiers=3), headers=_csrf(client))
    assert stored.json()["config"]["drop_tiers"] == 3
    role = client.post(
        "/api/v1/roles",
        json={"name": "Só edita", "permissions": ["price_rules.manage"], "site_scope": "all"},
        headers=_csrf(client),
    )
    assert role.status_code == 201, role.text
    invited = client.post(
        "/api/v1/invitations",
        json={"email": "edita@acai.com", "role_id": role.json()["id"]},
        headers=_csrf(client),
    )
    assert invited.status_code == 201, invited.text
    editor = browser(client.app)
    accepted = editor.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Edita", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    assert editor.get(f"{base}/{rule_id}").status_code == 403
    kept = editor.put(url, json=_config(pmr_floor=45), headers=_csrf(editor))
    assert kept.status_code == 200, kept.text
    assert kept.json()["config"]["drop_tiers"] == 3
    explicit = editor.put(url, json=_config(drop_tiers=1), headers=_csrf(editor))
    assert explicit.status_code == 200, explicit.text
    assert explicit.json()["config"]["drop_tiers"] == 1
