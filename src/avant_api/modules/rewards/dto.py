"""DTOs dos rewards, usados pelo painel do cliente e pelo interno. Datas em ISO 8601 UTC."""

import uuid
from datetime import date, datetime

from avant_core.rewards.enums import (
    RewardIconKind,
    RewardLayout,
    RewardLeadKind,
    RewardLeadPosition,
    RewardTrigger,
)
from avant_core.rewards.models import (
    RewardAdUnitGroup,
    RewardDetails,
    RewardInput,
    RewardLead,
    RewardLeadRequest,
    RewardMetrics,
    RewardQuestion,
    RewardQuestionInput,
    RewardStyle,
)
from pydantic import BaseModel, Field

ICON_PATH = "/api/reward/icon/{reward_id}?v={version}"


class RewardStyleIO(BaseModel):
    layout: RewardLayout = RewardLayout.SIMPLE
    body_color: str = Field(default="#0a213d", max_length=7)
    border_color: str = Field(default="#1e3a5f", max_length=7)
    title_color: str = Field(default="#ffffff", max_length=7)
    text_color: str = Field(default="#c7d2e0", max_length=7)
    button_color: str = Field(default="#1976d2", max_length=7)
    button_text_color: str = Field(default="#ffffff", max_length=7)
    border_width: int = Field(default=1, ge=0, le=6)
    radius: int = Field(default=24, ge=0, le=32)
    font: str = Field(default="Geist", max_length=40)
    shadow: bool = True

    @classmethod
    def of(cls, style: RewardStyle) -> "RewardStyleIO":
        """Monta o corpo da janela."""
        return cls(**style.__dict__)

    def to_core(self) -> RewardStyle:
        """O corpo no formato do caso de uso."""
        return RewardStyle(**self.model_dump())


class RewardLeadIO(BaseModel):
    kind: RewardLeadKind
    position: RewardLeadPosition
    title: str = Field(max_length=200)
    description: str = Field(default="", max_length=500)
    button: str = Field(max_length=80)

    @classmethod
    def of(cls, lead: RewardLeadRequest | None) -> "RewardLeadIO | None":
        """Monta o pedido de contato, ou vazio quando está desligado."""
        return None if lead is None else cls(**lead.__dict__)


class RewardQuestionIn(BaseModel):
    # O id da pergunta que já existe (mantém as métricas e respostas); vazio cria uma nova.
    id: uuid.UUID | None = None
    title: str = Field(max_length=300)
    description: str = Field(default="", max_length=500)
    answers: list[str] = Field(min_length=3, max_length=3)


class RewardQuestionOut(BaseModel):
    id: uuid.UUID
    position: int
    title: str
    description: str
    answers: list[str]

    @classmethod
    def of(cls, question: RewardQuestion) -> "RewardQuestionOut":
        """Monta a pergunta."""
        return cls(
            id=question.id,
            position=question.position,
            title=question.title,
            description=question.description,
            answers=list(question.answers),
        )


class RewardIn(BaseModel):
    site_id: uuid.UUID
    name: str = Field(max_length=200)
    # Caminho da página no domínio do site; a URL inteira do mesmo site também vale.
    page_path: str = Field(max_length=2000)
    title: str = Field(max_length=200)
    description: str = Field(default="", max_length=500)
    button_text: str = Field(max_length=80)
    icon_kind: RewardIconKind = RewardIconKind.EMOJI
    icon_emoji: str | None = Field(default="🎁", max_length=32)
    style: RewardStyleIO = Field(default_factory=RewardStyleIO)
    trigger: RewardTrigger = RewardTrigger.LOAD
    scroll_percent: int | None = None
    click_selector: str | None = Field(default=None, max_length=300)
    cooldown_minutes: int = 30
    # Vazio: sempre os ad units de reward mais recentes do site.
    ad_unit_day: date | None = None
    redirect_path: str | None = Field(default=None, max_length=2000)
    questions: list[RewardQuestionIn] = Field(default_factory=list, max_length=5)
    lead: RewardLeadIO | None = None
    active: bool = True

    def to_core(self) -> RewardInput:
        """O formulário no formato do caso de uso."""
        return RewardInput(
            site_id=self.site_id,
            name=self.name,
            page_path=self.page_path,
            title=self.title,
            description=self.description,
            button_text=self.button_text,
            icon_kind=self.icon_kind,
            icon_emoji=self.icon_emoji,
            style=self.style.to_core(),
            trigger=self.trigger,
            scroll_percent=self.scroll_percent,
            click_selector=self.click_selector,
            cooldown_minutes=self.cooldown_minutes,
            ad_unit_day=self.ad_unit_day,
            redirect_path=self.redirect_path,
            questions=tuple(
                RewardQuestionInput(
                    title=question.title,
                    answers=(question.answers[0], question.answers[1], question.answers[2]),
                    description=question.description,
                    id=question.id,
                )
                for question in self.questions
            ),
            lead=None if self.lead is None else RewardLeadRequest(**self.lead.model_dump()),
            active=self.active,
        )


