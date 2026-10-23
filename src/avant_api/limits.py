"""Limite de tentativas nas rotas sem sessão (login, esqueci a senha, redefinir).

Janela fixa: cada chave conta as tentativas que falharam e zera sozinha no fim da janela.
Em staging e produção os contadores ficam no Redis, valendo para todas as instâncias.
"""

import math
import threading
import time
from dataclasses import dataclass
from typing import Protocol

import redis

from avant_api.errors import TooManyAttempts


@dataclass(frozen=True)
class Rule:
    name: str
    limit: int
    window_seconds: int


LOGIN_EMAIL = Rule("login:email", 5, 15 * 60)
LOGIN_IP = Rule("login:ip", 20, 15 * 60)
PASSWORD_IP = Rule("password:ip", 20, 15 * 60)


class Counter(Protocol):
    def get(self, key: str) -> tuple[int, int]:
        """Tentativas na janela e segundos até ela acabar."""
        ...

    def incr(self, key: str, window_seconds: int) -> None: ...
    def delete(self, key: str) -> None: ...


class MemoryCounter:
    def __init__(self) -> None:
        self._data: dict[str, tuple[int, float]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> tuple[int, int]:
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            left = until - time.monotonic()
            return (count, math.ceil(left)) if left > 0 else (0, 0)

    def incr(self, key: str, window_seconds: int) -> None:
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            now = time.monotonic()
            if until <= now:
                count, until = 0, now + window_seconds
            self._data[key] = (count + 1, until)

    def delete(self, key: str) -> None:
        with self._lock:
            self._data.pop(key, None)


class RedisCounter:
    def __init__(self, client: redis.Redis) -> None:
        self._r = client

    @classmethod
    def from_url(cls, url: str) -> "RedisCounter":
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def get(self, key: str) -> tuple[int, int]:
        pipe = self._r.pipeline()
        pipe.get(key)
        pipe.ttl(key)
        raw, ttl = pipe.execute()
        return (int(raw or 0), max(int(ttl), 0))

    def incr(self, key: str, window_seconds: int) -> None:
        pipe = self._r.pipeline()
        pipe.incr(key)
        pipe.expire(key, window_seconds, nx=True)
        pipe.execute()

    def delete(self, key: str) -> None:
        self._r.delete(key)


class Limiter:
    def __init__(self, counter: Counter, prefix: str = "avant:limit") -> None:
        self._c = counter
        self._prefix = prefix

    def _key(self, rule: Rule, subject: str) -> str:
        return f"{self._prefix}:{rule.name}:{subject.lower()}"

    def check(self, *pairs: tuple[Rule, str | None]) -> None:
        """Antes de tentar: recusa com 429 quem já passou do limite em alguma das chaves."""
        for rule, subject in pairs:
            if subject is None:
                continue
            count, left = self._c.get(self._key(rule, subject))
            if count >= rule.limit:
                raise TooManyAttempts(retry_after=max(left, 1))

    def fail(self, *pairs: tuple[Rule, str | None]) -> None:
        for rule, subject in pairs:
            if subject is not None:
                self._c.incr(self._key(rule, subject), rule.window_seconds)

    def clear(self, rule: Rule, subject: str) -> None:
        self._c.delete(self._key(rule, subject))
