"""Apaga o cache público das páginas que um reward usa, depois de mudar o reward."""

from avant_core.rewards.models import RewardDetails

from avant_api.app.reward_cache import RewardCache, reward_cache_key


def forget_pages(cache: RewardCache, *rewards: RewardDetails) -> None:
    """Apaga a chave da página de cada reward (o de antes e o de depois de uma edição)."""
    cache.delete(*{reward_cache_key(item.domain, item.reward.page_path) for item in rewards})