class RewardActiveIn(BaseModel):
    active: bool


class RewardClientOut(BaseModel):
    id: uuid.UUID
    name: str


class RewardOut(BaseModel):
    id: uuid.UUID
    site_id: uuid.UUID
    domain: str
    # Só no painel interno.
    client: RewardClientOut | None = None
    name: str
    page_path: str
    active: bool
    title: str
    description: str
    button_text: str
    icon_kind: RewardIconKind
    icon_emoji: str | None
    icon_url: str | None
    style: RewardStyleIO
    trigger: RewardTrigger
    scroll_percent: int | None
    click_selector: str | None
    cooldown_minutes: int
    ad_unit_day: date | None
    redirect_path: str | None
    questions: list[RewardQuestionOut]
    lead: RewardLeadIO | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, details: RewardDetails) -> "RewardOut":
        """Monta o reward com as perguntas e, no painel interno, o cliente."""
        reward = details.reward
        icon_url = (
            ICON_PATH.format(reward_id=reward.id, version=reward.icon_version)
            if reward.icon_kind is RewardIconKind.IMAGE and reward.icon_version
            else None
        )
        client = (
            RewardClientOut(id=reward.company_id, name=details.company_name)
            if details.company_name is not None
            else None
        )
        return cls(
            id=reward.id,
            site_id=reward.site_id,
            domain=details.domain,
            client=client,
            name=reward.name,
            page_path=reward.page_path,
            active=reward.active,
            title=reward.title,
            description=reward.description,
            button_text=reward.button_text,
            icon_kind=reward.icon_kind,
            icon_emoji=reward.icon_emoji,
            icon_url=icon_url,
            style=RewardStyleIO.of(reward.style),
            trigger=reward.trigger,
            scroll_percent=reward.scroll_percent,
            click_selector=reward.click_selector,
            cooldown_minutes=reward.cooldown_minutes,
            ad_unit_day=reward.ad_unit_day,
            redirect_path=reward.redirect_path,
            questions=[RewardQuestionOut.of(question) for question in details.questions],
            lead=RewardLeadIO.of(reward.lead),
            created_at=reward.created_at,
            updated_at=reward.updated_at,
        )


class RewardAdUnitOut(BaseModel):
    name: str
    desktop: bool
    mobile: bool


class RewardAdUnitGroupOut(BaseModel):
    day: date
    desktop: bool
    mobile: bool
    ad_units: list[RewardAdUnitOut]

    @classmethod
    def of(cls, group: RewardAdUnitGroup) -> "RewardAdUnitGroupOut":
        """Monta o grupo de ad units de um dia, com os aparelhos."""
        return cls(
            day=group.day,
            desktop=group.desktop,
            mobile=group.mobile,
            ad_units=[
                RewardAdUnitOut(name=unit.name, desktop=unit.desktop, mobile=unit.mobile)
                for unit in group.ad_units
            ],
        )


class RewardDayOut(BaseModel):
    day: date
    opens: int
    clicks: int
    completed: int
    closed: int


class RewardAnswerOut(BaseModel):
    question_id: uuid.UUID
    answer: int
    count: int


class RewardMetricsOut(BaseModel):
    start: date
    end: date
    total: RewardDayOut
    days: list[RewardDayOut]
    # Etapas ``question_1`` a ``question_5`` e ``lead``: quantas pessoas chegaram ao fim delas.
    steps: dict[str, int]
    answers: list[RewardAnswerOut]

    @classmethod
    def of(cls, metrics: RewardMetrics) -> "RewardMetricsOut":
        """Monta as métricas do período."""
        return cls(
            start=metrics.start,
            end=metrics.end,
            total=RewardDayOut(**metrics.total.__dict__),
            days=[RewardDayOut(**day.__dict__) for day in metrics.days],
            steps=metrics.steps,
            answers=[RewardAnswerOut(**answer.__dict__) for answer in metrics.answers],
        )


class RewardLeadAnswerOut(BaseModel):
    question_id: uuid.UUID
    answer: int


class RewardLeadOut(BaseModel):
    id: uuid.UUID
    name: str
    contact: str
    kind: RewardLeadKind
    language: str
    # A resposta (0 a 2) de cada pergunta respondida; vazia se o contato veio antes.
    answers: list[RewardLeadAnswerOut]
    created_at: datetime

    @classmethod
    def of(cls, lead: RewardLead) -> "RewardLeadOut":
        """Monta o contato."""
        return cls(
            id=lead.id,
            name=lead.name,
            contact=lead.contact,
            kind=lead.kind,
            language=lead.language,
            answers=[
                RewardLeadAnswerOut(question_id=question_id, answer=answer)
                for question_id, answer in zip(lead.question_ids, lead.answers, strict=True)
            ],
            created_at=lead.created_at,
        )
