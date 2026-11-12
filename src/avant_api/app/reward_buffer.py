"""Buffer no Redis dos eventos e contatos que o script do reward manda: a rota não toca no banco.

O contrato com o avant-worker (``avant.default.flush_reward_events``, a cada minuto): a lista
``avant:reward:buffer`` recebe um JSON por item, ``{"type": "event", ...}`` ou
``{"type": "lead", ...}``. O worker renomeia a lista para ``avant:reward:processing:{lote}``,
grava o lote no banco e apaga a chave; o identificador do lote torna a gravação idempotente.

As páginas vistas do ``tag.js`` usam a mesma fila em outra lista, ``avant:page-views:buffer``
(``avant.default.flush_page_views``): um JSON por página com o ``ip`` e o ``received_at``.
"""

from typing import Protocol

import redis

BUFFER = "avant:reward:buffer"
PAGE_VIEWS_BUFFER = "avant:page-views:buffer"
# Acima disso, o buffer descarta (o worker parado não enche o Redis).
MAX_ITEMS = 500_000


class RewardBuffer(Protocol):
    def push(self, items: list[str]) -> bool:
        """Guarda os itens (JSON) para o worker; ``False`` quando o buffer está cheio."""
        ...


class RedisRewardBuffer:
    """O buffer no Redis, compartilhado pelas instâncias da API e pelo worker."""

    def __init__(self, client: redis.Redis, key: str = BUFFER) -> None:
        self._client = client
        self._key = key

    @classmethod
    def from_url(cls, url: str, key: str = BUFFER) -> "RedisRewardBuffer":
        """Conecta ao Redis pela URL, para a lista dada."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0), key)

    def push(self, items: list[str]) -> bool:
        """Acrescenta ao fim da lista, se ela ainda cabe."""
        if not items or int(self._client.llen(self._key)) >= MAX_ITEMS:
            return False
        self._client.rpush(self._key, *items)
        return True
