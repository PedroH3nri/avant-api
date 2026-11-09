"""Buffer no Redis dos eventos e contatos que o script do reward manda: a rota não toca no banco.

O contrato com o avant-worker (``avant.default.flush_reward_events``, a cada minuto): a lista
``avant:reward:buffer`` recebe um JSON por item, ``{"type": "event", ...}`` ou
``{"type": "lead", ...}``. O worker renomeia a lista para ``avant:reward:processing:{lote}``,
grava o lote no banco e apaga a chave; o identificador do lote torna a gravação idempotente.
"""

from dataclasses import dataclass, field
from typing import Protocol

import redis

BUFFER = "avant:reward:buffer"
# Acima disso, o buffer descarta (o worker parado não enche o Redis).
MAX_ITEMS = 500_000


class RewardBuffer(Protocol):
    def push(self, items: list[str]) -> bool:
        """Guarda os itens (JSON) para o worker; ``False`` quando o buffer está cheio."""
        ...


class RedisRewardBuffer:
    """O buffer no Redis, compartilhado pelas instâncias da API e pelo worker."""

    def __init__(self, client: redis.Redis) -> None:
        self._client = client

    @classmethod
    def from_url(cls, url: str) -> "RedisRewardBuffer":
        """Conecta ao Redis pela URL."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def push(self, items: list[str]) -> bool:
        """Acrescenta ao fim da lista, se ela ainda cabe."""
        if not items or int(self._client.llen(BUFFER)) >= MAX_ITEMS:
            return False
        self._client.rpush(BUFFER, *items)
        return True


@dataclass
class MemoryRewardBuffer:
    """Local e testes: a lista em memória."""

    items: list[str] = field(default_factory=list)

    def push(self, items: list[str]) -> bool:
        """Guarda na memória."""
        self.items.extend(items)
        return bool(items)
