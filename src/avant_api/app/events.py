"""Avisos em tempo real (SSE). O avant-worker publica no Redis, qualquer instância da API
repassa; por isso funciona com várias instâncias e no blue-green.

Contrato, igual ao do worker: canal ``avant:events:{company_id}``, mensagem JSON
``{"type": "network.updated", "data": {"network_id": "..."}}``. O evento só diz o que
mudou: a tela busca o estado pela rota de sempre, que confere a permissão de novo.

Cada processo tem um cliente Redis só e um teto de streams abertos, por pessoa e no total.
"""

import asyncio
import json
import logging
import threading
import uuid
from collections import Counter
from collections.abc import AsyncIterator, Callable
from typing import Protocol

import redis.asyncio as aioredis

from avant_api.app.errors import TooManyAttempts

log = logging.getLogger("avant.api.events")

# Tipo de evento -> permissão para recebê-lo. O que não está aqui não sai.
PERMISSION_FOR = {
    "network.updated": "network.view",
    "gam_tool_run.updated": "internal.gam_tools.view",
    "metrics.updated": "reports.view",
}
HEARTBEAT_SECONDS = 15
# Depois disso o servidor fecha; o EventSource reconecta e a sessão é conferida de novo.
MAX_STREAM_SECONDS = 30 * 60
RETRY_MS = 5000
# Abas abertas de uma pessoa e streams de um processo da API ao mesmo tempo.
EVENT_STREAMS_PER_USER = 5
EVENT_STREAMS_PER_PROCESS = 500


class StreamLimiter:
    """Conta os streams abertos neste processo e recusa com 429 quem passa do teto."""

    def __init__(
        self, per_user: int = EVENT_STREAMS_PER_USER, per_process: int = EVENT_STREAMS_PER_PROCESS
    ) -> None:
        self._per_user = per_user
        self._per_process = per_process
        self._open: Counter[uuid.UUID] = Counter()
        self._lock = threading.Lock()

    def acquire(self, user_id: uuid.UUID) -> None:
        """Reserva um stream para a pessoa, ou recusa quando ela ou o processo está no teto."""
        with self._lock:
            if (
                self._open[user_id] >= self._per_user
                or sum(self._open.values()) >= self._per_process
            ):
                raise TooManyAttempts("avisos em tempo real abertos demais", retry_after=30)
            self._open[user_id] += 1

    def release(self, user_id: uuid.UUID) -> None:
        """Devolve o stream que acabou."""
        with self._lock:
            self._open[user_id] -= 1
            if self._open[user_id] <= 0:
                del self._open[user_id]


def channel(company_id: uuid.UUID) -> str:
    """Nome do canal do Redis com os eventos de uma Empresa."""
    return f"avant:events:{company_id}"


class EventSource(Protocol):
    def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Mensagens do canal; ``None`` quando passou ``timeout`` sem nada."""
        ...


class RedisEvents:
    """Um cliente Redis por processo; cada stream só abre a própria inscrição no canal."""

    def __init__(self, url: str) -> None:
        self._url = url
        self._client: aioredis.Redis | None = None

    def _shared(self) -> aioredis.Redis:
        """O cliente do processo, criado no primeiro stream."""
        if self._client is None:
            self._client = aioredis.Redis.from_url(self._url)
        return self._client

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Escuta o canal da Empresa e entrega cada evento, ou None no tempo limite."""
        pubsub = self._shared().pubsub()
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
