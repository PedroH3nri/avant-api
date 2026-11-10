"""Apaga o cache público de uma ad tag depois de publicar, pausar ou apagar."""

from avant_api.app.ad_tag_cache import ad_tag_cache_key
from avant_api.app.reward_cache import RewardCache


def forget_tag(cache: RewardCache, key: str) -> None:
    """Apaga a configuração guardada da tag."""
    cache.delete(ad_tag_cache_key(key))
