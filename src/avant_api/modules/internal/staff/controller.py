"""Equipe Groone: /api/v1/internal/staff."""

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.staff.dependencies import staff_service
from avant_api.modules.internal.staff.dto import StaffInviteIn
from avant_api.modules.internal.staff.service import StaffService
from avant_api.shared.dto import InvitationOut, ItemsOut, MemberOut

router = APIRouter(prefix="/internal/staff", tags=["internal"])


@router.get("")
def staff(
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    service: StaffService = Depends(staff_service),
) -> ItemsOut[MemberOut]:
    """Lista a equipe Groone."""
    return ItemsOut(items=service.list_all(actor))


@router.post("/invitations", status_code=status.HTTP_201_CREATED)
def invite(
    body: StaffInviteIn,
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    service: StaffService = Depends(staff_service),
) -> InvitationOut:
    """Convida alguém para a equipe Groone com um papel interno."""
    return service.invite(actor, body)
