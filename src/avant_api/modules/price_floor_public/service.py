"""Service da rota pública dos floors: cache por site e content_hash e o país pelo IP.

Duas chaves no Redis (o mesmo do reward): ``avant:price-floors:tag:{chave}`` guarda o site da
tag (vazio quando a tag não leva regra) e ``avant:price-floors:{site}:{hash}`` guarda o controle
e os floors de todos os países do hash. O worker apaga a segunda quando o floor muda; o painel
apaga quando a regra muda à mão. Ligar, desligar e trocar blocos vale em até 1 hora.
"""

import json
import time

from avant_core.price_rules.catalog import FLOOR_CACHE_KEY, FLOOR_CACHE_SECONDS
from avant_core.price_rules.services import public_price_floors

from avant_api.app.countries import CountryLookup
from avant_api.app.errors import RateLimited
from avant_api.app.limits import TAG_PRICES, Bucket
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.price_floor_public.dto import PublicPriceFloorsOut

TAG_SITE_KEY = "avant:price-floors:tag:{key}"
NO_SITE = ""
EMPTY_TTL_SECONDS = 300


class PublicPriceFloorService:
    """Os floors do hash da página no país de quem pede."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        cache: RewardCache,
        bucket: Bucket,
        countries: CountryLookup,
    ) -> None:
        self._uows = uows
        self._cache = cache
        self._bucket = bucket
        self._countries = countries

    def floors(self, key: str, content_hash: str, client: str) -> PublicPriceFloorsOut:
        """O controle e os floors do país do IP, do cache ou do banco (e então guardados)."""
        taken = self._bucket.take(f"tag-prices:{client}", TAG_PRICES, time.time())
        if not taken.allowed:
            raise RateLimited("muitos pedidos deste endereço", retry_after=taken.retry_after)
        site_key = TAG_SITE_KEY.format(key=key)
        site_id = self._cache.get(site_key)
        if site_id == NO_SITE:
            return PublicPriceFloorsOut()
        cached = None
        if site_id is not None:
            cached = self._cache.get(
                FLOOR_CACHE_KEY.format(site_id=site_id, content_hash=content_hash)
            )
        if cached is None:
            cached = self._load(key, content_hash)
            if cached is None:
                return PublicPriceFloorsOut()
        stored = json.loads(cached)
        country = (self._countries.country_code(client) or "").upper()
        return PublicPriceFloorsOut(
            control_percent=stored["control_percent"],
            floors=stored["floors"].get(country, {}),
        )

    def _load(self, key: str, content_hash: str) -> str | None:
        """Lê do banco e guarda o site da tag e os floors do hash; vazio sem regra na tag."""
        found = public_price_floors(self._uows.trusted_uow(), key=key, content_hash=content_hash)
        site_key = TAG_SITE_KEY.format(key=key)
        if found is None:
            self._cache.set(site_key, NO_SITE, EMPTY_TTL_SECONDS)
            return None
        value = json.dumps({"control_percent": found.control_percent, "floors": found.floors})
        floors_key = FLOOR_CACHE_KEY.format(site_id=found.site_id, content_hash=content_hash)
        ttl = FLOOR_CACHE_SECONDS if found.floors else EMPTY_TTL_SECONDS
        self._cache.set(site_key, str(found.site_id), FLOOR_CACHE_SECONDS)
        self._cache.set(floors_key, value, ttl)
        return value
