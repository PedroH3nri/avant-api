"""Rotas públicas do reward contra o Postgres: configuração com cache, ícone, eventos e
contatos no buffer, CORS e limite por IP."""

import json
import uuid

import pytest
import redis
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.price_rules.catalog import CASCADE_CACHE_KEY
from avant_core.price_rules.enums import BlockKind, PriceRuleModel
from avant_core.price_rules.models import PriceRule
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app import price_cascade_cache
from avant_api.app.container import Services
from avant_api.app.countries import FixedCountries
from avant_api.app.reward_cache import RedisRewardCache, reward_cache_key
from avant_api.modules.reward_public import service as reward_service
from tests.conftest import CapturingMailer, browser
from tests.fakes import MemoryRewardBuffer
from tests.test_api import _csrf, _onboard_owner
from tests.test_company_image import _png
from tests.test_rewards import NOW, _body, _cache, _site

PAGE = "https://www.blog.com/receitas/bolo?utm_source=x"
ORIGIN = {"Origin": "https://blog.com"}
EMPTY_PAGE = {"reward": None, "price_rules": None}


def _buffer(client: TestClient) -> MemoryRewardBuffer:
    """O buffer em memória da aplicação de teste."""
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    assert isinstance(services.reward_events, MemoryRewardBuffer)
    return services.reward_events


