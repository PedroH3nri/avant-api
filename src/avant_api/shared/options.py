"""Listas para seletores (``/options``): com busca opcional e um teto, para não devolver
milhares de itens de uma vez."""

from collections.abc import Callable

OPTIONS_LIMIT = 2000


def capped[Item](items: list[Item], query: str | None, label: Callable[[Item], str]) -> list[Item]:
    """Os itens cujo rótulo contém o trecho (sem diferenciar maiúsculas), até o teto."""
    needle = (query or "").strip().casefold()
    found = [item for item in items if needle in label(item).casefold()] if needle else items
    return found[:OPTIONS_LIMIT]
