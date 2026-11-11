"""DTOs das rotas públicas do reward: a configuração da página, os eventos e o contato."""

import uuid

from avant_core.rewards.enums import (
    RewardEventKind,
    RewardIconKind,
    RewardLayout,
    RewardLeadKind,
    RewardLeadPosition,
    RewardTrigger,
)
from avant_core.rewards.models import PublicReward
from pydantic import BaseModel, Field

MAX_EVENTS = 20


class PublicIconOut(BaseModel):
    kind: RewardIconKind
    emoji: str | None
    # URL absoluta da imagem, com a versão; vazia sem imagem.
    url: str | None


class PublicStyleOut(BaseModel):
    layout: RewardLayout
    body_color: str
    border_color: str
    title_color: str
    text_color: str
    button_color: str
    button_text_color: str
    border_width: int
    radius: int
    font: str
    shadow: bool


class PublicQuestionOut(BaseModel):
    # Vai de volta nos eventos de resposta e no contato.
    id: uuid.UUID
    title: str
    description: str
    answers: list[str]


class PublicLeadOut(BaseModel):
    kind: RewardLeadKind
    position: RewardLeadPosition
    title: str
    description: str
    button: str


class PublicAdUnitsOut(BaseModel):
    # Caminhos do googletag; um bloco sem aparelho no nome aparece nos dois.
    desktop: list[str]
    mobile: list[str]


class PublicRewardOut(BaseModel):
    id: uuid.UUID
    title: str
    description: str
    button_text: str
    icon: PublicIconOut
    style: PublicStyleOut
    trigger: RewardTrigger
    scroll_percent: int | None
    click_selector: str | None
    cooldown_minutes: int
    redirect_url: str | None
    questions: list[PublicQuestionOut]
    lead: PublicLeadOut | None
    ad_units: PublicAdUnitsOut

    @classmethod
    def of(cls, found: PublicReward, base_url: str) -> "PublicRewardOut":
        """Monta a configuração com a URL absoluta do ícone."""
        reward = found.reward
        icon_url = (
            f"{base_url}/api/reward/icon/{reward.id}?v={reward.icon_version}"
            if reward.icon_kind is RewardIconKind.IMAGE and reward.icon_version
            else None
        )
        lead = reward.lead
        return cls(
            id=reward.id,
            title=reward.title,
            description=reward.description,
            button_text=reward.button_text,
            icon=PublicIconOut(kind=reward.icon_kind, emoji=reward.icon_emoji, url=icon_url),
            style=PublicStyleOut(**reward.style.__dict__),
            trigger=reward.trigger,
            scroll_percent=reward.scroll_percent,
            click_selector=reward.click_selector,
            cooldown_minutes=reward.cooldown_minutes,
            redirect_url=found.redirect_url,
            questions=[
                PublicQuestionOut(
                    id=question.id,
                    title=question.title,
                    description=question.description,
                    answers=list(question.answers),
                )
                for question in found.questions
            ],
            lead=None if lead is None else PublicLeadOut(**lead.__dict__),
            ad_units=PublicAdUnitsOut(
                desktop=list(found.desktop_ad_units), mobile=list(found.mobile_ad_units)
            ),
        )


class PublicRewardPriceOut(BaseModel):
    # Percentual do grupo de controle e, por bloco Rewards*, os três floors da escada do país.
    control_percent: int
    cascades: dict[str, list[str]]


class PublicPageOut(BaseModel):
    # Vazio: a página não tem reward ativo com ad units para mostrar.
    reward: PublicRewardOut | None
    # Vazio: as regras de preço do site estão desligadas.
    price_rules: PublicRewardPriceOut | None = None


class CachedPage(BaseModel):
    # O que o cache guarda por página: o reward e, só para o service, o site e o controle.
    reward: PublicRewardOut | None
    site_id: uuid.UUID | None = None
    control_percent: int | None = None


class RewardEventIn(BaseModel):
    reward_id: uuid.UUID
    kind: RewardEventKind
    # Na etapa: question_1 a question_5 ou lead.
    step: str | None = Field(default=None, max_length=16)
    # Na resposta: o id da pergunta e a resposta de 0 a 2.
    question_id: uuid.UUID | None = None
    answer: int | None = Field(default=None, ge=0, le=2)


class RewardEventsIn(BaseModel):
    events: list[RewardEventIn] = Field(min_length=1, max_length=MAX_EVENTS)


class RewardLeadAnswerIn(BaseModel):
    question_id: uuid.UUID
    answer: int = Field(ge=0, le=2)


class RewardLeadIn(BaseModel):
    reward_id: uuid.UUID
    name: str = Field(max_length=200)
    # E-mail ou telefone, conforme o pedido de contato do reward.
    contact: str = Field(max_length=300)
    # Idioma do navegador (pt, en, es; o resto vira en).
    language: str = Field(default="en", max_length=16)
    # A resposta de cada pergunta respondida; vazia se o contato vem antes das perguntas.
    answers: list[RewardLeadAnswerIn] = Field(default_factory=list, max_length=5)
