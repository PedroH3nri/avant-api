"""MCM sem dono: /api/v1/internal/networks."""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.mcm.dependencies import mcm_service
from avant_api.modules.internal.mcm.dto import AssignNetworkIn, McmCandidateOut
from avant_api.modules.internal.mcm.service import McmService
from avant_api.modules.networks.dto import NetworkOut
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal/networks", tags=["internal"])


@router.get("/unassigned")
def unassigned_networks(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    service: McmService = Depends(mcm_service),
) -> PageOut[McmCandidateOut]:
    """Uma página das networks MCM aprovadas cujo e-mail não é dono de nenhuma Empresa."""
    return service.unassigned(actor, page)


@router.post("/{candidate_id}/assign", status_code=status.HTTP_202_ACCEPTED)
def assign_network(
    candidate_id: uuid.UUID,
    body: AssignNetworkIn,
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    service: McmService = Depends(mcm_service),
) -> NetworkOut:
    """Liga uma network do MCM a uma Empresa e agenda a primeira sincronização."""
    return service.assign(actor, candidate_id, body.company_id)
