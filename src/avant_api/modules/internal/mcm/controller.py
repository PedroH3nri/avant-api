"""Networks no painel interno: /api/v1/internal/networks. A equipe cadastra a network do
cliente e confirma a que o cliente cadastrou; as do MCM sem cadastro ficam só como registro
(core#289)."""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.mcm.dependencies import mcm_service
from avant_api.modules.internal.mcm.dto import ClientNetworkIn, McmCandidateOut
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
    """Uma página das networks do MCM que ninguém cadastrou ainda."""
    return service.unassigned(actor, page)


@router.post("", status_code=status.HTTP_202_ACCEPTED)
def register_network(
    body: ClientNetworkIn,
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    service: McmService = Depends(mcm_service),
) -> NetworkOut:
    """Cadastra a network do cliente escolhido, ligada a ele e ao dono, e agenda o teste."""
    return service.register(actor, body.company_id, body.network_code)


@router.post("/{network_id}/confirm", status_code=status.HTTP_202_ACCEPTED)
def confirm_network(
    network_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    service: McmService = Depends(mcm_service),
) -> NetworkOut:
    """Confirma que a network do MCM cadastrada pelo cliente é dele e agenda o teste."""
    return service.confirm(actor, network_id)


@router.post("/{network_id}/reject", status_code=status.HTTP_204_NO_CONTENT)
def reject_network(
    network_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    service: McmService = Depends(mcm_service),
) -> None:
    """Recusa a network do MCM que o cliente cadastrou e não é dele; o código fica livre."""
    service.reject(actor, network_id)
