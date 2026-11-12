"""Buffer dos key-values que a g-tag manda, no Redis: a rota não toca no banco.

O contrato com o avant-worker (que esvazia o buffer e cria os valores no GAM):
``kv:networks:connected`` é o conjunto das networks aceitas (o worker atualiza);
``kv:buffer:networks`` tem as networks com valores pendentes; ``kv:buffer:{network}`` tem os
pares ``key:value`` pendentes da network.
"""

from typing import Protocol

import redis

CONNECTED = "kv:networks:connected"
PENDING_NETWORKS = "kv:buffer:networks"
BUFFER = "kv:buffer:{network}"


class KeyValueBuffer(Protocol):
    def is_connected(self, network_code: str) -> bool:
        """Diz se a network está conectada (lista mantida pelo worker)."""
        ...

    def push(self, network_code: str, pairs: set[str]) -> None:
        """Guarda os pares ``key:value`` da network para o worker."""
        ...


class RedisKeyValueBuffer:
    """O buffer no Redis, compartilhado por todas as instâncias da API e pelo worker."""

    def __init__(self, client: redis.Redis) -> None:
        self._client = client

    @classmethod
    def from_url(cls, url: str) -> "RedisKeyValueBuffer":
        """Conecta ao Redis pela URL."""
        return cls(redis.Redis.from_url(url, socket_timeout=1.0))

    def is_connected(self, network_code: str) -> bool:
        """Consulta o conjunto das networks conectadas."""
        return bool(self._client.sismember(CONNECTED, network_code))

    def push(self, network_code: str, pairs: set[str]) -> None:
        """Acrescenta os pares ao conjunto da network e marca a network como pendente."""
        pipe = self._client.pipeline(transaction=False)
        pipe.sadd(BUFFER.format(network=network_code), *pairs)
        pipe.sadd(PENDING_NETWORKS, network_code)
        pipe.execute()
