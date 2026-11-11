"""A escada da Cascata de todos os países de um site, lida pelo cache por site.

A chave é ``avant:price-cascades:{site}``. Serve a rota dos floors e a página do reward: o mesmo
valor, a mesma validade. Falha na busca nunca derruba quem chama.
"""

import json
import logging
import uuid
from typing import cast

from avant_core.price_rules.catalog import CASCADE_CACHE_KEY, FLOOR_CACHE_SECONDS
from avant_core.price_rules.services import public_price_cascades

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import EMPTY_TTL_SECONDS, RewardCache

log = logging.getLogger("avant.api.price_cascade_cache")


def is_cascade_shape(value: object) -> bool:
    """Confere o formato país, bloco, lista de textos; qualquer outro valor é lixo no cache."""
    return isinstance(value, dict) and all(
        isinstance(blocks, dict)
        and all(
            isinstance(ladder, list) and all(isinstance(label, str) for label in ladder)
            for ladder in blocks.values()
        )
        for blocks in value.values()
    )


def site_cascades(
    cache: RewardCache, uows: UnitOfWorkFactory, site_id: str
) -> dict[str, dict[str, list[str]]]:
    """A escada de todos os países do site, do cache ou do banco (e então guardada)."""
    cascade_key = CASCADE_CACHE_KEY.format(site_id=site_id)
    cached = cache.get(cascade_key)
    if cached is not None:
        try:
            stored = json.loads(cached)
        except ValueError:
            stored = None
        if is_cascade_shape(stored):
            return cast("dict[str, dict[str, list[str]]]", stored)
        log.warning("escada da Cascata inválida no cache do site %s", site_id)
    found = public_price_cascades(uows.trusted_uow(), site_id=uuid.UUID(site_id))
    cache.set(cascade_key, json.dumps(found), FLOOR_CACHE_SECONDS if found else EMPTY_TTL_SECONDS)
    return found


def safe_site_cascades(
    cache: RewardCache, uows: UnitOfWorkFactory, site_id: str
) -> dict[str, dict[str, list[str]]]:
    """A escada do site, ou vazio (e um aviso) quando a busca falha: quem chama segue."""
    try:
        return site_cascades(cache, uows, site_id)
    except Exception:
        log.warning("falha ao buscar a escada da Cascata do site %s", site_id, exc_info=True)
        return {}
