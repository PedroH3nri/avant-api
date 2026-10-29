"""Equipe Groone: /api/v1/internal/staff."""

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.staff.dependencies import staff_service
from avant_api.modules.internal.staff.dto import StaffInviteIn
from avant_api.modules.internal.staff.service import StaffService
from avant_api.shared.dto import InvitationOut, MemberOut, PageOut

router = APIRouter(prefix="/internal/staff", tags=["internal"])


@router.get("")
def staff(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    service: StaffService = Depends(staff_service),
) -> PageOut[MemberOut]:
    """Uma página da equipe Groone, a mais recente primeiro."""
    return service.list_all(actor, page)


@router.post("/invitations", status_code=status.HTTP_201_CREATED)
def invite(
    body: StaffInviteIn,
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    service: StaffService = Depends(staff_service),
) -> InvitationOut:
    """Convida alguém para a equipe Groone com um papel interno."""
    return service.invite(actor, body)
