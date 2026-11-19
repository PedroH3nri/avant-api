"""Formatos das rotas do Facebook. Dinheiro sai fora de micros, na moeda da conta."""

import uuid
from datetime import date, datetime
from decimal import Decimal

from avant_core.facebook.enums import (
    FacebookAccountState,
    FacebookAlertKind,
    FacebookChangeOrigin,
    FacebookJobKind,
    FacebookJobState,
    FacebookLevel,
    FacebookOnLimit,
    FacebookProfileStatus,
    FacebookReview,
    FacebookRuleAction,
)
from avant_core.facebook.models import (
    FacebookAccountInput,
    FacebookAccountView,
    FacebookAdAccount,
    FacebookAlertSetting,
    FacebookAlertView,
    FacebookChange,
    FacebookControlResult,
    FacebookCountryTotals,
    FacebookDailyPoint,
    FacebookJob,
    FacebookMedia,
    FacebookObject,
    FacebookObjectDetail,
    FacebookObjectView,
    FacebookOption,
    FacebookPersonView,
    FacebookProfileView,
    FacebookRule,
    FacebookRuleDecision,
    FacebookRuleInput,
    FacebookTotals,
)
from pydantic import BaseModel, Field

from avant_api.shared.ads import MAX_LIMIT, MICROS, PersonRefOut, micros, money


class FacebookProfileOut(BaseModel):
    """O perfil conectado, sem o token, que nunca sai do servidor."""

    id: uuid.UUID
    name: str
    facebook_user_id: str
    status: FacebookProfileStatus
    connected_by: PersonRefOut | None
    connected_at: datetime
    token_expires_at: datetime | None
    last_synced_at: datetime | None
    last_error: str | None
    account_count: int

    @classmethod
    def of(cls, view: FacebookProfileView) -> "FacebookProfileOut":
        """Monta o perfil com quem conectou e quantas contas ele trouxe."""
        profile = view.profile
        return cls(
            id=profile.id,
            name=profile.name,
            facebook_user_id=profile.facebook_user_id,
            status=profile.status,
            connected_by=PersonRefOut.of(view.connected_by),
            connected_at=profile.connected_at,
            token_expires_at=profile.token_expires_at,
            last_synced_at=profile.last_synced_at,
            last_error=profile.last_error,
            account_count=view.account_count,
        )


class FacebookAccountRefOut(BaseModel):
    id: uuid.UUID
    external_id: str
    name: str
    currency: str

    @classmethod
    def of(cls, account: FacebookAdAccount | None) -> "FacebookAccountRefOut | None":
        """A conta resumida, ou vazio."""
        if account is None:
            return None
        return cls(
            id=account.id,
            external_id=account.external_id,
            name=account.name,
            currency=account.currency,
        )


class FacebookAccountOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    external_id: str
    name: str
    business_id: str | None
    business_name: str | None
    currency: str
    time_zone: str
    state: FacebookAccountState
    profile_id: uuid.UUID | None
    profile_name: str | None
    site_id: uuid.UUID | None
    holder: PersonRefOut | None
    daily_limit: Decimal | None
    monthly_limit: Decimal | None
    on_limit: FacebookOnLimit
    month_spend: Decimal
    synced_at: datetime | None

    @classmethod
    def of(cls, view: FacebookAccountView) -> "FacebookAccountOut":
        """Monta a conta com quem usa, o perfil que trouxe e o gasto do mês."""
        account = view.account
        return cls(
            id=account.id,
            company_id=account.company_id,
            external_id=account.external_id,
            name=account.name,
            business_id=account.business_id,
            business_name=account.business_name,
            currency=account.currency,
            time_zone=account.time_zone,
            state=account.state,
            profile_id=account.profile_id,
            profile_name=view.profile_name,
            site_id=account.site_id,
            holder=PersonRefOut.of(view.holder),
            daily_limit=money(account.daily_limit_micros),
            monthly_limit=money(account.monthly_limit_micros),
            on_limit=account.on_limit,
            month_spend=Decimal(view.month_spend_micros) / MICROS,
            synced_at=account.synced_at,
        )


