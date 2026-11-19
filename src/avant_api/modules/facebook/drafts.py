"""Formatos do rascunho e da edição de campanhas (decisão 16, F3).

Aqui só entram tipos e tamanhos; o que falta para o Facebook aceitar (a lista "Para criar") o
core confere e devolve em ``facebook_draft_invalid``. Dinheiro chega na moeda da conta.
"""

import uuid
from datetime import datetime
from decimal import Decimal

from avant_core.facebook.enums import FacebookAdFormat, FacebookObjective
from avant_core.facebook.models import (
    FacebookDraft,
    FacebookDraftAd,
    FacebookDraftAdset,
    FacebookDraftCard,
    FacebookEdit,
    FacebookPick,
)
from pydantic import BaseModel, Field

from avant_api.modules.facebook.dto import MAX_LIMIT, micros

NAME = 400
TEXT = 2_000
ID = 60
SHORT = 40
MAX_ITEMS = 50
MAX_TEXTS = 10
MAX_ADSETS = 20
MAX_ADS = 60


class FacebookPickIn(BaseModel):
    """Um item escolhido numa lista do Facebook: o id que ele deu e o nome para a tela."""

    id: str = Field(min_length=1, max_length=ID)
    name: str = Field(default="", max_length=NAME)
    kind: str = Field(default="", max_length=SHORT)

    def to_core(self) -> FacebookPick:
        """O item no formato do core."""
        return FacebookPick(self.id, self.name, self.kind)


class FacebookCardIn(BaseModel):
    """Um cartão do carrossel com a imagem já enviada."""

    title: str = Field(default="", max_length=NAME)
    path: str = Field(default="", max_length=TEXT)
    image_hash: str = Field(default="", max_length=ID)

    def to_core(self) -> FacebookDraftCard:
        """O cartão no formato do core."""
        return FacebookDraftCard(self.title, self.path, self.image_hash)


class FacebookAdIn(BaseModel):
    """Um anúncio: Página, Instagram, mídia, textos, títulos, caminho no site e botão."""

    name: str = Field(default="", max_length=NAME)
    format: FacebookAdFormat = FacebookAdFormat.IMAGE
    page_id: str = Field(default="", max_length=ID)
    texts: list[str] = Field(default_factory=list, max_length=MAX_TEXTS)
    titles: list[str] = Field(default_factory=list, max_length=MAX_TEXTS)
    path: str = Field(default="", max_length=TEXT)
    call_to_action: str = Field(default="LEARN_MORE", max_length=SHORT)
    instagram_id: str | None = Field(default=None, max_length=ID)
    description: str = Field(default="", max_length=TEXT)
    display_link: str = Field(default="", max_length=NAME)
    image_hash: str | None = Field(default=None, max_length=ID)
    video_id: str | None = Field(default=None, max_length=ID)
    cards: list[FacebookCardIn] = Field(default_factory=list, max_length=MAX_ITEMS)

    def to_core(self) -> FacebookDraftAd:
        """O anúncio no formato do core, com textos e títulos cortados nas pontas."""
        return FacebookDraftAd(
            name=self.name.strip(),
            format=self.format,
            page_id=self.page_id,
            texts=tuple(text[:TEXT] for text in self.texts),
            titles=tuple(title[:NAME] for title in self.titles),
            path=self.path.strip(),
            call_to_action=self.call_to_action,
            instagram_id=self.instagram_id or None,
            description=self.description,
            display_link=self.display_link.strip(),
            image_hash=self.image_hash or None,
            video_id=self.video_id or None,
            cards=tuple(card.to_core() for card in self.cards),
        )