def test_public_config_is_cached_and_cleared(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    site_id = _site(engine, uuid.UUID(me["active_company_id"]))
    visitor = browser(client.app)
    empty = visitor.get("/api/reward/v2", params={"url": PAGE})
    assert empty.status_code == 200 and empty.json() == EMPTY_PAGE
    assert empty.headers["access-control-allow-origin"] == "*"
    key = reward_cache_key("blog.com", "receitas/bolo")
    assert json.loads(_cache(client).values[key]) == EMPTY_PAGE

    created = client.post("/api/v1/rewards", json=_body(site_id), headers=_csrf(client)).json()
    client.put(
        f"/api/v1/rewards/{created['id']}/icon",
        content=_png(32, 32),
        headers={**_csrf(client), "Content-Type": "image/png"},
    )
    config = visitor.get("/api/reward/v2", params={"url": PAGE}).json()["reward"]
    assert config["id"] == created["id"] and config["trigger"] == "load"
    assert config["ad_units"] == {
        "desktop": ["/2100/blog.com/Blog_Rewards_Desktop_20261028"],
        "mobile": ["/2100/blog.com/Blog_Rewards_Mobile_20261028"],
    }
    assert config["questions"][0]["answers"] == ["Cenoura", "Chocolate", "Fubá"]
    assert config["questions"][0]["id"] == created["questions"][0]["id"]
    assert config["lead"]["kind"] == "email"
    base = client.app.state.services.settings.app_base_url  # type: ignore[attr-defined]
    assert config["icon"]["url"].startswith(f"{base}/api/reward/icon/{created['id']}?v=")
    icon = visitor.get(config["icon"]["url"].removeprefix(base))
    assert icon.status_code == 200 and icon.headers["content-type"] == "image/webp"
    assert key in _cache(client).values

    client.patch(f"/api/v1/rewards/{created['id']}", json={"active": False}, headers=_csrf(client))
    assert key not in _cache(client).values
    assert visitor.get("/api/reward/v2", params={"url": PAGE}).json() == EMPTY_PAGE
    assert visitor.get("/api/reward/v2", params={"url": "javascript:alert(1)"}).json() == EMPTY_PAGE


def test_icon_route_has_the_ip_limit(client: TestClient) -> None:
    """Ícone que não existe é 404, e uma enxurrada de ids aleatórios do mesmo IP leva 429."""
    visitor = browser(client.app)
    codes = [visitor.get(f"/api/reward/icon/{uuid.uuid4()}").status_code for _ in range(25)]
    assert codes[0] == 404
    assert 429 in codes


class _BrokenRedis:
    """Um cliente Redis que sempre falha, como o Redis fora do ar."""

    def get(self, key: str) -> None:
        """Falha na leitura."""
        raise redis.ConnectionError("fora do ar")

    def set(self, *args: object, **kwargs: object) -> None:
        """Falha na escrita."""
        raise redis.ConnectionError("fora do ar")

    def delete(self, *keys: str) -> None:
        """Falha ao apagar."""
        raise redis.ConnectionError("fora do ar")


def test_cache_down_does_not_break_the_page_or_the_save() -> None:
    """Com o Redis fora, a leitura vem vazia e gravar ou apagar só registra."""
    cache = RedisRewardCache(_BrokenRedis())  # type: ignore[arg-type]
    assert cache.get("avant:reward:blog.com/a") is None
    cache.set("avant:reward:blog.com/a", "{}", 60)
    cache.delete("avant:reward:blog.com/a")


def test_events_and_leads_go_to_the_buffer(client: TestClient) -> None:
    visitor = browser(client.app)
    reward_id, question_id = str(uuid.uuid4()), str(uuid.uuid4())
    events = {
        "events": [
            {"reward_id": reward_id, "kind": "open"},
            {"reward_id": reward_id, "kind": "answer", "question_id": question_id, "answer": 2},
        ]
    }
    sent = visitor.post(
        "/api/reward/events",
        content=json.dumps(events),
        headers={**ORIGIN, "Content-Type": "text/plain", "Sec-Fetch-Site": "cross-site"},
    )
    assert sent.status_code == 202, sent.text
    assert sent.headers["access-control-allow-origin"] == "https://blog.com"
    first, second = (json.loads(item) for item in _buffer(client).items)
    assert first["type"] == "event" and first["kind"] == "open" and len(first["day"]) == 10
    assert (second["question_id"], second["answer"]) == (question_id, 2)
    bad = visitor.post("/api/reward/events", json={"events": [{"reward_id": "x", "kind": "open"}]})
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "validation_error"
    preflight = visitor.options("/api/reward/leads", headers=ORIGIN)
    assert preflight.status_code == 204

    lead = {
        "reward_id": reward_id,
        "name": " Ana ",
        "contact": "Ana@Email.com",
        "language": "pt-BR",
        "answers": [{"question_id": question_id, "answer": 1}],
    }
    accepted = visitor.post(
        "/api/reward/leads", json=lead, headers={"Sec-Fetch-Site": "cross-site"}
    )
    assert accepted.status_code == 202, accepted.text
    stored = json.loads(_buffer(client).items[-1])
    assert (stored["name"], stored["contact"], stored["language"]) == ("Ana", "ana@email.com", "pt")
    assert stored["answers"] == [{"question_id": question_id, "answer": 1}]
    repeated = [{"question_id": question_id, "answer": 1}] * 2
    twice = {**lead, "answers": repeated}
    assert visitor.post("/api/reward/leads", json=twice).status_code == 422
    invalid = visitor.post("/api/reward/leads", json={**lead, "contact": "123"})
    assert invalid.status_code == 422
    limited = [visitor.post("/api/reward/leads", json=lead).status_code for _ in range(4)]
    assert 429 in limited


LADDER = ["3.31", "3.08", "2.86"]


def _cascade_reward(
    client: TestClient, engine: Engine, mailer: CapturingMailer, *, active: bool = True
) -> tuple[uuid.UUID, TestClient]:
    """Site em dólar com a regra, o Rewards_Mobile em Cascata no Brasil e um reward na página."""
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    site_id = _site(engine, company_id)
    base = f"/api/v1/sites/{site_id}/price-rules"
    client.put(
        f"{base}/settings", json={"active": active, "control_percent": 10}, headers=_csrf(client)
    )
    blocks = client.put(
        f"{base}/blocks", json={"blocks": {"Rewards_Mobile": "cascade"}}, headers=_csrf(client)
    )
    assert blocks.status_code == 200, blocks.text
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        settings = uow.price_rule_settings.get(site_id)
        assert settings is not None
        settings.currency = "USD"
        uow.price_rules.add(
            PriceRule(
                company_id=company_id,
                site_id=site_id,
                content_hash="",
                block="Rewards_Mobile",
                kind=BlockKind.REWARD,
                country_code="BR",
                currency="USD",
                created_at=NOW,
                updated_at=NOW,
                floor_micros=3_310_000,
                model=PriceRuleModel.CASCADE,
            )
        )
        uow.commit()
    created = client.post("/api/v1/rewards", json=_body(site_id), headers=_csrf(client))
    assert created.status_code == 201, created.text
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    services.countries = FixedCountries({"testclient": "BR"})
    return site_id, browser(client.app)


def test_reward_page_has_cascade_for_rewards_block(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, visitor = _cascade_reward(client, engine, mailer)
    body = visitor.get("/api/reward/v2", params={"url": PAGE}).json()
    assert body["reward"] is not None
    assert body["price_rules"] == {"control_percent": 10, "cascades": {"Rewards_Mobile": LADDER}}
    header = visitor.get("/api/reward/v2", params={"url": PAGE}).headers["cache-control"]
    assert header.startswith("private")
    assert CASCADE_CACHE_KEY.format(site_id=site_id) in _cache(client).values
    assert "site_id" not in body["reward"] and "site_id" not in body
    again = visitor.get("/api/reward/v2", params={"url": PAGE}).json()
    assert again == body


def test_reward_page_has_no_cascade_for_other_country(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _, visitor = _cascade_reward(client, engine, mailer)
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    services.countries = FixedCountries({"testclient": "MX"})
    body = visitor.get("/api/reward/v2", params={"url": PAGE}).json()
    assert body["price_rules"] == {"control_percent": 10, "cascades": {}}


def test_reward_page_price_rules_null_when_site_off(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _, visitor = _cascade_reward(client, engine, mailer, active=False)
    body = visitor.get("/api/reward/v2", params={"url": PAGE}).json()
    assert body["reward"] is not None and body["price_rules"] is None


def test_reward_page_without_reward_stays_empty(client: TestClient) -> None:
    visitor = browser(client.app)
    assert visitor.get("/api/reward/v2", params={"url": PAGE}).json() == EMPTY_PAGE


def test_reward_page_survives_cascade_failure(
    client: TestClient,
    engine: Engine,
    mailer: CapturingMailer,
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
) -> None:
    site_id, visitor = _cascade_reward(client, engine, mailer)

    def broken(*args: object, **kwargs: object) -> dict[str, dict[str, list[str]]]:
        """Simula a falha do banco na busca da escada."""
        raise RuntimeError("banco fora")

    monkeypatch.setattr(price_cascade_cache, "public_price_cascades", broken)
    response = visitor.get("/api/reward/v2", params={"url": PAGE})
    assert response.status_code == 200
    body = response.json()
    assert body["reward"] is not None
    assert body["price_rules"] == {"control_percent": 10, "cascades": {}}
    assert "falha ao buscar a escada da Cascata" in caplog.text
    assert CASCADE_CACHE_KEY.format(site_id=site_id) not in _cache(client).values


def test_reward_page_survives_price_rules_failure(
    client: TestClient,
    engine: Engine,
    mailer: CapturingMailer,
    monkeypatch: pytest.MonkeyPatch,
    caplog: pytest.LogCaptureFixture,
) -> None:
    _, visitor = _cascade_reward(client, engine, mailer)

    def broken(*args: object, **kwargs: object) -> int | None:
        """Simula a falha do banco na leitura da regra de preço."""
        raise RuntimeError("banco fora")

    monkeypatch.setattr(reward_service, "public_control_percent", broken)
    response = visitor.get("/api/reward/v2", params={"url": PAGE})
    assert response.status_code == 200
    body = response.json()
    assert body["reward"] is not None and body["price_rules"] is None
    assert "falha ao ler a regra de preço" in caplog.text
    assert reward_cache_key("blog.com", "receitas/bolo") not in _cache(client).values


def test_reward_page_ignores_malformed_cascade_cache(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    site_id, visitor = _cascade_reward(client, engine, mailer)
    for invalid in (
        '{"BR": 5}',
        '{"BR": {"Rewards_Mobile": 5}}',
        '{"BR": {"Rewards_Mobile": [1]}}',
    ):
        _cache(client).values[CASCADE_CACHE_KEY.format(site_id=site_id)] = invalid
        response = visitor.get("/api/reward/v2", params={"url": PAGE})
        assert response.status_code == 200
        assert response.json()["price_rules"]["cascades"] == {"Rewards_Mobile": LADDER}