class FacebookAccountIn(BaseModel):
    """Site, quem usa e os limites da conta; vazio é sem site, sem pessoa ou sem limite."""

    site_id: uuid.UUID | None = None
    user_id: uuid.UUID | None = None
    daily_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    monthly_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    on_limit: FacebookOnLimit = FacebookOnLimit.WARN

    def to_core(self) -> FacebookAccountInput:
        """Os campos em micros, como o core grava."""
        return FacebookAccountInput(
            site_id=self.site_id,
            user_id=self.user_id,
            daily_limit_micros=micros(self.daily_limit),
            monthly_limit_micros=micros(self.monthly_limit),
            on_limit=self.on_limit,
        )


class FacebookPersonOut(BaseModel):
    person: PersonRefOut
    account_ids: list[uuid.UUID]
    daily_limit: Decimal | None
    monthly_limit: Decimal | None

    @classmethod
    def of(cls, view: FacebookPersonView) -> "FacebookPersonOut":
        """Monta a pessoa com as contas que usa e os limites dela."""
        limit = view.limit
        person = PersonRefOut.of(view.user)
        assert person is not None
        return cls(
            person=person,
            account_ids=view.account_ids,
            daily_limit=money(limit.daily_limit_micros) if limit else None,
            monthly_limit=money(limit.monthly_limit_micros) if limit else None,
        )


class FacebookPersonIn(BaseModel):
    """As contas que a pessoa passa a usar (tira de quem usava) e os limites dela."""

    account_ids: list[uuid.UUID] = Field(default_factory=list, max_length=500)
    daily_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    monthly_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)


class FacebookTotalsOut(BaseModel):
    """Gasto, receita e lucro na moeda da conta; receita e visitas vazias sem site ligado."""

    spend: Decimal
    impressions: int
    reach: int
    clicks: int
    link_clicks: int
    landing_page_views: int
    cpc: Decimal | None
    ctr: float | None
    revenue: Decimal | None
    visits: int | None
    profit: Decimal | None
    roi: float | None

    @classmethod
    def of(cls, totals: FacebookTotals) -> "FacebookTotalsOut":
        """Monta os números com as contas derivadas (CPC, CTR, lucro e ROI)."""
        return cls(
            spend=Decimal(totals.spend_micros) / MICROS,
            impressions=totals.impressions,
            reach=totals.reach,
            clicks=totals.clicks,
            link_clicks=totals.link_clicks,
            landing_page_views=totals.landing_page_views,
            cpc=money(totals.cpc_micros),
            ctr=totals.ctr,
            revenue=money(totals.revenue_micros),
            visits=totals.visits,
            profit=money(totals.profit_micros),
            roi=totals.roi,
        )


class FacebookObjectOut(BaseModel):
    id: uuid.UUID
    external_id: str
    level: FacebookLevel
    name: str
    parent_external_id: str | None
    campaign_external_id: str
    status: str
    effective_status: str
    active: bool
    objective: str | None
    daily_budget: Decimal | None
    lifetime_budget: Decimal | None
    review: FacebookReview | None
    review_reasons: list[str]
    url_tags: str | None
    synced_at: datetime
    account: FacebookAccountRefOut
    company_id: uuid.UUID
    totals: FacebookTotalsOut

    @classmethod
    def of(cls, view: FacebookObjectView) -> "FacebookObjectOut":
        """Monta a campanha, o conjunto ou o anúncio com a conta e os números do período."""
        item = view.item
        account = FacebookAccountRefOut.of(view.account)
        assert account is not None
        return cls(
            id=item.id,
            external_id=item.external_id,
            level=item.level,
            name=item.name,
            parent_external_id=item.parent_external_id,
            campaign_external_id=item.campaign_external_id,
            status=item.status,
            effective_status=item.effective_status,
            active=item.active,
            objective=item.objective,
            daily_budget=money(item.daily_budget_micros),
            lifetime_budget=money(item.lifetime_budget_micros),
            review=item.review,
            review_reasons=list(item.review_reasons),
            url_tags=item.url_tags,
            synced_at=item.synced_at,
            account=account,
            company_id=item.company_id,
            totals=FacebookTotalsOut.of(view.totals),
        )


class FacebookParentOut(BaseModel):
    external_id: str
    name: str

    @classmethod
    def of(cls, item: FacebookObject | None) -> "FacebookParentOut | None":
        """A campanha ou o conjunto acima, resumido."""
        return None if item is None else cls(external_id=item.external_id, name=item.name)


class FacebookDailyOut(BaseModel):
    day: date
    totals: FacebookTotalsOut

    @classmethod
    def of(cls, point: FacebookDailyPoint) -> "FacebookDailyOut":
        """Os números de um dia."""
        return cls(day=point.day, totals=FacebookTotalsOut.of(point.totals))


