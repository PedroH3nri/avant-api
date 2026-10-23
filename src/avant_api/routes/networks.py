"""Networks do Google Ad Manager da Empresa ativa: /api/v1/networks.

A API não fala com o GAM: conectar e "sincronizar agora" gravam o pedido e enfileiram
``avant.gam.sync_network`` (teste, sites e ad units) no avant-worker, que tem a chave da
conta de serviço. A tela acompanha pelo estado da network e pelas últimas etapas.
"""

import uuid

from avant_core.company.application import Actor
from avant_core.gam.application import (
    connect_network,
    disconnect_network,
    get_network,
    list_networks,
    list_sync_runs,
    request_sync,
)
from avant_core.gam.domain import Network
from fastapi import APIRouter, Depends, Query, status

from avant_api.deps import get_services, require
from avant_api.schemas import (
    ItemsOut,
    NetworkDetailOut,
    NetworkIn,
    ServiceAccountOut,
    SyncRunOut,
)
from avant_api.services import Services
from avant_api.tasks import SYNC_NETWORK

router = APIRouter(prefix="/networks", tags=["networks"])


def enqueue_sync(services: Services, network: Network) -> None:
    services.tasks.send(SYNC_NETWORK, str(network.company_id), str(network.id))


@router.get("")
def index(
    actor: Actor = Depends(require("network.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[NetworkDetailOut]:
    views = list_networks(services.uow(actor.company_id), actor=actor)
    return ItemsOut(items=[NetworkDetailOut.of_view(v) for v in views])


@router.get("/service-account")
def service_account(
    _: Actor = Depends(require("network.connect")),
    services: Services = Depends(get_services),
) -> ServiceAccountOut:
    return ServiceAccountOut(email=services.settings.gam_service_account_email)


@router.post("", status_code=status.HTTP_202_ACCEPTED)
def connect(
    body: NetworkIn,
    actor: Actor = Depends(require("network.connect")),
    services: Services = Depends(get_services),
) -> NetworkDetailOut:
    """202: a network nasce pendente e o worker testa o acesso em seguida."""
    network = connect_network(
        services.uow(actor.company_id),
        actor=actor,
        network_code=body.network_code,
        clock=services.clock,
    )
    enqueue_sync(services, network)
    view = get_network(services.uow(actor.company_id), actor=actor, network_id=network.id)
    return NetworkDetailOut.of_view(view)


@router.get("/{network_id}")
def show(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.view")),
    services: Services = Depends(get_services),
) -> NetworkDetailOut:
    view = get_network(services.uow(actor.company_id), actor=actor, network_id=network_id)
    return NetworkDetailOut.of_view(view)


@router.post("/{network_id}/sync", status_code=status.HTTP_202_ACCEPTED)
def sync(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.sync")),
    services: Services = Depends(get_services),
) -> NetworkDetailOut:
    """No máximo uma vez a cada 10 minutos (429 com Retry-After)."""
    network = request_sync(
        services.uow(actor.company_id), actor=actor, network_id=network_id, clock=services.clock
    )
    enqueue_sync(services, network)
    view = get_network(services.uow(actor.company_id), actor=actor, network_id=network.id)
    return NetworkDetailOut.of_view(view)


@router.get("/{network_id}/sync-runs")
def sync_runs(
    network_id: uuid.UUID,
    limit: int = Query(default=50, ge=1, le=200),
    actor: Actor = Depends(require("network.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[SyncRunOut]:
    runs = list_sync_runs(
        services.uow(actor.company_id), actor=actor, network_id=network_id, limit=limit
    )
    return ItemsOut(items=[SyncRunOut.of(r) for r in runs])


@router.post("/{network_id}/disconnect")
def disconnect(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.disconnect")),
    services: Services = Depends(get_services),
) -> NetworkDetailOut:
    disconnect_network(
        services.uow(actor.company_id), actor=actor, network_id=network_id, clock=services.clock
    )
    view = get_network(services.uow(actor.company_id), actor=actor, network_id=network_id)
    return NetworkDetailOut.of_view(view)
