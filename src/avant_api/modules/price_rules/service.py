"""Service das regras de preço de um site da Empresa ativa, com o RLS dela."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.price_rules.enums import PriceRuleModel
from avant_core.price_rules.services import (
    get_price_rule,
    get_price_rule_site,
    list_price_rule_history,
    page_price_rules,
    set_price_rule_floor,
    set_price_rule_status,
    update_price_rule_blocks,
    update_price_rule_config,
    update_price_rule_settings,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.price_rules.dto import (
    PriceRuleConfigIn,
    PriceRuleDetailsOut,
    PriceRuleFloorIn,
    PriceRuleHistoryOut,
    PriceRuleOut,
    PriceRuleSettingsIn,
    PriceRuleSiteOut,
    PriceRuleStatusIn,
)
from avant_api.modules.price_rules.floor_cache import forget_floors
from avant_api.shared.dto import PageOut, page_out


class PriceRuleService:
    """Regras de preço da Empresa ativa; o core confere a permissão e os sites do membro."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, cache: RewardCache) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache

    def site(self, actor: Actor, site_id: uuid.UUID) -> PriceRuleSiteOut:
        """A configuração e os blocos do site."""
        view = get_price_rule_site(
            self._uows.uow(actor.company_id), actor=actor, site_id=site_id, clock=self._clock
        )
        return PriceRuleSiteOut.of(view)

    def update_settings(
        self, actor: Actor, site_id: uuid.UUID, body: PriceRuleSettingsIn
    ) -> PriceRuleSiteOut:
        """Liga ou desliga a regra e grava o percentual do controle."""
        view = update_price_rule_settings(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            active=body.active,
            control_percent=body.control_percent,
            clock=self._clock,
        )
        return PriceRuleSiteOut.of(view)

    def update_blocks(
        self, actor: Actor, site_id: uuid.UUID, blocks: dict[str, PriceRuleModel]
    ) -> PriceRuleSiteOut:
        """Troca os blocos marcados e o modelo de cada um."""
        view = update_price_rule_blocks(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            blocks=blocks,
            clock=self._clock,
        )
        return PriceRuleSiteOut.of(view)

    def page(
        self,
        actor: Actor,
        site_id: uuid.UUID,
        page: int,
        content_hash: str | None,
        country_code: str | None,
    ) -> PageOut[PriceRuleOut]:
        """Uma página das regras do site."""
        found = page_price_rules(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            page=page,
            content_hash=content_hash,
            country_code=country_code,
        )
        return page_out(found, PriceRuleOut.of)

    def get(self, actor: Actor, site_id: uuid.UUID, rule_id: uuid.UUID) -> PriceRuleDetailsOut:
        """Uma regra com os limites."""
        details = get_price_rule(
            self._uows.uow(actor.company_id), actor=actor, site_id=site_id, rule_id=rule_id
        )
        return PriceRuleDetailsOut.of_details(details)

    def history(
        self, actor: Actor, site_id: uuid.UUID, rule_id: uuid.UUID, start: date, end: date
    ) -> list[PriceRuleHistoryOut]:
        """As decisões da regra no período, até 31 dias."""
        entries = list_price_rule_history(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            rule_id=rule_id,
            start=start,
            end=end,
        )
        return [PriceRuleHistoryOut.of(entry) for entry in entries]

    def update_config(
        self, actor: Actor, site_id: uuid.UUID, rule_id: uuid.UUID, body: PriceRuleConfigIn
    ) -> PriceRuleDetailsOut:
        """Grava os limites da regra."""
        details = update_price_rule_config(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            rule_id=rule_id,
            data=body.to_core(),
            clock=self._clock,
        )
        return PriceRuleDetailsOut.of_details(details)

    def set_status(
        self, actor: Actor, site_id: uuid.UUID, rule_id: uuid.UUID, body: PriceRuleStatusIn
    ) -> PriceRuleDetailsOut:
        """Ativa, pausa ou desliga a regra e apaga o cache dos floors do hash."""
        details = set_price_rule_status(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            rule_id=rule_id,
            status=body.status,
            clock=self._clock,
        )
        forget_floors(self._cache, details.rule.site_id, details.rule.content_hash)
        return PriceRuleDetailsOut.of_details(details)

    def set_floor(
        self, actor: Actor, site_id: uuid.UUID, rule_id: uuid.UUID, body: PriceRuleFloorIn
    ) -> PriceRuleDetailsOut:
        """Troca o floor à mão e apaga o cache dos floors do hash."""
        details = set_price_rule_floor(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=site_id,
            rule_id=rule_id,
            floor_micros=body.floor_micros,
            clock=self._clock,
        )
        forget_floors(self._cache, details.rule.site_id, details.rule.content_hash)
        return PriceRuleDetailsOut.of_details(details)
