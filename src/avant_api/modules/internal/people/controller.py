"""Pessoas no painel interno: /api/v1/internal/users."""

import uuid

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.people.dependencies import people_service
from avant_api.modules.internal.people.dto import PersonOut
from avant_api.modules.internal.people.service import PeopleService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal/users", tags=["internal"])


@router.get("")
def users(
    query: str = Query(alias="q", min_length=3, max_length=120),
    actor: Actor = Depends(require_staff("internal.users.manage")),
    service: PeopleService = Depends(people_service),
) -> ItemsOut[PersonOut]:
    """Busca pessoas por nome ou email."""
    return ItemsOut(items=service.search(actor, query))


@router.post("/{user_id}/disable", status_code=status.HTTP_204_NO_CONTENT)
def disable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    service: PeopleService = Depends(people_service),
) -> None:
    """Desativa a conta de uma pessoa e encerra as sessões dela."""
    service.set_disabled(actor, user_id, disabled=True)


@router.post("/{user_id}/enable", status_code=status.HTTP_204_NO_CONTENT)
def enable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    service: PeopleService = Depends(people_service),
) -> None:
    """Reativa a conta de uma pessoa."""
    service.set_disabled(actor, user_id, disabled=False)


@router.post("/{user_id}/reset-mfa", status_code=status.HTTP_204_NO_CONTENT)
def reset_mfa(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    service: PeopleService = Depends(people_service),
) -> None:
    """Desliga o 2FA de uma pessoa que perdeu o acesso."""
    service.reset_mfa(actor, user_id)