class FacebookCountryOut(BaseModel):
    country: str
    totals: FacebookTotalsOut

    @classmethod
    def of(cls, row: FacebookCountryTotals) -> "FacebookCountryOut":
        """Os números de um país."""
        return cls(country=row.country, totals=FacebookTotalsOut.of(row.totals))


class FacebookObjectDetailOut(FacebookObjectOut):
    """O objeto com os números por dia, por país e a campanha e o conjunto acima."""

    daily: list[FacebookDailyOut]
    countries: list[FacebookCountryOut]
    campaign: FacebookParentOut | None
    adset: FacebookParentOut | None

    @classmethod
    def detail(cls, found: FacebookObjectDetail) -> "FacebookObjectDetailOut":
        """Monta o detalhe a partir da visão do core."""
        base = FacebookObjectOut.of(found.view)
        return cls(
            **base.model_dump(),
            daily=[FacebookDailyOut.of(point) for point in found.daily],
            countries=[FacebookCountryOut.of(row) for row in found.countries],
            campaign=FacebookParentOut.of(found.campaign),
            adset=FacebookParentOut.of(found.adset),
        )


class FacebookChangeOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    account_id: uuid.UUID
    origin: FacebookChangeOrigin
    what: str
    data: dict[str, object]
    happened_at: datetime
    object_external_id: str | None
    level: FacebookLevel | None
    object_name: str | None
    user_id: uuid.UUID | None
    actor_name: str | None

    @classmethod
    def of(cls, change: FacebookChange) -> "FacebookChangeOut":
        """Uma linha do histórico: quem mudou o quê, no Avant ou no Facebook."""
        return cls(
            id=change.id,
            company_id=change.company_id,
            account_id=change.account_id,
            origin=change.origin,
            what=change.what,
            data=dict(change.data),
            happened_at=change.happened_at,
            object_external_id=change.object_external_id,
            level=change.level,
            object_name=change.object_name,
            user_id=change.user_id,
            actor_name=change.actor_name,
        )


class FacebookAlertOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    kind: FacebookAlertKind
    created_at: datetime
    account: FacebookAccountRefOut | None
    profile_id: uuid.UUID | None
    object_external_id: str | None
    data: dict[str, object]
    read: bool

    @classmethod
    def of(cls, view: FacebookAlertView) -> "FacebookAlertOut":
        """Um aviso com a conta e se a pessoa já leu; o painel monta o texto pelo ``kind``."""
        alert = view.alert
        return cls(
            id=alert.id,
            company_id=alert.company_id,
            kind=alert.kind,
            created_at=alert.created_at,
            account=FacebookAccountRefOut.of(view.account),
            profile_id=alert.profile_id,
            object_external_id=alert.object_external_id,
            data=dict(alert.data),
            read=view.read,
        )


class FacebookAlertSettingOut(BaseModel):
    """Para cada tipo de aviso, quem recebe (dono, quem usa a conta, quem conectou) e se vai
    também por e-mail."""

    kind: FacebookAlertKind
    owner: bool
    users: bool
    connector: bool
    email: bool

    @classmethod
    def of(cls, setting: FacebookAlertSetting) -> "FacebookAlertSettingOut":
        """Monta a configuração de um tipo de aviso."""
        return cls(
            kind=setting.kind,
            owner=setting.owner,
            users=setting.users,
            connector=setting.connector,
            email=setting.email,
        )

    def to_core(self, company_id: uuid.UUID) -> FacebookAlertSetting:
        """A configuração do tipo de aviso na Empresa."""
        return FacebookAlertSetting(
            company_id=company_id,
            kind=self.kind,
            owner=self.owner,
            users=self.users,
            connector=self.connector,
            email=self.email,
        )


class FacebookStatusIn(BaseModel):
    """Os objetos a ligar (``active``) ou pausar, de 1 a 100."""

    external_ids: list[str] = Field(min_length=1, max_length=100)
    active: bool


class FacebookControlOut(BaseModel):
    """O que mudou e o código do erro de cada objeto que o Facebook recusou."""

    done: list[str]
    failed: dict[str, str]

    @classmethod
    def of(cls, result: FacebookControlResult) -> "FacebookControlOut":
        """Monta a resposta de uma mudança em lote."""
        return cls(done=list(result.done), failed=dict(result.failed))


