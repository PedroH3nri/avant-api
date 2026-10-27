"""Networks do Google Ad Manager da Empresa ativa: /api/v1/networks.

A tela acompanha a sincronização pelo estado da network e pelas últimas etapas.
"""

import uuid

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require
from avant_api.modules.networks.dependencies import network_service
from avant_api.modules.networks.dto import (
    NetworkDetailOut,
    NetworkIn,
    ServiceAccountOut,
    SyncRunOut,
)
from avant_api.modules.networks.service import NetworkService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/networks", tags=["networks"])


@router.get("")
def index(
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> ItemsOut[NetworkDetailOut]:
    """Lista as networks da Empresa ativa."""
    return ItemsOut(items=service.list_all(actor))


@router.get("/service-account")
def service_account(
    _: Actor = Depends(require("network.connect")),
    service: NetworkService = Depends(network_service),
) -> ServiceAccountOut:
    """Devolve o email da conta de serviço que o cliente adiciona no GAM."""
    return ServiceAccountOut(email=service.service_account)


@router.post("", status_code=status.HTTP_202_ACCEPTED)
def connect(
    body: NetworkIn,
    actor: Actor = Depends(require("network.connect")),
    service: NetworkService = Depends(network_service),
) -> NetworkDetailOut:
    """202: a network nasce pendente e o worker testa o acesso em seguida."""
    return service.connect(actor, body)


@router.get("/{network_id}")
def show(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> NetworkDetailOut:
    """Mostra uma network com sites e últimas sincronizações."""
    return service.show(actor, network_id)


@router.post("/{network_id}/sync", status_code=status.HTTP_202_ACCEPTED)
def sync(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.sync")),
    service: NetworkService = Depends(network_service),
) -> NetworkDetailOut:
    """No máximo uma vez a cada 10 minutos (429 com Retry-After)."""
    return service.sync(actor, network_id)


@router.get("/{network_id}/sync-runs")
def sync_runs(
    network_id: uuid.UUID,
    limit: int = Query(default=50, ge=1, le=200),
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> ItemsOut[SyncRunOut]:
    """Lista as sincronizações recentes de uma network."""
    return ItemsOut(items=service.sync_runs(actor, network_id, limit))


@router.post("/{network_id}/disconnect")
def disconnect(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.disconnect")),
    service: NetworkService = Depends(network_service),
) -> NetworkDetailOut:
    """Desconecta uma network da Empresa."""
    return service.disconnect(actor, network_id)
