"""Service das metas da equipe Groone: chama os casos de uso do avant-core e devolve os DTOs.

O andamento lê os números de todas as Empresas cliente, então usa o Unit of Work sem RLS,
como o resultado dos clientes; o core confere a Company Groone e as permissões.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.goals.services import (
    create_goal_template,
    delete_goal_template,
    list_goal_templates,
    list_role_goals,
    my_goal,
    page_goal_templates,
    set_role_goal,
    team_goals,
    update_goal_template,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.goals.dto import (
    GoalTemplateIn,
    GoalTemplateOut,
    PersonGoalOut,
    RoleGoalIn,
    RoleGoalOut,
    TeamGoalsOut,
)
from avant_api.shared.dto import PageOut, page_out


class GoalService:
    """Modelos de meta, meta dos papéis e andamento do mês."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def template_page(self, actor: Actor, page: int) -> PageOut[GoalTemplateOut]:
        """Uma página dos modelos de meta, do ano mais novo para o mais velho."""
        found = page_goal_templates(self._uows.uow(actor.company_id), actor=actor, page=page)
        return page_out(found, GoalTemplateOut.of)

    def templates(self, actor: Actor) -> list[GoalTemplateOut]:
        """Os modelos de meta, do ano mais novo para o mais velho."""
        items = list_goal_templates(self._uows.uow(actor.company_id), actor=actor)
        return [GoalTemplateOut.of(item) for item in items]

    def create_template(self, actor: Actor, body: GoalTemplateIn) -> GoalTemplateOut:
        """Cadastra um modelo de meta."""
        template = create_goal_template(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return GoalTemplateOut.of(template)

    def update_template(
        self, actor: Actor, template_id: uuid.UUID, body: GoalTemplateIn
    ) -> GoalTemplateOut:
        """Troca nome, ano, valores e a marca de meta da Groone."""
        template = update_goal_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            data=body.input(),
            clock=self._clock,
        )
        return GoalTemplateOut.of(template)

    def delete_template(self, actor: Actor, template_id: uuid.UUID) -> None:
        """Apaga o modelo; os papéis que o usavam ficam sem meta."""
        delete_goal_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            clock=self._clock,
        )

    def role_goals(self, actor: Actor) -> list[RoleGoalOut]:
        """A meta de cada papel da equipe Groone."""
        return [
            RoleGoalOut.of(goal)
            for goal in list_role_goals(self._uows.uow(actor.company_id), actor=actor)
        ]

    def set_role_goal(self, actor: Actor, role_id: uuid.UUID, body: RoleGoalIn) -> None:
        """Põe, troca ou tira a meta de um papel."""
        set_role_goal(
            self._uows.uow(actor.company_id),
            actor=actor,
            role_id=role_id,
            template_id=body.goal_template_id,
            mode=body.goal_mode,
            clock=self._clock,
        )

    def team(self, actor: Actor, month: date) -> TeamGoalsOut:
        """A meta da Groone e a de cada pessoa da equipe no mês."""
        result = team_goals(self._uows.trusted_uow(), actor=actor, month=month, clock=self._clock)
        return TeamGoalsOut.of(month, result)

    def mine(self, actor: Actor, month: date) -> PersonGoalOut:
        """A meta do mês de quem pergunta."""
        return PersonGoalOut.of(
            my_goal(self._uows.trusted_uow(), actor=actor, month=month, clock=self._clock)
        )

    def current_month(self) -> date:
        """O primeiro dia do mês de hoje."""
        return self._clock.now().date().replace(day=1)