class FacebookBudgetIn(BaseModel):
    """O orçamento novo na moeda da conta: o diário ou o vitalício, um dos dois."""

    daily_budget: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    lifetime_budget: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)


class FacebookBudgetOut(BaseModel):
    external_id: str
    daily_budget: Decimal | None
    lifetime_budget: Decimal | None

    @classmethod
    def of(cls, item: FacebookObject) -> "FacebookBudgetOut":
        """Os orçamentos do objeto depois da mudança."""
        return cls(
            external_id=item.external_id,
            daily_budget=money(item.daily_budget_micros),
            lifetime_budget=money(item.lifetime_budget_micros),
        )


class FacebookRuleIn(BaseModel):
    """As três regras automáticas; ROI em pontos percentuais, passos em % do orçamento."""

    scale: bool
    up_roi: int
    up_by: int
    down_roi: int
    down_by: int
    pause: bool
    min_roi: int
    days: int
    duplicate: bool
    duplicate_roi: int

    def to_core(self) -> FacebookRuleInput:
        """As regras no formato do caso de uso (o core confere os números)."""
        return FacebookRuleInput(**self.model_dump())


class FacebookRuleOut(FacebookRuleIn):
    object_external_id: str
    level: FacebookLevel
    enabled: bool
    updated_at: datetime
    updated_by: uuid.UUID | None
    last_duplicated_at: datetime | None

    @classmethod
    def of(cls, rule: FacebookRule) -> "FacebookRuleOut":
        """As regras gravadas do objeto, ou as sugeridas desligadas."""
        return cls(
            object_external_id=rule.object_external_id,
            level=rule.level,
            enabled=rule.enabled,
            updated_at=rule.updated_at,
            updated_by=rule.updated_by,
            last_duplicated_at=rule.last_duplicated_at,
            scale=rule.scale,
            up_roi=rule.up_roi,
            up_by=rule.up_by,
            down_roi=rule.down_roi,
            down_by=rule.down_by,
            pause=rule.pause,
            min_roi=rule.min_roi,
            days=rule.days,
            duplicate=rule.duplicate,
            duplicate_roi=rule.duplicate_roi,
        )


class FacebookRuleDecisionOut(BaseModel):
    id: uuid.UUID
    object_external_id: str
    day: date
    action: FacebookRuleAction
    decided_at: datetime
    roi: float | None
    data: dict[str, object]

    @classmethod
    def of(cls, decision: FacebookRuleDecision) -> "FacebookRuleDecisionOut":
        """Uma decisão das regras com o ROI do dia; a tela monta o motivo pela ``action``."""
        return cls(
            id=decision.id,
            object_external_id=decision.object_external_id,
            day=decision.day,
            action=decision.action,
            decided_at=decision.decided_at,
            roi=decision.roi,
            data=dict(decision.data),
        )


class FacebookJobOut(BaseModel):
    """Um job de criar, editar ou duplicar: o passo, os ids criados, o erro e o aviso."""

    id: uuid.UUID
    account_id: uuid.UUID
    kind: FacebookJobKind
    state: FacebookJobState
    step: str | None
    target_external_id: str | None
    created: dict[str, object]
    error_code: str | None
    error_message: str | None
    warning_code: str | None
    created_at: datetime
    updated_at: datetime
    finished_at: datetime | None

    @classmethod
    def of(cls, job: FacebookJob) -> "FacebookJobOut":
        """O job sem o rascunho guardado."""
        return cls(
            id=job.id,
            account_id=job.account_id,
            kind=job.kind,
            state=job.state,
            step=job.step,
            target_external_id=job.target_external_id,
            created=job.created,
            error_code=job.error_code,
            error_message=job.error_message,
            warning_code=job.warning_code,
            created_at=job.created_at,
            updated_at=job.updated_at,
            finished_at=job.finished_at,
        )


class FacebookOptionOut(BaseModel):
    id: str
    name: str
    detail: str

    @classmethod
    def of(cls, option: FacebookOption) -> "FacebookOptionOut":
        """Um item de uma lista do Facebook."""
        return cls(id=option.id, name=option.name, detail=option.detail)


class FacebookMediaOut(BaseModel):
    kind: str
    ref: str

    @classmethod
    def of(cls, media: FacebookMedia) -> "FacebookMediaOut":
        """O hash da imagem ou o id do vídeo enviado à conta."""
        return cls(kind=media.kind, ref=media.ref)
