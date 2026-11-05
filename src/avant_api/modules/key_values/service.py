"""Recebe os key-values da g-tag: confere a network, limpa e guarda no buffer, sem banco."""

import time

from avant_core.gam.key_values.services import traffic_key_value

from avant_api.app.errors import RateLimited
from avant_api.app.key_value_buffer import KeyValueBuffer
from avant_api.app.limits import KEY_VALUES, Bucket
from avant_api.modules.key_values.dto import KeyValueIn


def receive_key_values(
    items: list[KeyValueIn], *, client: str, bucket: Bucket, buffer: KeyValueBuffer
) -> int:
    """Guarda os pares limpos das networks conectadas e devolve quantos; 4 pedidos por segundo
    por IP, e o que não serve (key de fora, valor sujo, network não conectada) é ignorado."""
    taken = bucket.take(f"key-values:{client}", KEY_VALUES, time.time())
    if not taken.allowed:
        raise RateLimited("muitos key-values deste endereço", retry_after=taken.retry_after)
    by_network: dict[str, set[str]] = {}
    for item in items:
        value = traffic_key_value(item.name, item.value)
        network = network_code(item.network)
        if value is None or not network:
            continue
        by_network.setdefault(network, set()).add(f"{item.name}:{value}")
    stored = 0
    for network, pairs in by_network.items():
        if buffer.is_connected(network):
            buffer.push(network, pairs)
            stored += len(pairs)
    return stored


def network_code(raw: str) -> str:
    """O código da network como a g-tag manda; nas Manage Inventory vem ``groone,filha`` e vale
    o primeiro. Só algarismos."""
    first = raw.split(",", 1)[0].strip()
    return first if first.isascii() and first.isdecimal() else ""