class FacebookAdsetIn(BaseModel):
    """Um conjunto: datas, orçamento (quando fica no conjunto), público, posicionamentos,
    otimização, pixel e os anúncios."""

    name: str = Field(default="", max_length=NAME)
    optimization: str = Field(default="", max_length=SHORT)
    countries: list[str] = Field(default_factory=list, max_length=300)
    ads: list[FacebookAdIn] = Field(default_factory=list, max_length=MAX_ADS)
    start_time: datetime | None = None
    end_time: datetime | None = None
    budget: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    places: list[FacebookPickIn] = Field(default_factory=list, max_length=MAX_ITEMS)
    age_min: int = Field(default=18, ge=13, le=65)
    age_max: int = Field(default=65, ge=13, le=65)
    gender: str = Field(default="all", max_length=SHORT)
    locales: list[FacebookPickIn] = Field(default_factory=list, max_length=MAX_ITEMS)
    advantage_audience: bool = True
    interests: list[FacebookPickIn] = Field(default_factory=list, max_length=MAX_ITEMS)
    audiences: list[FacebookPickIn] = Field(default_factory=list, max_length=MAX_ITEMS)
    excluded_audiences: list[FacebookPickIn] = Field(default_factory=list, max_length=MAX_ITEMS)
    placements: list[str] = Field(default_factory=list, max_length=MAX_ITEMS)
    pixel_id: str | None = Field(default=None, max_length=ID)
    event: str | None = Field(default=None, max_length=SHORT)

    def to_core(self) -> FacebookDraftAdset:
        """O conjunto no formato do core, com o orçamento em micros."""
        return FacebookDraftAdset(
            name=self.name.strip(),
            optimization=self.optimization,
            countries=tuple(country.upper() for country in self.countries),
            ads=tuple(ad.to_core() for ad in self.ads),
            start_time=self.start_time,
            end_time=self.end_time,
            budget_micros=micros(self.budget),
            places=tuple(place.to_core() for place in self.places),
            age_min=self.age_min,
            age_max=self.age_max,
            gender=self.gender,
            locales=tuple(locale.to_core() for locale in self.locales),
            advantage_audience=self.advantage_audience,
            interests=tuple(interest.to_core() for interest in self.interests),
            audiences=tuple(audience.to_core() for audience in self.audiences),
            excluded_audiences=tuple(audience.to_core() for audience in self.excluded_audiences),
            placements=tuple(self.placements),
            pixel_id=self.pixel_id or None,
            event=self.event or None,
        )


class FacebookDraftIn(BaseModel):
    """A campanha nova: conta, objetivo, orçamento, lance, limite de gasto e os conjuntos."""

    account_id: uuid.UUID
    name: str = Field(default="", max_length=NAME)
    objective: FacebookObjective
    adsets: list[FacebookAdsetIn] = Field(default_factory=list, max_length=MAX_ADSETS)
    budget_at: str = Field(default="campaign", max_length=SHORT)
    budget_kind: str = Field(default="daily", max_length=SHORT)
    budget: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    special_categories: list[str] = Field(default_factory=list, max_length=10)
    bid: str = Field(default="volume", max_length=SHORT)
    bid_amount: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    spend_cap: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    start_active: bool = False

    def to_core(self) -> FacebookDraft:
        """O rascunho no formato do core, com o dinheiro em micros."""
        return FacebookDraft(
            name=self.name.strip(),
            objective=self.objective,
            adsets=tuple(adset.to_core() for adset in self.adsets),
            budget_at=self.budget_at,
            budget_kind=self.budget_kind,
            budget_micros=micros(self.budget),
            special_categories=tuple(self.special_categories),
            bid=self.bid,
            bid_micros=micros(self.bid_amount),
            spend_cap_micros=micros(self.spend_cap),
            start_active=self.start_active,
        )


class FacebookEditIn(BaseModel):
    """O que muda: nome e, conforme o nível, limite de gasto, público do conjunto ou anúncio."""

    name: str | None = Field(default=None, max_length=NAME)
    spend_cap: Decimal | None = Field(default=None, gt=0, le=MAX_LIMIT)
    adset: FacebookAdsetIn | None = None
    ad: FacebookAdIn | None = None

    def to_core(self) -> FacebookEdit:
        """A edição no formato do core."""
        return FacebookEdit(
            name=self.name.strip() if self.name is not None else None,
            spend_cap_micros=micros(self.spend_cap),
            adset=self.adset.to_core() if self.adset else None,
            ad=self.ad.to_core() if self.ad else None,
        )
