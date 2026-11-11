"""Limites: tentativas nas rotas sem sessão (login, esqueci a senha, redefinir), chaves de
API que não conferem (por IP) e requisições por chave de API.

Tentativas: janela fixa; cada chave conta as que falharam e zera sozinha no fim da janela.
Com ``attempt``, a tentativa é reservada antes (INCR atômico) e devolvida se não falhar, para
uma rajada em paralelo não passar do limite.
Chaves de API: balde de fichas (2 por segundo, rajada de 20).
Em staging e produção os contadores ficam no Redis, valendo para todas as instâncias.
"""

import math
import threading
import time
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Protocol

import redis

from avant_api.app.errors import TooManyAttempts


@dataclass(frozen=True)
class Rule:
    name: str
    limit: int
    window_seconds: int


LOGIN_EMAIL = Rule("login:email", 5, 15 * 60)
LOGIN_IP = Rule("login:ip", 20, 15 * 60)
PASSWORD_IP = Rule("password:ip", 20, 15 * 60)
# Senha atual na troca de senha, por pessoa.
PASSWORD_CHANGE = Rule("password:change", 5, 15 * 60)
# Códigos do 2FA no segundo passo do login, por IP; por pessoa, quem trava é o core.
MFA_IP = Rule("mfa:ip", 20, 15 * 60)
# Chave de API que não confere, por IP: passou do limite, a chave nem chega ao banco.
API_KEY_IP = Rule("api_key:ip", 20, 15 * 60)


class Counter(Protocol):
    def get(self, key: str) -> tuple[int, int]:
        """Tentativas na janela e segundos até ela acabar."""
        ...

    def incr(self, key: str, window_seconds: int) -> tuple[int, int]:
        """Soma uma tentativa, abrindo a janela se for a primeira; devolve como get."""
        ...

    def decr(self, key: str) -> None:
        """Devolve uma tentativa reservada, sem passar de zero."""
        ...

    def delete(self, key: str) -> None:
        """Zera o contador."""
        ...


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


# Devolve uma tentativa só se a chave ainda existe, para não criar chave sem prazo.
_DECR = """
local count = tonumber(redis.call('GET', KEYS[1]) or '0')
if count > 0 then redis.call('DECR', KEYS[1]) end
return 0
"""


