"""Formatos das rotas do Google Ads. Dinheiro sai fora de micros, na moeda da conta."""

import uuid
from datetime import date, datetime
from decimal import Decimal

from avant_core.google_ads.enums import (
    GoogleAdsAccountStatus,
    GoogleAdsAlertKind,
    GoogleAdsChangeOrigin,
    GoogleAdsLevel,
    GoogleAdsLoginStatus,
    GoogleAdsOnLimit,
    GoogleAdsReview,
    GoogleAdsSuffixState,
)
from avant_core.google_ads.models import (
    GoogleAdsAccount,
    GoogleAdsAccountInput,
    GoogleAdsAccountView,
    GoogleAdsAlertSetting,
    GoogleAdsAlertView,
    GoogleAdsChange,
    GoogleAdsDailyPoint,
    GoogleAdsKeywordView,
    GoogleAdsLoginView,
    GoogleAdsObject,
    GoogleAdsObjectDetail,
    GoogleAdsObjectView,
    GoogleAdsPersonView,
    GoogleAdsTermTotals,
    GoogleAdsTotals,
)
from pydantic import BaseModel, Field

from avant_api.shared.ads import MAX_LIMIT, MICROS, PersonRefOut, micros, money


class GoogleAdsLoginOut(BaseModel):
    """O login do Google conectado, sem o token, que nunca sai do servidor."""

    id: uuid.UUID
    email: str
    google_user_id: str
    status: GoogleAdsLoginStatus
    connected_by: PersonRefOut | None
    connected_at: datetime
    last_synced_at: datetime | None
    last_error: str | None
    account_count: int

    @classmethod
    def of(cls, view: GoogleAdsLoginView) -> "GoogleAdsLoginOut":
        """Monta o login com quem conectou e quantas contas ele trouxe."""
        login = view.login
        return cls(
            id=login.id,
            email=login.email,
            google_user_id=login.google_user_id,
            status=login.status,
            connected_by=PersonRefOut.of(view.connected_by),
            connected_at=login.connected_at,
            last_synced_at=login.last_synced_at,
            last_error=login.last_error,
            account_count=view.account_count,
        )


class GoogleAdsAccountRefOut(BaseModel):
    id: uuid.UUID
    customer_id: str
    name: str
    currency: str

    @classmethod
    def of(cls, account: GoogleAdsAccount | None) -> "GoogleAdsAccountRefOut | None":
        """A conta resumida, ou vazio."""
        if account is None:
            return None
        return cls(
            id=account.id,
            customer_id=account.customer_id,
            name=account.name,
            currency=account.currency,
        )


class GoogleAdsAccountOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    customer_id: str
    name: str
    manager_customer_id: str | None
    manager_name: str | None
    currency: str
    time_zone: str
    status: GoogleAdsAccountStatus
    login_id: uuid.UUID | None
    login_email: str | None
    suffix_state: GoogleAdsSuffixState
    url_suffix: str | None
    site_id: uuid.UUID | None
    holder: PersonRefOut | None
    daily_limit: Decimal | None
    monthly_limit: Decimal | None
    on_limit: GoogleAdsOnLimit
    month_spend: Decimal
    synced_at: datetime | None

    @classmethod
    def of(cls, view: GoogleAdsAccountView) -> "GoogleAdsAccountOut":
        """Monta a conta com quem usa, o login que trouxe, o sufixo e o gasto do mês."""
        account = view.account
        return cls(
            id=account.id,
            company_id=account.company_id,
            customer_id=account.customer_id,
            name=account.name,
            manager_customer_id=account.manager_customer_id,
            manager_name=account.manager_name,
            currency=account.currency,
            time_zone=account.time_zone,
            status=account.status,
            login_id=account.login_id,
            login_email=view.login_email,
            suffix_state=account.suffix_state,
            url_suffix=account.url_suffix,
            site_id=account.site_id,
            holder=PersonRefOut.of(view.holder),
            daily_limit=money(account.daily_limit_micros),
            monthly_limit=money(account.monthly_limit_micros),
            on_limit=account.on_limit,
            month_spend=Decimal(view.month_spend_micros) / MICROS,
            synced_at=account.synced_at,
        )


class GoogleAdsAccountIn(BaseModel):
    """Site, quem usa e os limites da conta; vazio é sem site, sem pessoa ou sem limite."""

    site_id: uuid.UUID | None = None
    user_id: uuid.UUID | None = None
    daily_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    monthly_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    on_limit: GoogleAdsOnLimit = GoogleAdsOnLimit.WARN

    def to_core(self) -> GoogleAdsAccountInput:
        """Os campos em micros, como o core grava."""
        return GoogleAdsAccountInput(
            site_id=self.site_id,
            user_id=self.user_id,
            daily_limit_micros=micros(self.daily_limit),
            monthly_limit_micros=micros(self.monthly_limit),
            on_limit=self.on_limit,
        )


