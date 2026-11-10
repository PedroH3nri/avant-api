"""Service das rotas públicas da ad tag: a configuração da versão no ar, com cache por chave, e
as páginas vistas, que vão para o buffer do worker.

O cache guarda a configuração com o domínio do site; a rota confere o domínio da página a cada
pedido, então uma chave copiada para outro site recebe ``{"tag": null}``. A página vista não
toca no banco: o worker confere a tag e o domínio ao gravar.
"""

import json
import time

from avant_core.ad_tags.services import public_ad_tag
from avant_core.rewards.services import parse_page_url
from avant_core.shared.clock import Clock

from avant_api.app.ad_tag_cache import EMPTY_TTL_SECONDS, TTL_SECONDS, ad_tag_cache_key
from avant_api.app.errors import RateLimited
from avant_api.app.limits import TAG_CONFIG, TAG_PAGE_VIEWS, Bucket, BucketRule
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_buffer import RewardBuffer
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.ad_tag_public.dto import PageViewIn, PublicAdTagOut, PublicTagOut

NO_TAG = PublicTagOut(tag=None).model_dump_json()
EMPTY = "{}"
MAX_KEY = 20


class PublicAdTagService:
    """A configuração da tag para a página que pede e as páginas vistas."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        cache: RewardCache,
        page_views: RewardBuffer,
        bucket: Bucket,
        *,
        groone_network_code: str,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache
        self._page_views = page_views
        self._bucket = bucket
        self._groone_network_code = groone_network_code

    def config(self, key: str, url: str, client: str) -> str:
        """O JSON da configuração para a URL, do cache ou do banco (e então guardado)."""
        self._limit("tag-config", TAG_CONFIG, client)
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

    def page_view(self, body: PageViewIn, client: str) -> bool:
        """Guarda a página vista no buffer com o IP e a hora de chegada; ``False`` quando o
        buffer está cheio."""
        self._limit("tag-page-views", TAG_PAGE_VIEWS, client)
        item = {
            **body.model_dump(mode="json"),
            "ip": client,
            "received_at": self._clock.now().isoformat(),
        }
        return self._page_views.push([json.dumps(item)])

    def _limit(self, name: str, rule: BucketRule, client: str) -> None:
        """Recusa com 429 quem passou do limite da rota."""
        taken = self._bucket.take(f"{name}:{client}", rule, time.time())
        if not taken.allowed:
            raise RateLimited("muitos pedidos deste endereço", retry_after=taken.retry_after)
