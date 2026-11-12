"""Cache no Redis da configuração pública dos rewards, por página.

O contrato com o avant-worker (que apaga as chaves dos rewards em "mais recentes" quando a
importação traz ad units de reward novos): a chave é ``avant:reward:{domínio}/{caminho}``, com o
domínio sem ``www.`` e o caminho sem barras nas pontas. Página sem reward também fica no cache,
com o valor vazio, para o site não bater no banco a cada visita.
"""

import logging
from typing import Protocol

import redis

log = logging.getLogger("avant.api.reward_cache")

KEY = "avant:reward:{domain}/{path}"
TTL_SECONDS = 3600
EMPTY_TTL_SECONDS = 300


def reward_cache_key(domain: str, path: str) -> str:
    """A chave do cache da página."""
    return KEY.format(domain=domain, path=path)


class RewardCache(Protocol):
    def get(self, key: str) -> str | None:
        """O JSON guardado da página; vazio quando não está no cache."""
        ...

    def set(self, key: str, value: str, ttl_seconds: int) -> None:
        """Guarda o JSON da página por ``ttl_seconds``."""
        ...

    def delete(self, *keys: str) -> None:
        """Apaga as chaves (salvar, pausar ou apagar um reward)."""
        ...


class RedisRewardCache:
    """O cache no Redis, compartilhado pelas instâncias da API e pelo worker."""

    def __init__(self, client: redis.Redis) -> None:
        self._client = client

    @classmethod
    def from_url(cls, url: str) -> "RedisRewardCache":
        """Conecta ao Redis pela URL."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def get(self, key: str) -> str | None:
        """Lê a chave como texto; com o Redis fora, vazio (a página vai ao banco)."""
        try:
            found = self._client.get(key)
        except redis.RedisError:
            log.warning("cache do reward indisponível na leitura", exc_info=True)
            return None
        return found.decode() if isinstance(found, bytes) else found

    def set(self, key: str, value: str, ttl_seconds: int) -> None:
        """Grava com prazo; com o Redis fora, segue sem cache."""
        try:
            self._client.set(key, value, ex=ttl_seconds)
        except redis.RedisError:
            log.warning("cache do reward indisponível na escrita", exc_info=True)

    def delete(self, *keys: str) -> None:
        """Apaga as chaves pedidas; com o Redis fora, só registra (o prazo limpa depois)."""
        if not keys:
            return
        try:
            self._client.delete(*keys)
        except redis.RedisError:
            log.warning("cache do reward indisponível ao apagar", exc_info=True)
