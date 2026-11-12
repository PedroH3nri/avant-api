"""Fakes em memória dos adaptadores da API, só para os testes: o ``Services`` de produção
não tem nenhum padrão, e a fábrica ``memory_services`` do conftest monta estes."""

import asyncio
import math
import threading
import time
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from typing import Any

from avant_api.app.limits import BucketResult, BucketRule


class MemoryCounter:
    def __init__(self) -> None:
        self._data: dict[str, tuple[int, float]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> tuple[int, int]:
        """Devolve as tentativas na janela e os segundos que faltam para ela acabar."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            left = until - time.monotonic()
            return (count, math.ceil(left)) if left > 0 else (0, 0)

    def incr(self, key: str, window_seconds: int) -> tuple[int, int]:
        """Soma uma tentativa, abrindo a janela se for a primeira; devolve como get."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            now = time.monotonic()
            if until <= now:
                count, until = 0, now + window_seconds
            self._data[key] = (count + 1, until)
            return count + 1, math.ceil(until - now)

    def reserve(self, entries: list[tuple[str, int, int]]) -> int:
        """Confere todas as chaves e só soma se nenhuma estiver no limite, sob a mesma trava."""
        with self._lock:
            now = time.monotonic()
            for key, limit, _ in entries:
                count, until = self._data.get(key, (0, 0.0))
                if until > now and count >= limit:
                    return max(math.ceil(until - now), 1)
            for key, _, window_seconds in entries:
                count, until = self._data.get(key, (0, 0.0))
                if until <= now:
                    count, until = 0, now + window_seconds
                self._data[key] = (count + 1, until)
            return 0

    def decr(self, key: str) -> None:
        """Devolve uma tentativa reservada, sem passar de zero."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            if count > 0:
                self._data[key] = (count - 1, until)

    def delete(self, key: str) -> None:
        """Zera o contador."""
        with self._lock:
            self._data.pop(key, None)


class MemoryBucket:
    """Testes: o balde em memória, um por processo."""

    def __init__(self) -> None:
        self._tokens: dict[str, tuple[float, float]] = {}
        self._denied: dict[str, tuple[int, float]] = {}
        self._blocked: dict[str, float] = {}
        self._lock = threading.Lock()

    def take(self, subject: str, rule: BucketRule, now: float) -> BucketResult:
        """Tira uma ficha do balde do sujeito, ou diz quanto esperar."""
        with self._lock:
            until = self._blocked.get(subject, 0.0)
            if until > now:
                return BucketResult(False, 0, math.ceil(until - now))
            tokens, ts = self._tokens.get(subject, (float(rule.burst), now))
            tokens = min(float(rule.burst), tokens + (now - ts) * rule.rate)
            if tokens >= 1:
                self._tokens[subject] = (tokens - 1, now)
                return BucketResult(True, math.floor(tokens - 1), 0)
            self._tokens[subject] = (tokens, now)
            count, start = self._denied.get(subject, (0, now))
            if now - start >= 60:
                count, start = 0, now
            count += 1
            self._denied[subject] = (count, start)
            if count > rule.abuse_limit:
                self._blocked[subject] = now + rule.block_seconds
                self._denied.pop(subject, None)
                return BucketResult(False, 0, rule.block_seconds)
            return BucketResult(False, 0, math.ceil((1 - tokens) / rule.rate))


@dataclass
class RecordingQueue:
    """Testes: guarda o que seria enfileirado."""

    sent: list[tuple[str, tuple[Any, ...]]] = field(default_factory=list)
    offline: bool = False

    def send(self, name: str, *args: Any) -> bool:
        """Guarda a tarefa em memória, para os testes conferirem; ``offline`` simula a fila fora do
        ar."""
        if self.offline:
            return False
        self.sent.append((name, args))
        return True


class NoEvents:
    """Testes: a conexão fica aberta só com o heartbeat, sem evento."""

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Nunca tem evento: só entrega None a cada tempo limite."""
        while True:
            await asyncio.sleep(timeout)
            yield None


@dataclass
class MemoryKeyValueBuffer:
    """Testes: as networks conectadas e o buffer em memória."""

    connected: set[str] = field(default_factory=set)
    buffered: dict[str, set[str]] = field(default_factory=dict)

    def is_connected(self, network_code: str) -> bool:
        """Diz se a network está no conjunto em memória."""
        return network_code in self.connected

    def push(self, network_code: str, pairs: set[str]) -> None:
        """Guarda os pares em memória."""
        self.buffered.setdefault(network_code, set()).update(pairs)


@dataclass
class MemoryRewardCache:
    """Testes: o cache em memória, sem prazo."""

    values: dict[str, str] = field(default_factory=dict)

    def get(self, key: str) -> str | None:
        """Lê da memória."""
        return self.values.get(key)

    def set(self, key: str, value: str, ttl_seconds: int) -> None:
        """Grava na memória."""
        self.values[key] = value

    def delete(self, *keys: str) -> None:
        """Apaga da memória."""
        for key in keys:
            self.values.pop(key, None)


@dataclass
class MemoryRewardBuffer:
    """Testes: a lista em memória."""

    items: list[str] = field(default_factory=list)

    def push(self, items: list[str]) -> bool:
        """Guarda na memória."""
        self.items.extend(items)
        return bool(items)