class GoogleAdsPersonOut(BaseModel):
    person: PersonRefOut
    account_ids: list[uuid.UUID]
    daily_limit: Decimal | None
    monthly_limit: Decimal | None

    @classmethod
    def of(cls, view: GoogleAdsPersonView) -> "GoogleAdsPersonOut":
        """Monta a pessoa com as contas que usa e os limites dela no Google Ads."""
        limit = view.limit
        person = PersonRefOut.of(view.user)
        assert person is not None
        return cls(
            person=person,
            account_ids=view.account_ids,
            daily_limit=money(limit.daily_limit_micros) if limit else None,
            monthly_limit=money(limit.monthly_limit_micros) if limit else None,
        )


class GoogleAdsPersonIn(BaseModel):
    """As contas que a pessoa passa a usar (tira de quem usava) e os limites dela."""

    account_ids: list[uuid.UUID] = Field(default_factory=list, max_length=500)
    daily_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)
    monthly_limit: Decimal | None = Field(default=None, gt=0, lt=MAX_LIMIT, decimal_places=2)


class GoogleAdsTotalsOut(BaseModel):
    """Gasto, receita e lucro na moeda da conta; receita e visitas vazias sem site ligado."""

    spend: Decimal
    impressions: int
    clicks: int
    conversions: float
    cpc: Decimal | None
    ctr: float | None
    revenue: Decimal | None
    visits: int | None
    profit: Decimal | None
    roi: float | None

    @classmethod
    def of(cls, totals: GoogleAdsTotals) -> "GoogleAdsTotalsOut":
        """Monta os números com as contas derivadas (CPC, CTR, lucro e ROI)."""
        return cls(
            spend=Decimal(totals.spend_micros) / MICROS,
            impressions=totals.impressions,
            clicks=totals.clicks,
            conversions=totals.conversions,
            cpc=money(totals.cpc_micros),
            ctr=totals.ctr,
            revenue=money(totals.revenue_micros),
            visits=totals.visits,
            profit=money(totals.profit_micros),
            roi=totals.roi,
        )


class GoogleAdsObjectOut(BaseModel):
    id: uuid.UUID
    external_id: str
    level: GoogleAdsLevel
    name: str
    parent_external_id: str | None
    campaign_external_id: str
    status: str
    active: bool
    channel_type: str | None
    bidding_strategy: str | None
    budget: Decimal | None
    cpc_bid: Decimal | None
    ad_type: str | None
    final_url: str | None
    review: GoogleAdsReview | None
    review_reasons: list[str]
    synced_at: datetime
    account: GoogleAdsAccountRefOut
    company_id: uuid.UUID
    totals: GoogleAdsTotalsOut

    @classmethod
    def of(cls, view: GoogleAdsObjectView) -> "GoogleAdsObjectOut":
        """Monta a campanha, o grupo ou o anúncio com a conta e os números do período."""
        item = view.item
        account = GoogleAdsAccountRefOut.of(view.account)
        assert account is not None
        return cls(
            id=item.id,
            external_id=item.external_id,
            level=item.level,
            name=item.name,
            parent_external_id=item.parent_external_id,
            campaign_external_id=item.campaign_external_id,
            status=item.status,
            active=item.active,
            channel_type=item.channel_type,
            bidding_strategy=item.bidding_strategy,
            budget=money(item.budget_micros),
            cpc_bid=money(item.cpc_bid_micros),
            ad_type=item.ad_type,
            final_url=item.final_url,
            review=item.review,
            review_reasons=list(item.review_reasons),
            synced_at=item.synced_at,
            account=account,
            company_id=item.company_id,
            totals=GoogleAdsTotalsOut.of(view.totals),
        )


class GoogleAdsParentOut(BaseModel):
    external_id: str
    name: str

    @classmethod
    def of(cls, item: GoogleAdsObject | None) -> "GoogleAdsParentOut | None":
        """A campanha ou o grupo acima, resumido."""
        return None if item is None else cls(external_id=item.external_id, name=item.name)


class GoogleAdsDailyOut(BaseModel):
    day: date
    totals: GoogleAdsTotalsOut

    @classmethod
    def of(cls, point: GoogleAdsDailyPoint) -> "GoogleAdsDailyOut":
        """Os números de um dia."""
        return cls(day=point.day, totals=GoogleAdsTotalsOut.of(point.totals))


