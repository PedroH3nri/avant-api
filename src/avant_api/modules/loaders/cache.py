"""Apaga o cache público das ad tags que usam um loader, depois de mudar o loader."""

from avant_core.loaders.models import LoaderDetails

from avant_api.app.ad_tag_cache import ad_tag_cache_key
from avant_api.app.reward_cache import RewardCache


def forget_tags(cache: RewardCache, details: LoaderDetails) -> None:
    """Apaga a configuração guardada de cada tag que usa o loader."""
    cache.delete(*(ad_tag_cache_key(use.key) for use in details.tags))
