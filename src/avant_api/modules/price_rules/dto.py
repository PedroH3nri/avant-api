"""DTOs das regras de preço, usados pelo painel do cliente e pelo interno. Valores em micros,
na moeda da network do site (sem conversão). Datas em ISO 8601 UTC."""

import uuid
from datetime import date, datetime
from datetime import date as calendar_date

from avant_core.price_rules.catalog import DEFAULT_DROP_TIERS
from avant_core.price_rules.enums import (
    BlockKind,
    PriceRuleAction,
    PriceRuleModel,
    PriceRuleReason,
    PriceRuleStatus,
)
from avant_core.price_rules.models import (
    CascadeHour,
    HourlyCounts,
    PriceRule,
    PriceRuleConfig,
    PriceRuleConfigInput,
    PriceRuleDetails,
    PriceRuleHistoryEntry,
    PriceRuleHour,
    PriceRuleSiteSummary,
    PriceRuleSiteView,
)
from avant_core.price_rules.services import kind_of, recommended_model
from pydantic import BaseModel, Field


class PriceRuleBlockOut(BaseModel):
    block: str
    model: PriceRuleModel


class PriceRuleSiteOut(BaseModel):
    site_id: uuid.UUID
    domain: str
    active: bool
    control_percent: int
    # Moeda vista nos números do GAM; vazia até a primeira sincronia.
    currency: str | None
    currency_supported: bool
    blocks: list[PriceRuleBlockOut]
    available_blocks: list[str]
    # O modelo padrão da tela para cada bloco disponível que recebe regra.
    recommended_models: dict[str, PriceRuleModel]
    updated_at: datetime

    @classmethod
    def of(cls, view: PriceRuleSiteView) -> "PriceRuleSiteOut":
        """Monta a configuração do site."""
        settings = view.settings
        return cls(
            site_id=settings.site_id,
            domain=view.domain,
            active=settings.active,
            control_percent=settings.control_percent,
            currency=settings.currency,
            currency_supported=view.currency_supported,
            blocks=[PriceRuleBlockOut(block=item.block, model=item.model) for item in view.blocks],
            available_blocks=list(view.available_blocks),
            recommended_models=_recommended_models(view.available_blocks),
            updated_at=settings.updated_at,
        )


def _recommended_models(blocks: tuple[str, ...]) -> dict[str, PriceRuleModel]:
    """O modelo recomendado de cada bloco; o offerwall e os blocos sem tipo ficam de fora."""
    recommended = {}
    for block in blocks:
        kind = kind_of(block)
        model = recommended_model(kind) if kind is not None else None
        if model is not None:
            recommended[block] = model
    return recommended


class PriceRuleSiteSummaryOut(BaseModel):
    site_id: uuid.UUID
    domain: str
    # Só no interno: o nome do cliente dono do site.
    client: str | None
    active: bool
    control_percent: int
    currency: str | None
    currency_supported: bool
    automatic_blocks: int
    active_rules: int

    @classmethod
    def of(cls, summary: PriceRuleSiteSummary) -> "PriceRuleSiteSummaryOut":
        """Monta a linha da lista de sites."""
        settings = summary.settings
        return cls(
            site_id=summary.site.id,
            domain=summary.site.domain,
            client=summary.client_name,
            active=settings.active,
            control_percent=settings.control_percent,
            currency=settings.currency,
            currency_supported=summary.currency_supported,
            automatic_blocks=summary.automatic_blocks,
            active_rules=summary.active_rules,
        )


class PriceRuleSettingsIn(BaseModel):
    active: bool
    control_percent: int = Field(ge=0, le=50)


class PriceRuleBlocksIn(BaseModel):
    blocks: dict[str, PriceRuleModel] = Field(max_length=100)


class PriceRuleOut(BaseModel):
    id: uuid.UUID
    site_id: uuid.UUID
    content_hash: str
    block: str
    kind: BlockKind
    model: PriceRuleModel
    country_code: str
    currency: str
    floor_micros: int
    status: PriceRuleStatus
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, rule: PriceRule) -> "PriceRuleOut":
        """Monta a regra."""
        return cls(
            id=rule.id,
            site_id=rule.site_id,
            content_hash=rule.content_hash,
            block=rule.block,
            kind=rule.kind,
            model=rule.model,
            country_code=rule.country_code,
            currency=rule.currency,
            floor_micros=rule.floor_micros,
            status=rule.status,
            created_at=rule.created_at,
            updated_at=rule.updated_at,
        )


