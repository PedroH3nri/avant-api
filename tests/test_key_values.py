"""Key-values que a g-tag manda dos sites dos clientes (o /admanager/keyvalue do Genius)."""

import os

import pytest
import redis
from fastapi.testclient import TestClient

from avant_api.app.key_value_buffer import (
    BUFFER,
    CONNECTED,
    PENDING_NETWORKS,
    MemoryKeyValueBuffer,
    RedisKeyValueBuffer,
)
from avant_api.app.security import CROSS_SITE_PATHS

PATH = "/api/admanager/keyvalue"
GROONE = "22893970961"


def _buffer(client: TestClient) -> MemoryKeyValueBuffer:
    """O buffer em memória da aplicação de teste, com a 2100 e a Groone conectadas."""
    buffer = client.app.state.services.key_values  # type: ignore[attr-defined]
    assert isinstance(buffer, MemoryKeyValueBuffer)
    buffer.connected.update({"2100", GROONE})
    return buffer


def test_clean_values_of_connected_networks_go_to_the_buffer(client: TestClient) -> None:
    buffer = _buffer(client)
    sent = client.post(
        PATH,
        json=[
            {"name": "utm_source", "value": "fb", "network": "2100"},
            {"name": "land_uri", "value": "/receitas/bolo", "network": f"{GROONE},5566"},
            {"name": "utm_campaign", "value": "a" * 41, "network": "2100"},
            {"name": "utm_source", "value": "face(book)", "network": "2100"},
            {"name": "utm_id", "value": "1", "network": "2100"},
            {"name": "utm_source", "value": "ig", "network": "9999"},
        ],
        headers={"Sec-Fetch-Site": "cross-site", "Origin": "https://blog.com"},
    )
    assert sent.status_code == 202, sent.text
    assert sent.headers["Access-Control-Allow-Origin"] == "https://blog.com"
    assert sent.headers["Access-Control-Allow-Credentials"] == "true"
    assert buffer.buffered == {"2100": {"utm_source:fb"}, GROONE: {"land_uri:/receitas/bolo"}}


def test_the_preflight_answers_with_cors(client: TestClient) -> None:
    preflight = client.options(
        PATH,
        headers={"Origin": "https://blog.com", "Access-Control-Request-Method": "POST"},
    )
    assert preflight.status_code == 204
    assert preflight.headers["Access-Control-Allow-Origin"] == "https://blog.com"
    assert preflight.headers["Access-Control-Allow-Credentials"] == "true"
    assert preflight.headers["Vary"] == "Origin"
    assert "POST" in preflight.headers["Access-Control-Allow-Methods"]
    assert "Content-Type" in preflight.headers["Access-Control-Allow-Headers"]


def test_four_requests_per_second_per_ip(client: TestClient) -> None:
    _buffer(client)
    item = [{"name": "utm_source", "value": "fb", "network": "2100"}]
    answers = [client.post(PATH, json=item).status_code for _ in range(5)]
    assert answers == [202, 202, 202, 202, 429]


def test_only_this_route_accepts_writes_from_another_site() -> None:
    assert frozenset({PATH}) == CROSS_SITE_PATHS


@pytest.mark.skipif("AVANT_TEST_REDIS_URL" not in os.environ, reason="defina AVANT_TEST_REDIS_URL")
def test_redis_buffer_follows_the_worker_contract() -> None:
    client = redis.Redis.from_url(os.environ["AVANT_TEST_REDIS_URL"])
    for key in (CONNECTED, PENDING_NETWORKS, BUFFER.format(network="2100")):
        client.delete(key)
    buffer = RedisKeyValueBuffer(client)
    assert not buffer.is_connected("2100")
    client.sadd(CONNECTED, "2100")
    assert buffer.is_connected("2100")
    buffer.push("2100", {"utm_source:fb", "land_uri:/a"})
    assert client.smembers(PENDING_NETWORKS) == {b"2100"}
    assert client.smembers(BUFFER.format(network="2100")) == {b"utm_source:fb", b"land_uri:/a"}
