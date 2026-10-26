"""Avisos em tempo real (SSE). O avant-worker publica no Redis, qualquer instância da API
repassa; por isso funciona com várias instâncias e no blue-green.

Contrato, igual ao do worker: canal ``avant:events:{company_id}``, mensagem JSON
``{"type": "network.updated", "data": {"network_id": "..."}}``. O evento só diz o que
mudou: a tela busca o estado pela rota de sempre, que confere a permissão de novo.
"""

import asyncio
import json
import logging
import uuid
from collections.abc import AsyncIterator, Callable
from typing import Protocol

import redis.asyncio as aioredis

log = logging.getLogger("avant.api.events")

# Tipo de evento -> permissão para recebê-lo. O que não está aqui não sai.
PERMISSION_FOR = {
    "network.updated": "network.view",
}
HEARTBEAT_SECONDS = 15
# Depois disso o servidor fecha; o EventSource reconecta e a sessão é conferida de novo.
MAX_STREAM_SECONDS = 30 * 60
RETRY_MS = 5000


def channel(company_id: uuid.UUID) -> str:
    """Nome do canal do Redis com os eventos de uma Empresa."""
    return f"avant:events:{company_id}"


class EventSource(Protocol):
    def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Mensagens do canal; ``None`` quando passou ``timeout`` sem nada."""
        ...


class RedisEvents:
    def __init__(self, url: str) -> None:
        self._url = url

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Escuta o canal da Empresa e entrega cada evento, ou None no tempo limite."""
        client = aioredis.Redis.from_url(self._url)
        pubsub = client.pubsub()
        try:
            await pubsub.subscribe(channel)
            while True:
                message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=timeout)
                if message is None:
                    yield None
                elif message["type"] == "message":
                    data = message["data"]
                    yield data.decode() if isinstance(data, bytes) else str(data)
        finally:
            await pubsub.aclose()  # type: ignore[no-untyped-call]
            await client.aclose()


class NoEvents:
    """Sem Redis (local e testes): a conexão fica aberta só com o heartbeat."""

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Nunca tem evento: só entrega None a cada tempo limite."""
        while True:
            await asyncio.sleep(timeout)
            yield None


async def sse(
    source: EventSource,
    *,
    company_id: uuid.UUID,
    can: Callable[[str], bool],
    heartbeat: float = HEARTBEAT_SECONDS,
    max_seconds: float = MAX_STREAM_SECONDS,
) -> AsyncIterator[str]:
    """O corpo da resposta ``text/event-stream``."""
    loop = asyncio.get_running_loop()
    deadline = loop.time() + max_seconds
    yield f"retry: {RETRY_MS}\n\n"
    async for raw in source.listen(channel(company_id), timeout=heartbeat):
        if raw is None:
            yield ": ping\n\n"
        elif (event := _parse(raw)) is not None:
            type_, data = event
            permission = PERMISSION_FOR.get(type_)
            if permission is not None and can(permission):
                yield f"event: {type_}\ndata: {json.dumps(data)}\n\n"
        if loop.time() >= deadline:
            return


def _parse(raw: str) -> tuple[str, dict[str, object]] | None:
    """Lê um evento JSON do canal; o que vier estragado é ignorado."""
    try:
        event = json.loads(raw)
        type_, data = event["type"], event.get("data") or {}
    except (ValueError, KeyError, TypeError):
        log.warning("evento inválido no Redis", extra={"raw": raw[:200]})
        return None
    if not isinstance(type_, str) or not isinstance(data, dict):
        return None
    return type_, data
