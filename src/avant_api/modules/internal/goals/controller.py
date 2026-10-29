"""Metas da equipe Groone: /api/v1/internal/goal-templates, /role-goals e /goals.

Editar modelos e a meta dos papéis pede ``internal.commissions.manage``; ver a meta de toda a
equipe pede ``internal.commissions.view``; cada pessoa da equipe sempre vê a própria meta.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff, require_staff_member
from avant_api.modules.internal.goals.dependencies import goal_service
from avant_api.modules.internal.goals.dto import (
    GoalTemplateIn,
    GoalTemplateOut,
    PersonGoalOut,
    RoleGoalIn,
    RoleGoalOut,
    TeamGoalsOut,
)
from avant_api.modules.internal.goals.service import GoalService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal", tags=["internal"])
MONTH_PATTERN = r"^\d{4}-(0[1-9]|1[0-2])$"
MANAGE = "internal.commissions.manage"


def _month(month: str | None, service: GoalService) -> date:
    """O mês pedido (AAAA-MM) ou o atual."""
    if month is None:
        return service.current_month()
    year, number = month.split("-")
    return date(int(year), int(number), 1)


@router.get("/goal-templates")
def templates(
    actor: Actor = Depends(require_staff_member),
    service: GoalService = Depends(goal_service),
) -> ItemsOut[GoalTemplateOut]:
    """Os modelos de meta (quem edita ou vê as metas)."""
    return ItemsOut(items=service.templates(actor))


@router.post("/goal-templates", status_code=status.HTTP_201_CREATED)
def create_template(
    body: GoalTemplateIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: GoalService = Depends(goal_service),
) -> GoalTemplateOut:
    """Cadastra um modelo de meta; no máximo uma meta da Groone por ano."""
    return service.create_template(actor, body)


@router.put("/goal-templates/{template_id}")
def update_template(
    template_id: uuid.UUID,
    body: GoalTemplateIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: GoalService = Depends(goal_service),
) -> GoalTemplateOut:
    """Troca nome, ano, valores e a marca de meta da Groone."""
    return service.update_template(actor, template_id, body)


@router.delete("/goal-templates/{template_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_template(
    template_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: GoalService = Depends(goal_service),
) -> None:
    """Apaga o modelo; os papéis que o usavam ficam sem meta."""
    service.delete_template(actor, template_id)


@router.get("/role-goals")
def role_goals(
    actor: Actor = Depends(require_staff_member),
    service: GoalService = Depends(goal_service),
) -> ItemsOut[RoleGoalOut]:
    """A meta de cada papel da equipe Groone."""
    return ItemsOut(items=service.role_goals(actor))


@router.put("/roles/{role_id}/goal", status_code=status.HTTP_204_NO_CONTENT)
def set_role_goal(
    role_id: uuid.UUID,
    body: RoleGoalIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: GoalService = Depends(goal_service),
) -> None:
    """Põe, troca ou tira (``goal_template_id`` vazio) a meta de um papel."""
    service.set_role_goal(actor, role_id, body)


@router.get("/goals")
def team(
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    actor: Actor = Depends(require_staff("internal.commissions.view")),
    service: GoalService = Depends(goal_service),
) -> TeamGoalsOut:
    """A meta da Groone e a de cada pessoa da equipe no mês (AAAA-MM, padrão o atual)."""
    return service.team(actor, _month(month, service))


@router.get("/goals/me")
def mine(
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    actor: Actor = Depends(require_staff_member),
    service: GoalService = Depends(goal_service),
) -> PersonGoalOut:
    """A meta do mês de quem pergunta."""
    return service.mine(actor, _month(month, service))
