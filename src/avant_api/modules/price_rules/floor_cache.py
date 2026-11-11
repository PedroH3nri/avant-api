"""Apaga o cache público dos floors e da escada da Cascata quando a regra ou o site mudam à mão."""

import uuid

from avant_core.ports import UnitOfWork
from avant_core.price_rules.catalog import CASCADE_CACHE_KEY, FLOOR_CACHE_KEY
from avant_core.price_rules.enums import PriceRuleModel
from avant_core.price_rules.models import PriceRule

from avant_api.app.reward_cache import RewardCache


def forget_floors(cache: RewardCache, site_id: uuid.UUID, content_hash: str) -> None:
    """Apaga os floors guardados do hash do site; a tag busca de novo no próximo pedido."""
    cache.delete(FLOOR_CACHE_KEY.format(site_id=site_id, content_hash=content_hash))


def forget_cascades(cache: RewardCache, site_id: uuid.UUID) -> None:
    """Apaga a escada da Cascata guardada do site; a tag e o reward buscam de novo."""
    cache.delete(CASCADE_CACHE_KEY.format(site_id=site_id))


def forget_rule(cache: RewardCache, rule: PriceRule) -> None:
    """Apaga o que a regra alimenta: a escada se for Cascata, os floors do hash se não for."""
    if rule.model is PriceRuleModel.CASCADE:
        forget_cascades(cache, rule.site_id)
        return
    forget_floors(cache, rule.site_id, rule.content_hash)


def forget_site(cache: RewardCache, uow: UnitOfWork, site_id: uuid.UUID) -> None:
    """Apaga a escada e os floors de todos os hashes das regras do site (blocos e ajustes)."""
    with uow:
        hashes = {rule.content_hash for rule in uow.price_rules.list_for_site(site_id)}
    forget_cascades(cache, site_id)
    for content_hash in hashes:
        forget_floors(cache, site_id, content_hash)
