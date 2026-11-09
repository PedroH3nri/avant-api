"""Service dos rewards do painel do cliente: chama os casos de uso e limpa o cache das páginas."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.ports import ImageProcessor
from avant_core.rewards.models import RewardLeadFilter
from avant_core.rewards.services import (
    create_reward,
    delete_reward,
    delete_reward_lead,
    export_reward_leads,
    get_reward,
    list_reward_ad_units,
    page_reward_leads,
    page_rewards,
    reward_metrics,
    set_reward_active,
    set_reward_icon,
    update_reward,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.rewards.cache import forget_pages
from avant_api.modules.rewards.dto import (
    RewardAdUnitGroupOut,
    RewardIn,
    RewardLeadOut,
    RewardMetricsOut,
    RewardOut,
)
from avant_api.shared.dto import PageOut, page_out


class RewardService:
    """Rewards da Empresa ativa, com o RLS dela."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, images: ImageProcessor, cache: RewardCache
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._images = images
        self._cache = cache

    def page(
        self,
        actor: Actor,
        page: int,
        site_id: uuid.UUID | None,
        query: str | None,
        deleted: bool = False,
    ) -> PageOut[RewardOut]:
        """Uma página dos rewards, o mais novo primeiro."""
        found = page_rewards(
            self._uows.uow(actor.company_id),
            actor=actor,
            page=page,
            site_id=site_id,
            query=query,
            deleted=deleted,
        )
        return page_out(found, RewardOut.of)

    def get(self, actor: Actor, reward_id: uuid.UUID) -> RewardOut:
        """Um reward com as perguntas."""
        return RewardOut.of(
            get_reward(self._uows.uow(actor.company_id), actor=actor, reward_id=reward_id)
        )

    def create(self, actor: Actor, body: RewardIn) -> RewardOut:
        """Cria o reward e limpa o cache da página (que podia estar guardada sem reward)."""
        created = create_reward(
            self._uows.uow(actor.company_id), actor=actor, data=body.to_core(), clock=self._clock
        )
        forget_pages(self._cache, created)
        return RewardOut.of(created)

    def update(self, actor: Actor, reward_id: uuid.UUID, body: RewardIn) -> RewardOut:
        """Troca todos os campos e limpa o cache da página antiga e da nova."""
        before = get_reward(self._uows.uow(actor.company_id), actor=actor, reward_id=reward_id)
        after = update_reward(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            data=body.to_core(),
            clock=self._clock,
        )
        forget_pages(self._cache, before, after)
        return RewardOut.of(after)

    def set_active(self, actor: Actor, reward_id: uuid.UUID, active: bool) -> RewardOut:
        """Pausa ou ativa e limpa o cache da página."""
        changed = set_reward_active(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            active=active,
            clock=self._clock,
        )
        forget_pages(self._cache, changed)
        return RewardOut.of(changed)

    def delete(self, actor: Actor, reward_id: uuid.UUID) -> None:
        """Apaga o reward e limpa o cache da página."""
        before = get_reward(self._uows.uow(actor.company_id), actor=actor, reward_id=reward_id)
        delete_reward(
            self._uows.uow(actor.company_id), actor=actor, reward_id=reward_id, clock=self._clock
        )
        forget_pages(self._cache, before)

    def set_icon(self, actor: Actor, reward_id: uuid.UUID, content: bytes) -> RewardOut:
        """Troca o ícone por uma imagem e limpa o cache da página."""
        changed = set_reward_icon(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            content=content,
            images=self._images,
            clock=self._clock,
        )
        forget_pages(self._cache, changed)
        return RewardOut.of(changed)

    def ad_units(self, actor: Actor, site_id: uuid.UUID) -> list[RewardAdUnitGroupOut]:
        """Os grupos de ad units de reward do site, do mais recente para o mais antigo."""
        groups = list_reward_ad_units(
            self._uows.uow(actor.company_id), actor=actor, site_id=site_id
        )
        return [RewardAdUnitGroupOut.of(group) for group in groups]

    def metrics(
        self, actor: Actor, reward_id: uuid.UUID, start: date, end: date
    ) -> RewardMetricsOut:
        """As métricas do período."""
        found = reward_metrics(
            self._uows.uow(actor.company_id), actor=actor, reward_id=reward_id, start=start, end=end
        )
        return RewardMetricsOut.of(found)

    def leads(
        self, actor: Actor, reward_id: uuid.UUID, lead_filter: RewardLeadFilter, page: int
    ) -> PageOut[RewardLeadOut]:
        """Uma página dos contatos, o mais novo primeiro."""
        found = page_reward_leads(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            lead_filter=lead_filter,
            page=page,
        )
        return page_out(found, RewardLeadOut.of)

    def export_leads(
        self, actor: Actor, reward_id: uuid.UUID, lead_filter: RewardLeadFilter
    ) -> str:
        """O CSV dos contatos; a exportação fica na auditoria."""
        return export_reward_leads(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            lead_filter=lead_filter,
            clock=self._clock,
        )

    def delete_lead(self, actor: Actor, reward_id: uuid.UUID, lead_id: uuid.UUID) -> None:
        """Apaga um contato (pedido do titular, por exemplo)."""
        delete_reward_lead(
            self._uows.uow(actor.company_id),
            actor=actor,
            reward_id=reward_id,
            lead_id=lead_id,
            clock=self._clock,
        )
