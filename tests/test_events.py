"""SSE: o gerador direto (sem rede) e a rota com uma fonte que termina."""

import asyncio
import json
import os
import uuid
from collections.abc import AsyncIterator
from dataclasses import dataclass

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.events import RedisEvents, channel, sse
from tests.conftest import CapturingMailer
from tests.test_api import _onboard_owner
from tests.test_team import _member_client

REDIS_URL = os.environ.get("AVANT_TEST_REDIS_URL")


@dataclass
class ListEvents:
    """Entrega o que tem e termina, para a resposta acabar."""

    items: list[str | None]
    seen_channel: str | None = None

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        self.seen_channel = channel
        for item in self.items:
            yield item


def _event(type_: str, **data: str) -> str:
    return json.dumps({"type": type_, "data": data})


async def _collect(source: ListEvents, can: set[str], **kw: float) -> list[str]:
    return [
        chunk
        async for chunk in sse(source, company_id=uuid.UUID(int=1), can=can.__contains__, **kw)
    ]


def test_stream_filters_by_permission_and_sends_heartbeats() -> None:
    source = ListEvents(
        [
            _event("network.updated", network_id="n1"),
            None,
            _event("segredo.qualquer", x="y"),  # tipo desconhecido nunca sai
            "isto não é json",
        ]
    )
    chunks = asyncio.run(_collect(source, {"network.view"}))
    assert chunks == [
        "retry: 5000\n\n",
        'event: network.updated\ndata: {"network_id": "n1"}\n\n',
        ": ping\n\n",
    ]
    assert source.seen_channel == channel(uuid.UUID(int=1))

    without = asyncio.run(_collect(ListEvents([_event("network.updated", network_id="n1")]), set()))
    assert without == ["retry: 5000\n\n"]


def test_stream_closes_after_the_limit() -> None:
    source = ListEvents([None, None, None])
    chunks = asyncio.run(_collect(source, set(), max_seconds=0))
    assert chunks == ["retry: 5000\n\n", ": ping\n\n"]


def test_redis_source_delivers_published_messages() -> None:
    if not REDIS_URL:
        pytest.skip("defina AVANT_TEST_REDIS_URL")
    import redis

    async def run() -> list[str | None]:
        got: list[str | None] = []
        source = RedisEvents(REDIS_URL or "")
        stream = source.listen("avant:events:teste", timeout=0.2)
        got.append(await anext(stream))  # nada ainda: heartbeat
        redis.Redis.from_url(REDIS_URL or "").publish("avant:events:teste", "oi")
        got.append(await anext(stream))
        await stream.aclose()  # type: ignore[attr-defined]
        return got

    assert asyncio.run(run()) == [None, "oi"]


def test_events_route(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    assert TestClient(client.app).get("/api/v1/events").status_code == 401
    me = _onboard_owner(client, engine, mailer)
    source = ListEvents([_event("network.updated", network_id="n1")])
    client.app.state.services.events = source  # type: ignore[attr-defined]

    r = client.get("/api/v1/events")
    assert r.status_code == 200 and r.headers["content-type"].startswith("text/event-stream")
    assert r.headers["x-accel-buffering"] == "no"
    assert 'event: network.updated\ndata: {"network_id": "n1"}' in r.text
    assert source.seen_channel == f"avant:events:{me['active_company_id']}"

    # Financeiro tem network.view; sem a permissão o evento não sairia (teste acima).
    ana = _member_client(client, mailer, "ana@acai.com")
    assert "network.updated" in ana.get("/api/v1/events").text
