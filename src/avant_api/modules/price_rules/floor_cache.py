"""Apaga o cache público dos floors de um hash quando a regra muda à mão (floor ou status)."""

import uuid

from avant_core.price_rules.catalog import FLOOR_CACHE_KEY

from avant_api.app.reward_cache import RewardCache


def forget_floors(cache: RewardCache, site_id: uuid.UUID, content_hash: str) -> None:
    """Apaga os floors guardados do hash do site; a tag busca de novo no próximo pedido."""
    cache.delete(FLOOR_CACHE_KEY.format(site_id=site_id, content_hash=content_hash))
