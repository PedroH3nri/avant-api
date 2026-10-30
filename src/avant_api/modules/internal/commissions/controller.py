"""Comissão da equipe Groone: /api/v1/internal/roles/{id}/commission-rules e /commissions.

Regras, data de início, emissão e desconto pedem ``internal.commissions.manage``; a comissão
da equipe pede ``internal.commissions.view``; cada pessoa da equipe sempre vê a própria.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff, require_staff_member
from avant_api.modules.internal.commissions.dependencies import commission_service
from avant_api.modules.internal.commissions.dto import (
    MONTH_PATTERN,
    AdjustmentIn,
    CommissionRuleIn,
    CommissionRuleOut,
    CommissionSettingsIn,
    CommissionSettingsOut,
    IssuedOut,
    MonthIn,
    MyCommissionsOut,
    PersonMonthOut,
    WindowMonthOut,
)
from avant_api.modules.internal.commissions.service import CommissionService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal", tags=["internal"])
MANAGE = "internal.commissions.manage"
VIEW = "internal.commissions.view"


def _month(month: str | None, service: CommissionService) -> date:
    """O mês pedido (AAAA-MM) ou o atual."""
    return MonthIn(month=month).first_day() if month else service.current_month()


@router.get("/roles/{role_id}/commission-rules")
def rules(
    role_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: CommissionService = Depends(commission_service),
) -> ItemsOut[CommissionRuleOut]:
    """As regras de comissão de um papel da equipe Groone, na ordem dos eventos."""
    return ItemsOut(items=service.rules(actor, role_id))


@router.post("/roles/{role_id}/commission-rules", status_code=status.HTTP_201_CREATED)
def create_rule(
    role_id: uuid.UUID,
    body: CommissionRuleIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> CommissionRuleOut:
    """Uma regra por evento no papel (409 ``commission_rule_taken`` se já existe)."""
    return service.save_rule(actor, role_id, body, None)


@router.put("/roles/{role_id}/commission-rules/{rule_id}")
def update_rule(
    role_id: uuid.UUID,
    rule_id: uuid.UUID,
    body: CommissionRuleIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> CommissionRuleOut:
    """Troca a regra; vale do dia seguinte em diante para os prazos abertos."""
    return service.save_rule(actor, role_id, body, rule_id)


@router.delete("/commission-rules/{rule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_rule(
    rule_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> None:
    """Apaga a regra; os prazos dela param e o que já foi calculado fica."""
    service.delete_rule(actor, rule_id)


@router.get("/commissions/settings")
def settings(
    actor: Actor = Depends(require_staff_member),
    service: CommissionService = Depends(commission_service),
) -> CommissionSettingsOut:
    """A data de início da comissão no Avant (vazia enquanto não foi configurada)."""
    return service.settings(actor)


@router.put("/commissions/settings")
def set_settings(
    body: CommissionSettingsIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> CommissionSettingsOut:
    """Grava a data de início e abre os prazos de cadastro do que já existia."""
    return service.set_start(actor, body.starts_on)


@router.get("/commissions/me")
def mine(
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    actor: Actor = Depends(require_staff_member),
    service: CommissionService = Depends(commission_service),
) -> MyCommissionsOut:
    """A comissão de quem pede: prazos, o mês (AAAA-MM; padrão o atual) e o histórico."""
    return service.mine(actor, _month(month, service))


@router.get("/commissions")
def team(
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    actor: Actor = Depends(require_staff(VIEW)),
    service: CommissionService = Depends(commission_service),
) -> ItemsOut[PersonMonthOut]:
    """A comissão de cada pessoa da equipe Groone no mês, pelo nome."""
    return ItemsOut(items=service.team(actor, _month(month, service)))


@router.get("/commissions/people/{user_id}")
def person(
    user_id: uuid.UUID,
    month: str | None = Query(default=None, pattern=MONTH_PATTERN),
    actor: Actor = Depends(require_staff_member),
    service: CommissionService = Depends(commission_service),
) -> ItemsOut[WindowMonthOut]:
    """Os prazos de uma pessoa com o que geraram no mês (a própria pessoa vê sem permissão)."""
    return ItemsOut(items=service.person(actor, user_id, _month(month, service)))


@router.post("/commissions/people/{user_id}/issue")
def issue(
    user_id: uuid.UUID,
    body: MonthIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> IssuedOut:
    """Marca o mês fechado da pessoa como emitido (422 se ainda não fechou)."""
    return service.issue(actor, user_id, body.first_day())


@router.post("/commissions/people/{user_id}/adjustments", status_code=status.HTTP_201_CREATED)
def adjust(
    user_id: uuid.UUID,
    body: AdjustmentIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: CommissionService = Depends(commission_service),
) -> None:
    """Desconto na comissão do mês ainda não emitido da pessoa, com o motivo."""
    service.adjust(actor, user_id, body)
