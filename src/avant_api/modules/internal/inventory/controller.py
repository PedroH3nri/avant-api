"""Networks e sites de todas as Empresas cliente: /api/v1/internal/networks e /sites.

A Groone não tem networks nem sites; os clientes têm. Cada linha leva o cliente e o status de
faturamento, que só a equipe Groone vê.
"""

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require_staff
from avant_api.modules.internal.inventory.dependencies import client_inventory_service
from avant_api.modules.internal.inventory.dto import ClientNetworkOut, ClientSiteOut
from avant_api.modules.internal.inventory.service import ClientInventoryService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/networks")
def networks(
    query: str | None = Query(alias="q", default=None, max_length=120),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientInventoryService = Depends(client_inventory_service),
) -> PageOut[ClientNetworkOut]:
    """Uma página das networks dos clientes, a mais recente primeiro, com busca por nome ou
    código."""
    return service.networks(actor, query, page)


@router.get("/sites")
def sites(
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientInventoryService = Depends(client_inventory_service),
) -> PageOut[ClientSiteOut]:
    """Uma página dos sites dos clientes, o mais recente primeiro, com busca pelo domínio."""
    return service.sites(actor, query, page)
