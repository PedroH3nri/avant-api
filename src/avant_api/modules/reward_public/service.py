"""Service das rotas públicas do reward: cache da configuração e buffer dos eventos e contatos.

Nada aqui grava no banco: os eventos e contatos vão para o buffer do Redis, que o worker
esvazia a cada minuto (``avant_api.app.reward_buffer``). O dia do evento é o de São Paulo.
"""

import json
import time
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

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

from avant_api.app.errors import RateLimited
from avant_api.app.limits import REWARD_CONFIG, REWARD_EVENTS, REWARD_LEADS, Bucket, BucketRule
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_buffer import RewardBuffer
from avant_api.app.reward_cache import (
    EMPTY_TTL_SECONDS,
    TTL_SECONDS,
    RewardCache,
    reward_cache_key,
)
from avant_api.modules.reward_public.dto import (
    PublicPageOut,
    PublicRewardOut,
    RewardEventsIn,
    RewardLeadIn,
)

DAY_ZONE = ZoneInfo("America/Sao_Paulo")
NO_REWARD = PublicPageOut(reward=None).model_dump_json()


class PublicRewardService:
    """A configuração da página, o ícone e a entrada dos eventos e contatos."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        cache: RewardCache,
        buffer: RewardBuffer,
        bucket: Bucket,
        *,
        base_url: str,
        groone_network_code: str,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache
        self._buffer = buffer
        self._bucket = bucket
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
        if cached is not None:
            return cached
        found = public_reward(
            self._uows.trusted_uow(), url=url, groone_network_code=self._groone_network_code
        )
        reward = None if found is None else PublicRewardOut.of(found, self._base_url)
        body = PublicPageOut(reward=reward).model_dump_json()
        self._cache.set(key, body, TTL_SECONDS if reward else EMPTY_TTL_SECONDS)
        return body

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