class PriceRuleConfigOut(BaseModel):
    pmr_floor: float
    pmr_emergency: float
    min_eligible_requests: int
    floor_min_micros: int
    floor_max_micros: int
    step_size: int
    drop_tiers: int
    automatic: bool
    updated_at: datetime

    @classmethod
    def of(cls, config: PriceRuleConfig) -> "PriceRuleConfigOut":
        """Monta os limites da regra."""
        return cls(
            pmr_floor=config.pmr_floor,
            pmr_emergency=config.pmr_emergency,
            min_eligible_requests=config.min_eligible_requests,
            floor_min_micros=config.floor_min_micros,
            floor_max_micros=config.floor_max_micros,
            step_size=config.step_size,
            drop_tiers=config.drop_tiers,
            automatic=config.automatic,
            updated_at=config.updated_at,
        )


class PriceRuleDetailsOut(PriceRuleOut):
    # Vazio até a primeira hora do motor.
    config: PriceRuleConfigOut | None
    tiers_micros: list[int]

    @classmethod
    def of_details(cls, details: PriceRuleDetails) -> "PriceRuleDetailsOut":
        """Monta a regra com os limites e os degraus da moeda."""
        config = PriceRuleConfigOut.of(details.config) if details.config else None
        return cls(
            **PriceRuleOut.of(details.rule).model_dump(),
            config=config,
            tiers_micros=list(details.tiers),
        )


class PriceRuleConfigIn(BaseModel):
    pmr_floor: float = Field(ge=0, le=100)
    pmr_emergency: float = Field(ge=0, le=100)
    min_eligible_requests: int = Field(ge=0)
    floor_min_micros: int = Field(ge=0)
    floor_max_micros: int = Field(ge=0)
    step_size: int = Field(ge=1, le=3)
    # Vazio mantém a queda guardada na regra (a Automática ignora).
    drop_tiers: int | None = Field(None, ge=1, le=3)
    automatic: bool = False

    def to_core(self, stored_drop_tiers: int | None) -> PriceRuleConfigInput:
        """Os limites no formato do caso de uso; sem ``drop_tiers`` vale o guardado na regra, e
        sem config ainda, o padrão."""
        drop_tiers = self.drop_tiers or stored_drop_tiers or DEFAULT_DROP_TIERS
        return PriceRuleConfigInput(
            **self.model_dump(exclude={"drop_tiers"}), drop_tiers=drop_tiers
        )


class PriceRuleStatusIn(BaseModel):
    status: PriceRuleStatus


class PriceRuleFloorIn(BaseModel):
    floor_micros: int = Field(ge=0)


class PriceRuleHistoryOut(BaseModel):
    date: date
    hour: int
    action: PriceRuleAction
    reason: PriceRuleReason
    floor_before_micros: int
    floor_applied_micros: int
    created_at: datetime
    data_date: calendar_date | None
    data_hour: int | None

    @classmethod
    def of(cls, entry: PriceRuleHistoryEntry) -> "PriceRuleHistoryOut":
        """Monta uma decisão do histórico."""
        return cls(
            date=entry.date,
            hour=entry.hour,
            action=entry.action,
            reason=entry.reason,
            floor_before_micros=entry.floor_before_micros,
            floor_applied_micros=entry.floor_applied_micros,
            created_at=entry.created_at,
            data_date=entry.data_date,
            data_hour=entry.data_hour,
        )


class PriceRuleHourOut(BaseModel):
    date: date
    hour: int
    eligible_requests: int
    responses_served: int
    impressions: int
    revenue_micros: int
    pmr: float
    ecpm_micros: int

    @classmethod
    def of(cls, row: PriceRuleHour) -> "PriceRuleHourOut":
        """Monta os números do GAM de uma hora da regra."""
        counts = row.counts
        return cls(
            date=row.date,
            hour=row.hour,
            eligible_requests=counts.eligible_requests,
            responses_served=counts.responses_served,
            impressions=counts.impressions,
            revenue_micros=counts.revenue_micros,
            pmr=counts.pmr,
            ecpm_micros=counts.ecpm_micros,
        )


class CascadeTryOut(BaseModel):
    eligible_requests: int
    responses_served: int
    impressions: int
    revenue_micros: int

    @classmethod
    def of(cls, counts: HourlyCounts) -> "CascadeTryOut":
        """Monta os números de uma tentativa da hora."""
        return cls(
            eligible_requests=counts.eligible_requests,
            responses_served=counts.responses_served,
            impressions=counts.impressions,
            revenue_micros=counts.revenue_micros,
        )


class CascadeHourOut(BaseModel):
    date: date
    hour: int
    floor_micros: int
    # As quatro tentativas, da primeira à quarta.
    tries: list[CascadeTryOut]

    @classmethod
    def of(cls, row: CascadeHour) -> "CascadeHourOut":
        """Monta os números das quatro tentativas de uma hora da regra Cascata."""
        return cls(
            date=row.date,
            hour=row.hour,
            floor_micros=row.floor_micros,
            tries=[CascadeTryOut.of(counts) for counts in row.tries],
        )
