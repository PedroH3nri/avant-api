"""Service das rotas públicas do reward: cache da configuração e buffer dos eventos e contatos.

Nada aqui grava no banco: os eventos e contatos vão para o buffer do Redis, que o worker
esvazia a cada minuto (``avant_api.app.reward_buffer``). O dia do evento é o de São Paulo.
"""

import json
import logging
import time
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

from avant_core.ports import UnitOfWork
from avant_core.rewards.enums import RewardLeadKind
from avant_core.rewards.models import RewardIcon
from avant_core.rewards.services import (
    clean_lead_answers,
    clean_lead_contact,
    clean_lead_language,
    clean_lead_name,
    get_public_reward_icon,
    parse_page_url,
    public_reward,
)
from avant_core.shared.clock import Clock

from avant_api.app.countries import CountryLookup
from avant_api.app.errors import RateLimited
from avant_api.app.limits import REWARD_CONFIG, REWARD_EVENTS, REWARD_LEADS, Bucket, BucketRule
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.price_cascade_cache import safe_site_cascades
from avant_api.app.reward_buffer import RewardBuffer
from avant_api.app.reward_cache import (
    EMPTY_TTL_SECONDS,
    TTL_SECONDS,
    RewardCache,
    reward_cache_key,
)
from avant_api.modules.reward_public.dto import (
    CachedPage,
    PublicPageOut,
    PublicRewardOut,
    PublicRewardPriceOut,
    RewardEventsIn,
    RewardLeadIn,
)

log = logging.getLogger("avant.api.reward_public")

DAY_ZONE = ZoneInfo("America/Sao_Paulo")
NO_REWARD = PublicPageOut(reward=None).model_dump_json(exclude={"price_rules"})
REWARD_BLOCK_PREFIX = "Rewards"


def public_control_percent(uow: UnitOfWork, site_id: uuid.UUID) -> int | None:
    """O percentual de controle das regras de preço do site, ou vazio com a regra desligada."""
    with uow:
        settings = uow.price_rule_settings.get(site_id)
        if settings is None or not settings.active:
            return None
        return settings.control_percent


class PublicRewardService:
    """A configuração da página, o ícone e a entrada dos eventos e contatos."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        cache: RewardCache,
        buffer: RewardBuffer,
        bucket: Bucket,
        countries: CountryLookup,
        *,
        base_url: str,
        groone_network_code: str,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache
        self._buffer = buffer
        self._bucket = bucket
        self._countries = countries
        self._base_url = base_url.rstrip("/")
        self._groone_network_code = groone_network_code

    def page(self, url: str, client: str) -> str:
        """O JSON da configuração da página, do cache ou do banco (e então guardado)."""
        self._limit("reward-config", REWARD_CONFIG, client)
        parsed = parse_page_url(url)
        if parsed is None:
            return NO_REWARD
        key = reward_cache_key(*parsed)
        cached = self._cache.get(key)
        if cached is None:
            cached = self._load_page(url, key)
        return self._answer(cached, client)

    def _load_page(self, url: str, key: str) -> str:
        """Lê a página do banco e guarda; a leitura da regra de preço que falha não é guardada."""
        found = public_reward(
            self._uows.trusted_uow(), url=url, groone_network_code=self._groone_network_code
        )
        if found is None:
            self._cache.set(key, NO_REWARD, EMPTY_TTL_SECONDS)
            return NO_REWARD
        site_id = found.reward.site_id
        reward = PublicRewardOut.of(found, self._base_url)
        try:
            control_percent = public_control_percent(self._uows.trusted_uow(), site_id)
        except Exception:
            log.warning("falha ao ler a regra de preço do site %s", site_id, exc_info=True)
            return CachedPage(reward=reward).model_dump_json()
        entry = CachedPage(reward=reward, site_id=site_id, control_percent=control_percent)
        body = entry.model_dump_json()
        self._cache.set(key, body, TTL_SECONDS)
        return body

    def _answer(self, cached: str, client: str) -> str:
        """A resposta pública: o reward da página e a escada do país de quem pede."""
        entry = CachedPage.model_validate_json(cached)
        if entry.reward is None:
            return NO_REWARD
        price_rules = None
        if entry.site_id is not None and entry.control_percent is not None:
            country = (self._countries.country_code(client) or "").upper()
            ladders = safe_site_cascades(self._cache, self._uows, str(entry.site_id))
            price_rules = PublicRewardPriceOut(
                control_percent=entry.control_percent,
                cascades={
                    block: ladder
                    for block, ladder in ladders.get(country, {}).items()
                    if block.startswith(REWARD_BLOCK_PREFIX)
                },
            )
        return PublicPageOut(reward=entry.reward, price_rules=price_rules).model_dump_json()

    def icon(self, reward_id: uuid.UUID, client: str) -> RewardIcon:
        """O ícone em imagem do reward, com o mesmo limite por IP da configuração."""
        self._limit("reward-icon", REWARD_CONFIG, client)
        return get_public_reward_icon(self._uows.trusted_uow(), reward_id=reward_id)

    def events(self, body: RewardEventsIn, client: str) -> int:
        """Guarda os eventos no buffer com o dia de hoje; devolve quantos."""
        self._limit("reward-events", REWARD_EVENTS, client)
        day = self._today()
        items = [
            json.dumps({"type": "event", "day": day, **event.model_dump(mode="json")})
            for event in body.events
        ]
        return len(items) if self._buffer.push(items) else 0

    def lead(self, body: RewardLeadIn, client: str) -> None:
        """Confere o contato e guarda no buffer; o worker confere de novo contra o reward."""
        self._limit("reward-leads", REWARD_LEADS, client)
        kind = RewardLeadKind.EMAIL if "@" in body.contact else RewardLeadKind.PHONE
        pairs = tuple((answer.question_id, answer.answer) for answer in body.answers)
        question_ids, answers = clean_lead_answers(pairs, {pair[0] for pair in pairs})
        item = {
            "type": "lead",
            "reward_id": str(body.reward_id),
            "name": clean_lead_name(body.name),
            "contact": clean_lead_contact(kind, body.contact),
            "language": clean_lead_language(body.language),
            "answers": [
                {"question_id": str(question_id), "answer": answer}
                for question_id, answer in zip(question_ids, answers, strict=True)
            ],
            "created_at": self._clock.now().isoformat(),
        }
        self._buffer.push([json.dumps(item)])

    def _limit(self, name: str, rule: BucketRule, client: str) -> None:
        """Tira uma ficha do balde do IP, ou recusa com 429."""
        taken = self._bucket.take(f"{name}:{client}", rule, time.time())
        if not taken.allowed:
            raise RateLimited("muitos pedidos deste endereço", retry_after=taken.retry_after)

    def _today(self) -> str:
        """O dia de hoje em São Paulo, em ISO."""
        now: datetime = self._clock.now()
        return now.astimezone(DAY_ZONE).date().isoformat()
