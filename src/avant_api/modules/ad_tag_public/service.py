"""Service da rota pública da ad tag: a configuração da versão no ar, com cache por chave.

O cache guarda a configuração com o domínio do site; a rota confere o domínio da página a cada
pedido, então uma chave copiada para outro site recebe ``{"tag": null}``.
"""

import json
import time

from avant_core.ad_tags.services import public_ad_tag
from avant_core.rewards.services import parse_page_url

from avant_api.app.ad_tag_cache import EMPTY_TTL_SECONDS, TTL_SECONDS, ad_tag_cache_key
from avant_api.app.errors import RateLimited
from avant_api.app.limits import TAG_CONFIG, Bucket
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.ad_tag_public.dto import PublicAdTagOut, PublicTagOut

NO_TAG = PublicTagOut(tag=None).model_dump_json()
EMPTY = "{}"
MAX_KEY = 20


class PublicAdTagService:
    """A configuração da tag para a página que pede."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        cache: RewardCache,
        bucket: Bucket,
        *,
        groone_network_code: str,
    ) -> None:
        self._uows = uows
        self._cache = cache
        self._bucket = bucket
        self._groone_network_code = groone_network_code

    def config(self, key: str, url: str, client: str) -> str:
        """O JSON da configuração para a URL, do cache ou do banco (e então guardado)."""
        taken = self._bucket.take(f"tag-config:{client}", TAG_CONFIG, time.time())
        if not taken.allowed:
            raise RateLimited("muitos pedidos deste endereço", retry_after=taken.retry_after)
        parsed = parse_page_url(url)
        if parsed is None or len(key) > MAX_KEY:
            return NO_TAG
        cache_key = ad_tag_cache_key(key)
        cached = self._cache.get(cache_key)
        if cached is None:
            cached = self._load(key, f"https://{parsed[0]}/")
            self._cache.set(
                cache_key, cached, TTL_SECONDS if cached != EMPTY else EMPTY_TTL_SECONDS
            )
        if cached == EMPTY or json.loads(cached).get("domain") != parsed[0]:
            return NO_TAG
        return '{"tag":' + cached + "}"

    def _load(self, key: str, url: str) -> str:
        """A configuração da tag do banco, em JSON, ou ``{}`` quando não há."""
        found = public_ad_tag(
            self._uows.trusted_uow(),
            key=key,
            url=url,
            groone_network_code=self._groone_network_code,
        )
        return EMPTY if found is None else PublicAdTagOut.of(found).model_dump_json()
