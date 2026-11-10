"""DTOs da configuração pública da ad tag."""

import uuid

from avant_core.ad_tags.enums import (
    AdTagBlockKind,
    AdTagBlockState,
    AdTagDevice,
    AdTagEdge,
    AdTagRuleMode,
    AdTagSide,
)
from avant_core.ad_tags.models import PublicAdTag, PublicAdTagBlock
from avant_core.loaders.enums import LoaderAdblock, LoaderStyle, LoaderTemplate
from avant_core.loaders.models import Loader
from pydantic import BaseModel, Field


class PublicLoaderOut(BaseModel):
    template: LoaderTemplate
    blur: int
    background: str
    accent: str
    style: LoaderStyle
    text: str | None
    max_seconds: int
    adblock: LoaderAdblock

    @classmethod
    def of(cls, loader: Loader | None) -> "PublicLoaderOut | None":
        """Monta o loader, ou vazio quando a tag não tem."""
        if loader is None:
            return None
        return cls(
            template=loader.template,
            blur=loader.blur,
            background=loader.background,
            accent=loader.accent,
            style=loader.style,
            text=loader.text,
            max_seconds=loader.max_seconds,
            adblock=loader.adblock,
        )


class PublicBlockOut(BaseModel):
    kind: AdTagBlockKind
    # Como no nome do bloco no GAM (Content3, Anchor...).
    unit_type: str
    # Caminhos do googletag; vazio, o bloco não roda no aparelho.
    desktop: str | None
    mobile: str | None
    edge: AdTagEdge | None
    selector: str | None
    side: AdTagSide | None
    refresh_seconds: int | None
    mgid_article: str | None
    rule_mode: AdTagRuleMode
    paths: list[str]

    @classmethod
    def of(cls, item: PublicAdTagBlock) -> "PublicBlockOut":
        """Monta o bloco resolvido, na ordem de carregamento."""
        block = item.block
        return cls(
            kind=block.kind,
            unit_type=block.unit_type,
            desktop=item.desktop_path,
            mobile=item.mobile_path,
            edge=block.edge,
            selector=block.selector,
            side=block.side,
            refresh_seconds=block.refresh_seconds,
            mgid_article=block.mgid_article,
            rule_mode=block.rule_mode,
            paths=list(block.paths),
        )


class PublicMgidOut(BaseModel):
    tag_id: str | None
    smart_widget: str | None
    back_button: str | None
    sidebar: str | None


class PublicAdTagOut(BaseModel):
    key: str
    version: int
    domain: str
    lazy_load: bool
    analytics_id: str | None
    mgid: PublicMgidOut
    reward: bool
    price_rules: bool
    loader: PublicLoaderOut | None
    blocks: list[PublicBlockOut]

    @classmethod
    def of(cls, config: PublicAdTag) -> "PublicAdTagOut":
        """Monta a configuração da versão no ar."""
        settings = config.settings
        return cls(
            key=config.key,
            version=config.version,
            domain=config.domain,
            lazy_load=settings.lazy_load,
            analytics_id=settings.analytics_id,
            mgid=PublicMgidOut(
                tag_id=settings.mgid_tag_id,
                smart_widget=settings.mgid_smart_widget,
                back_button=settings.mgid_back_button,
                sidebar=settings.mgid_sidebar,
            ),
            reward=settings.reward,
            price_rules=settings.price_rules,
            loader=PublicLoaderOut.of(config.loader),
            blocks=[PublicBlockOut.of(block) for block in config.blocks],
        )


class PublicTagOut(BaseModel):
    # Vazio: chave desconhecida, tag pausada, apagada, sem versão no ar ou outro domínio.
    tag: PublicAdTagOut | None


class PageViewBlockIn(BaseModel):
    type: str = Field(max_length=40)
    state: AdTagBlockState


class PageViewIn(BaseModel):
    # O resumo que o tag.js manda uma vez por página (avant-tag, src/page-views).
    key: str = Field(max_length=20)
    url: str = Field(max_length=2000)
    page_view_id: uuid.UUID
    visitor_id: uuid.UUID
    session_id: uuid.UUID
    version: int | None = Field(default=None, ge=1)
    device: AdTagDevice
    language: str | None = Field(default=None, max_length=35)
    referrer: str | None = Field(default=None, max_length=2000)
    visible_ms: int = Field(default=0, ge=0, le=24 * 60 * 60 * 1000)
    scroll_percent: int = Field(default=0, ge=0, le=100)
    clicked: bool = False
    adblock: bool = False
    id_post: str | None = Field(default=None, max_length=64)
    content_hash: str | None = Field(default=None, max_length=128)
    blocks: list[PageViewBlockIn] = Field(default_factory=list, max_length=20)
