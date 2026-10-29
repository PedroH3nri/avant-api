"""DTOs das metas da equipe Groone. Valores em dólar, como texto decimal; datas em ISO 8601 UTC."""

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Annotated

from avant_core.goals.enums import GoalMode
from avant_core.goals.models import GoalProgress, GoalTemplate, PersonGoal, RoleGoal, TeamGoals
from avant_core.goals.services import GoalTemplateInput
from pydantic import BaseModel, Field

MONTHS_IN_YEAR = 12


class GoalTemplateIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    year: int = Field(ge=2020, le=2100)
    # Um valor por mês, de janeiro a dezembro.
    months: list[Annotated[Decimal, Field(ge=0, max_digits=18, decimal_places=2)]] = Field(
        min_length=MONTHS_IN_YEAR, max_length=MONTHS_IN_YEAR
    )
    # A meta da Groone inteira (no máximo uma por ano).
    is_company_goal: bool = False

    def input(self) -> GoalTemplateInput:
        """O formulário no formato do caso de uso."""
        return GoalTemplateInput(self.name, self.year, tuple(self.months), self.is_company_goal)


class GoalTemplateOut(BaseModel):
    id: uuid.UUID
    name: str
    year: int
    currency: str
    months: list[Decimal]
    is_company_goal: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, template: GoalTemplate) -> "GoalTemplateOut":
        """Monta o modelo de meta."""
        return cls(
            id=template.id,
            name=template.name,
            year=template.year,
            currency=template.currency,
            months=list(template.months),
            is_company_goal=template.is_company_goal,
            created_at=template.created_at,
            updated_at=template.updated_at,
        )


class RoleGoalIn(BaseModel):
    # Vazio tira a meta do papel.
    goal_template_id: uuid.UUID | None
    goal_mode: GoalMode = GoalMode.PER_MEMBER


class RoleGoalOut(BaseModel):
    role_id: uuid.UUID
    goal_template_id: uuid.UUID
    goal_mode: GoalMode

    @classmethod
    def of(cls, goal: RoleGoal) -> "RoleGoalOut":
        """Monta a meta do papel."""
        return cls(
            role_id=goal.role_id, goal_template_id=goal.goal_template_id, goal_mode=goal.goal_mode
        )


class GoalProgressOut(BaseModel):
    done: Decimal
    goal: Decimal | None
    # Fração da meta já feita (0,5 = metade).
    share: Decimal | None
    # Se o realizado acompanha os dias que já passaram; vazio no primeiro dia ou sem meta.
    on_pace: bool | None
    projected: Decimal | None

    @classmethod
    def of(cls, progress: GoalProgress) -> "GoalProgressOut":
        """Monta o andamento."""
        return cls(
            done=progress.done,
            goal=progress.goal,
            share=progress.share,
            on_pace=progress.on_pace,
            projected=progress.projected,
        )


class PersonGoalOut(BaseModel):
    user_id: uuid.UUID
    name: str
    role_name: str | None
    mode: GoalMode | None
    progress: GoalProgressOut

    @classmethod
    def of(cls, person: PersonGoal) -> "PersonGoalOut":
        """Monta a meta da pessoa."""
        return cls(
            user_id=person.user_id,
            name=person.name,
            role_name=person.role_name,
            mode=person.mode,
            progress=GoalProgressOut.of(person.progress),
        )


class TeamGoalsOut(BaseModel):
    # Mês no formato AAAA-MM.
    month: str
    company: GoalProgressOut
    people: list[PersonGoalOut]

    @classmethod
    def of(cls, month: date, team: TeamGoals) -> "TeamGoalsOut":
        """Monta a meta da Groone e a de cada pessoa."""
        return cls(
            month=month.strftime("%Y-%m"),
            company=GoalProgressOut.of(team.company),
            people=[PersonGoalOut.of(person) for person in team.people],
        )