class GoogleAdsObjectDetailOut(GoogleAdsObjectOut):
    """O objeto com os números por dia e a campanha e o grupo acima."""

    daily: list[GoogleAdsDailyOut]
    campaign: GoogleAdsParentOut | None
    ad_group: GoogleAdsParentOut | None

    @classmethod
    def detail(cls, found: GoogleAdsObjectDetail) -> "GoogleAdsObjectDetailOut":
        """Monta o detalhe a partir da visão do core."""
        base = GoogleAdsObjectOut.of(found.view)
        return cls(
            **base.model_dump(),
            daily=[GoogleAdsDailyOut.of(point) for point in found.daily],
            campaign=GoogleAdsParentOut.of(found.campaign),
            ad_group=GoogleAdsParentOut.of(found.ad_group),
        )


class GoogleAdsKeywordOut(BaseModel):
    id: uuid.UUID
    criterion_id: str
    target_id: str
    ad_group_external_id: str
    campaign_external_id: str
    text: str
    match_type: str
    status: str
    active: bool
    cpc_bid: Decimal | None
    quality_score: int | None
    totals: GoogleAdsTotalsOut

    @classmethod
    def of(cls, view: GoogleAdsKeywordView) -> "GoogleAdsKeywordOut":
        """Monta a palavra-chave com os números e a receita da ``utm_keyword``."""
        keyword = view.keyword
        return cls(
            id=keyword.id,
            criterion_id=keyword.criterion_id,
            target_id=keyword.target_id,
            ad_group_external_id=keyword.ad_group_external_id,
            campaign_external_id=keyword.campaign_external_id,
            text=keyword.text,
            match_type=keyword.match_type,
            status=keyword.status,
            active=keyword.active,
            cpc_bid=money(keyword.cpc_bid_micros),
            quality_score=keyword.quality_score,
            totals=GoogleAdsTotalsOut.of(view.totals),
        )


class GoogleAdsTermOut(BaseModel):
    """Um termo de pesquisa (com a palavra-chave que casou) ou um posicionamento (com o tipo)."""

    text: str
    detail: str
    totals: GoogleAdsTotalsOut

    @classmethod
    def of(cls, row: GoogleAdsTermTotals) -> "GoogleAdsTermOut":
        """Monta a linha com os números do período."""
        return cls(text=row.text, detail=row.detail, totals=GoogleAdsTotalsOut.of(row.totals))


class GoogleAdsChangeOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    account_id: uuid.UUID
    origin: GoogleAdsChangeOrigin
    what: str
    data: dict[str, object]
    happened_at: datetime
    object_external_id: str | None
    level: GoogleAdsLevel | None
    object_name: str | None
    user_id: uuid.UUID | None
    actor_name: str | None

    @classmethod
    def of(cls, change: GoogleAdsChange) -> "GoogleAdsChangeOut":
        """Uma linha do histórico: quem mudou o quê, no Avant ou no Google Ads."""
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


class GoogleAdsAlertOut(BaseModel):
    id: uuid.UUID
    company_id: uuid.UUID
    kind: GoogleAdsAlertKind
    created_at: datetime
    account: GoogleAdsAccountRefOut | None
    login_id: uuid.UUID | None
    object_external_id: str | None
    data: dict[str, object]
    read: bool

    @classmethod
    def of(cls, view: GoogleAdsAlertView) -> "GoogleAdsAlertOut":
        """Um aviso com a conta e se a pessoa já leu; o painel monta o texto pelo ``kind``."""
        alert = view.alert
        return cls(
            id=alert.id,
            company_id=alert.company_id,
            kind=alert.kind,
            created_at=alert.created_at,
            account=GoogleAdsAccountRefOut.of(view.account),
            login_id=alert.login_id,
            object_external_id=alert.object_external_id,
            data=dict(alert.data),
            read=view.read,
        )


class GoogleAdsAlertSettingOut(BaseModel):
    """Para cada tipo de aviso, quem recebe (dono, quem usa a conta, quem conectou) e se vai
    também por e-mail."""

    kind: GoogleAdsAlertKind
    owner: bool
    users: bool
    connector: bool
    email: bool

    @classmethod
    def of(cls, setting: GoogleAdsAlertSetting) -> "GoogleAdsAlertSettingOut":
        """Monta a configuração de um tipo de aviso."""
        return cls(
            kind=setting.kind,
            owner=setting.owner,
            users=setting.users,
            connector=setting.connector,
            email=setting.email,
        )

    def to_core(self, company_id: uuid.UUID) -> GoogleAdsAlertSetting:
        """A configuração do tipo de aviso na Empresa."""
        return GoogleAdsAlertSetting(
            company_id=company_id,
            kind=self.kind,
            owner=self.owner,
            users=self.users,
            connector=self.connector,
            email=self.email,
        )