class RedisCounter:
    def __init__(self, client: redis.Redis) -> None:
        self._redis = client
        self._decr = client.register_script(_DECR)

    @classmethod
    def from_url(cls, url: str) -> "RedisCounter":
        """Conecta ao Redis pela URL."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def get(self, key: str) -> tuple[int, int]:
        """Devolve as tentativas na janela e os segundos que faltam para ela acabar."""
        pipeline = self._redis.pipeline()
        pipeline.get(key)
        pipeline.ttl(key)
        raw, ttl = pipeline.execute()
        return (int(raw or 0), max(int(ttl), 0))

    def incr(self, key: str, window_seconds: int) -> tuple[int, int]:
        """Soma uma tentativa numa transação, abrindo a janela se for a primeira."""
        pipeline = self._redis.pipeline()
        pipeline.incr(key)
        pipeline.expire(key, window_seconds, nx=True)
        pipeline.ttl(key)
        count, _, ttl = pipeline.execute()
        return int(count), max(int(ttl), 0)

    def decr(self, key: str) -> None:
        """Devolve uma tentativa reservada, sem passar de zero."""
        self._decr(keys=[key])

    def delete(self, key: str) -> None:
        """Zera o contador."""
        self._redis.delete(key)


class Limiter:
    def __init__(self, counter: Counter, prefix: str = "avant:limit") -> None:
        self._counter = counter
        self._prefix = prefix

    def _key(self, rule: Rule, subject: str) -> str:
        """Monta a chave do contador de uma regra para um sujeito."""
        return f"{self._prefix}:{rule.name}:{subject.lower()}"

    def check(self, *pairs: tuple[Rule, str | None]) -> None:
        """Antes de tentar: recusa com 429 quem já passou do limite em alguma das chaves."""
        for rule, subject in pairs:
            if subject is None:
                continue
            count, left = self._counter.get(self._key(rule, subject))
            if count >= rule.limit:
                raise TooManyAttempts(retry_after=max(left, 1))

    def fail(self, *pairs: tuple[Rule, str | None]) -> None:
        """Conta uma falha em cada regra com sujeito."""
        for rule, subject in pairs:
            if subject is not None:
                self._counter.incr(self._key(rule, subject), rule.window_seconds)

    def clear(self, rule: Rule, subject: str) -> None:
        """Zera o contador de uma regra para um sujeito."""
        self._counter.delete(self._key(rule, subject))

    def reserve(self, *pairs: tuple[Rule, str | None]) -> None:
        """Conta a tentativa já, de forma atômica, e recusa com 429 quem passou do limite.

        A recusa não conta: devolve tudo o que reservou, para um IP no limite não gastar o e-mail.
        """
        reserved: list[tuple[Rule, str | None]] = []
        for rule, subject in pairs:
            if subject is None:
                continue
            count, left = self._counter.incr(self._key(rule, subject), rule.window_seconds)
            reserved.append((rule, subject))
            if count > rule.limit:
                self.release(*reserved)
                raise TooManyAttempts(retry_after=max(left, 1))

    def release(self, *pairs: tuple[Rule, str | None]) -> None:
        """Devolve a tentativa reservada em cada regra com sujeito."""
        for rule, subject in pairs:
            if subject is not None:
                self._counter.decr(self._key(rule, subject))

    @contextmanager
    def attempt(
        self, *pairs: tuple[Rule, str | None], counts: tuple[type[Exception], ...]
    ) -> Iterator[None]:
        """Reserva a tentativa antes de rodar; só fica contada se terminar num erro de counts."""
        self.reserve(*pairs)
        failed = False
        try:
            yield
        except counts:
            failed = True
            raise
        finally:
            if not failed:
                self.release(*pairs)


# --- Chaves de API: balde de fichas -----------------------------------------------------


@dataclass(frozen=True)
class BucketRule:
    # Quantas fichas voltam por segundo.
    rate: float
    burst: int
    # Quem insiste depois do 429 fica bloqueado: mais de ``abuse_limit`` recusas em um
    # minuto bloqueiam a chave por ``block_seconds``.
    abuse_limit: int
    block_seconds: int


API_KEY = BucketRule(rate=2.0, burst=20, abuse_limit=20, block_seconds=30)
# Consultas de relatório somam muitas linhas: um balde próprio por pessoa e Empresa.
REPORTS = BucketRule(rate=0.5, burst=10, abuse_limit=20, block_seconds=60)
# Key-values da g-tag (rota pública, beacon de cada página): 4 pedidos por segundo por IP.
KEY_VALUES = BucketRule(rate=4.0, burst=4, abuse_limit=40, block_seconds=60)
# Rewards (rotas públicas do script do site): configuração da página, eventos e contatos por IP.
REWARD_CONFIG = BucketRule(rate=5.0, burst=20, abuse_limit=60, block_seconds=60)
REWARD_EVENTS = BucketRule(rate=4.0, burst=10, abuse_limit=40, block_seconds=60)
REWARD_LEADS = BucketRule(rate=0.2, burst=3, abuse_limit=10, block_seconds=300)
TAG_CONFIG = BucketRule(rate=5.0, burst=20, abuse_limit=60, block_seconds=60)
# Uma página vista por página: o mesmo IP (NAT, escritório) pode mandar várias por segundo.
TAG_PAGE_VIEWS = BucketRule(rate=5.0, burst=20, abuse_limit=60, block_seconds=60)
# Um pedido de floors por página, como a configuração.
TAG_PRICES = BucketRule(rate=5.0, burst=20, abuse_limit=60, block_seconds=60)


@dataclass(frozen=True)
class BucketResult:
    allowed: bool
    remaining: int
    # Segundos até poder tentar de novo; 0 quando já pode.
    retry_after: int


class Bucket(Protocol):
    def take(self, subject: str, rule: BucketRule, now: float) -> BucketResult:
        """Tira uma ficha do balde do sujeito, ou diz quanto esperar."""
        ...


class MemoryBucket:
    """Para desenvolvimento e testes: cada processo tem o seu."""

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


# KEYS: fichas, recusas no minuto, bloqueio. ARGV: agora, taxa, rajada, limite, bloqueio.
_TAKE = """
local blocked = redis.call('TTL', KEYS[3])
if blocked > 0 then return {0, 0, blocked} end
local now, rate, burst = tonumber(ARGV[1]), tonumber(ARGV[2]), tonumber(ARGV[3])
local data = redis.call('HMGET', KEYS[1], 't', 'ts')
local tokens = tonumber(data[1]) or burst
local ts = tonumber(data[2]) or now
tokens = math.min(burst, tokens + math.max(now - ts, 0) * rate)
local ttl = math.ceil(burst / rate) + 1
if tokens >= 1 then
  redis.call('HSET', KEYS[1], 't', tostring(tokens - 1), 'ts', ARGV[1])
  redis.call('EXPIRE', KEYS[1], ttl)
  return {1, math.floor(tokens - 1), 0}
end
redis.call('HSET', KEYS[1], 't', tostring(tokens), 'ts', ARGV[1])
redis.call('EXPIRE', KEYS[1], ttl)
local denied = redis.call('INCR', KEYS[2])
if denied == 1 then redis.call('EXPIRE', KEYS[2], 60) end
if denied > tonumber(ARGV[4]) then
  redis.call('SET', KEYS[3], '1', 'EX', ARGV[5])
  redis.call('DEL', KEYS[2])
  return {0, 0, tonumber(ARGV[5])}
end
return {0, 0, math.ceil((1 - tokens) / rate)}
"""


class RedisBucket:
    """Vale para todas as instâncias da API. Um script só, para ser atômico."""

    def __init__(self, client: redis.Redis, prefix: str = "avant:bucket") -> None:
        self._take = client.register_script(_TAKE)
        self._prefix = prefix

    @classmethod
    def from_url(cls, url: str) -> "RedisBucket":
        """Conecta ao Redis pela URL."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def take(self, subject: str, rule: BucketRule, now: float) -> BucketResult:
        """Tira uma ficha do balde do sujeito num script Lua atômico, ou diz quanto esperar."""
        base = f"{self._prefix}:{subject}"
        keys = [f"{base}:tokens", f"{base}:denied", f"{base}:blocked"]
        args: list[str | float] = [
            repr(now),
            rule.rate,
            rule.burst,
            rule.abuse_limit,
            rule.block_seconds,
        ]
        allowed, remaining, retry_after = self._take(keys=keys, args=args)
        return BucketResult(bool(allowed), int(remaining), int(retry_after))
