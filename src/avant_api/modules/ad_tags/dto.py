"""DTOs das ad tags, usados pelo painel do cliente e pelo interno. Datas em ISO 8601 UTC."""

import uuid
from datetime import date, datetime

from avant_core.ad_tags.enums import (
    AdTagBlockKind,
    AdTagDevice,
    AdTagEdge,
    AdTagRuleMode,
    AdTagSide,
)
from avant_core.ad_tags.models import (
    AdTagBlock,
    AdTagDetails,
    AdTagDraft,
    AdTagHealth,
    AdTagHealthDay,
    AdTagSettings,
    AdTagUnitDay,
    AdTagVersionDetails,
)
from pydantic import BaseModel, Field


class AdTagBlockIO(BaseModel):
    kind: AdTagBlockKind
    desktop: bool = True
    mobile: bool = True
    # Conteúdo de 1 a 9.
    number: int | None = Field(default=None, ge=1, le=9)
    edge: AdTagEdge | None = None
    selector: str | None = Field(default=None, max_length=500)
    side: AdTagSide | None = None
    refresh_seconds: int | None = None
    mgid_article: str | None = Field(default=None, max_length=200)
    rule_mode: AdTagRuleMode = AdTagRuleMode.ALL
    paths: list[str] = Field(default_factory=list, max_length=100)

    @classmethod
    def of(cls, block: AdTagBlock) -> "AdTagBlockIO":
        """Monta o bloco."""
        return cls(**{**block.__dict__, "paths": list(block.paths)})

    def to_core(self) -> AdTagBlock:
        """O bloco no formato do caso de uso."""
        return AdTagBlock(**{**self.model_dump(), "paths": tuple(self.paths)})


class AdTagSettingsIO(BaseModel):
    lazy_load: bool = True
    # Vazio: sempre os blocos mais recentes do GAM.
    ad_unit_day: date | None = None
    analytics_id: str | None = Field(default=None, max_length=200)
    mgid_tag_id: str | None = Field(default=None, max_length=200)
    mgid_smart_widget: str | None = Field(default=None, max_length=200)
    mgid_back_button: str | None = Field(default=None, max_length=200)
    mgid_sidebar: str | None = Field(default=None, max_length=200)
    reward: bool = False
    price_rules: bool = False
    loader_id: uuid.UUID | None = None

    @classmethod
    def of(cls, settings: AdTagSettings) -> "AdTagSettingsIO":
        """Monta as configurações."""
        return cls(**settings.__dict__)

    def to_core(self) -> AdTagSettings:
        """As configurações no formato do caso de uso."""
        return AdTagSettings(**self.model_dump())


class AdTagDraftIO(BaseModel):
    blocks: list[AdTagBlockIO] = Field(default_factory=list, max_length=60)
    settings: AdTagSettingsIO = Field(default_factory=AdTagSettingsIO)

    @classmethod
    def of(cls, draft: AdTagDraft) -> "AdTagDraftIO":
        """Monta o rascunho ou o conteúdo de uma versão."""
        return cls(
            blocks=[AdTagBlockIO.of(block) for block in draft.blocks],
            settings=AdTagSettingsIO.of(draft.settings),
        )

    def to_core(self) -> AdTagDraft:
        """O rascunho no formato do caso de uso."""
        return AdTagDraft(tuple(block.to_core() for block in self.blocks), self.settings.to_core())


class AdTagCreateIn(BaseModel):
    site_id: uuid.UUID
    name: str = Field(max_length=200)


class AdTagIn(BaseModel):
    name: str = Field(max_length=200)
    draft: AdTagDraftIO


class AdTagPublishIn(BaseModel):
    note: str | None = Field(default=None, max_length=500)


class AdTagActiveIn(BaseModel):
    active: bool


class AdTagClientOut(BaseModel):
    id: uuid.UUID
    name: str


class AdTagLiveOut(BaseModel):
    number: int
    published_at: datetime


class AdTagOut(BaseModel):
    id: uuid.UUID
    site_id: uuid.UUID
    domain: str
    # Só no painel interno.
    client: AdTagClientOut | None = None
    name: str
    key: str
    active: bool
    draft: AdTagDraftIO
    # A versão no ar; vazia se a tag nunca foi publicada.
    live: AdTagLiveOut | None
    # O rascunho mudou desde a versão no ar (ou nunca foi publicado).
    has_changes: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, details: AdTagDetails) -> "AdTagOut":
        """Monta a tag com o rascunho, a versão no ar e, no painel interno, o cliente."""
        tag = details.tag
        client = (
            AdTagClientOut(id=tag.company_id, name=details.company_name)
            if details.company_name is not None
            else None
        )
        live = (
            AdTagLiveOut(number=details.live.number, published_at=details.live.published_at)
            if details.live is not None
            else None
        )
        return cls(
            id=tag.id,
            site_id=tag.site_id,
            domain=details.domain,
            client=client,
            name=tag.name,
            key=tag.key,
            active=tag.active,
            draft=AdTagDraftIO.of(details.draft),
            live=live,
            has_changes=details.has_changes,
            created_at=tag.created_at,
            updated_at=tag.updated_at,
        )


class AdTagVersionOut(BaseModel):
    number: int
    note: str | None
    published_at: datetime
    published_by: str | None
    live: bool
    content: AdTagDraftIO

    @classmethod
    def of(cls, details: AdTagVersionDetails) -> "AdTagVersionOut":
        """Monta a versão com quem publicou e o conteúdo."""
        version = details.version
        return cls(
            number=version.number,
            note=version.note,
            published_at=version.published_at,
            published_by=details.author_name,
            live=details.live,
            content=AdTagDraftIO.of(details.draft),
        )


class AdTagUnitOut(BaseModel):
    # Como no nome do bloco: Content1 a Content9, Anchor, Interstitial ou Fixed.
    unit_type: str
    desktop: bool
    mobile: bool


class AdTagUnitDayOut(BaseModel):
    day: date
    units: list[AdTagUnitOut]

    @classmethod
    def of(cls, day: AdTagUnitDay) -> "AdTagUnitDayOut":
        """Monta o dia com os tipos de bloco e os aparelhos de cada um."""
        return cls(
            day=day.day,
            units=[
                AdTagUnitOut(
                    unit_type=unit.unit_type,
                    desktop=unit.desktop_path is not None,
                    mobile=unit.mobile_path is not None,
                )
                for unit in day.units
            ],
        )


class AdTagHealthDayOut(BaseModel):
    day: date
    version: int
    # O tipo do bloco (Content3, Anchor...) ou "page" para a página inteira.
    placement: str
    device: AdTagDevice
    page_views: int
    rendered: int
    empty: int
    last_seen_at: datetime

    @classmethod
    def of(cls, row: AdTagHealthDay) -> "AdTagHealthDayOut":
        """Monta a linha do dia."""
        return cls(
            day=row.day,
            version=row.version,
            placement=row.placement,
            device=row.device,
            page_views=row.page_views,
            rendered=row.rendered,
            empty=row.empty,
            last_seen_at=row.last_seen_at,
        )


class AdTagHealthOut(BaseModel):
    # Vazio: a tag ainda não foi vista em nenhum site.
    last_seen_at: datetime | None
    seen_version: int | None
    days: list[AdTagHealthDayOut]

    @classmethod
    def of(cls, health: AdTagHealth) -> "AdTagHealthOut":
        """Monta a saúde da tag no período."""
        return cls(
            last_seen_at=health.last_seen_at,
            seen_version=health.seen_version,
            days=[AdTagHealthDayOut.of(row) for row in health.days],
        )
