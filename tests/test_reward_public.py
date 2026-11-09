"""Rotas públicas do reward contra o Postgres: configuração com cache, ícone, eventos e
contatos no buffer, CORS e limite por IP."""

import json
import uuid

import redis
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.container import Services
from avant_api.app.reward_buffer import MemoryRewardBuffer
from avant_api.app.reward_cache import RedisRewardCache, reward_cache_key
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_company_image import _png
from tests.test_rewards import _body, _cache, _site

PAGE = "https://www.blog.com/receitas/bolo?utm_source=x"
ORIGIN = {"Origin": "https://blog.com"}


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
    visitor = TestClient(client.app)
    empty = visitor.get("/api/reward/v2", params={"url": PAGE})
    assert empty.status_code == 200 and empty.json() == {"reward": None}
    assert empty.headers["access-control-allow-origin"] == "*"
    key = reward_cache_key("blog.com", "receitas/bolo")
    assert json.loads(_cache(client).values[key]) == {"reward": None}

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
    assert visitor.get("/api/reward/v2", params={"url": PAGE}).json() == {"reward": None}
    assert visitor.get("/api/reward/v2", params={"url": "javascript:alert(1)"}).json() == {
        "reward": None
    }


def test_icon_route_has_the_ip_limit(client: TestClient) -> None:
    """Ícone que não existe é 404, e uma enxurrada de ids aleatórios do mesmo IP leva 429."""
    visitor = TestClient(client.app)
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
    visitor = TestClient(client.app)
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
