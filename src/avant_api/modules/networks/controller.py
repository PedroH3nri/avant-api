"""Networks do Google Ad Manager da Empresa ativa: /api/v1/networks.

A tela acompanha a sincronização pelo estado da network e pelas últimas etapas.
"""

import uuid

from avant_core.access.models import Actor
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
from avant_api.shared.dto import ItemsOut, PageOut

router = APIRouter(prefix="/networks", tags=["networks"])


@router.get("")
def index(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> PageOut[NetworkDetailOut]:
    """Uma página das networks da Empresa ativa, a mais recente primeiro."""
    return service.page(actor, page)


@router.get("/options")
def options(
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> ItemsOut[NetworkDetailOut]:
    """Todas as networks da Empresa ativa, para seletores e telas que juntam dados."""
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
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("network.view")),
    service: NetworkService = Depends(network_service),
) -> PageOut[SyncRunOut]:
    """Uma página das sincronizações de uma network, a mais recente primeiro."""
    return service.sync_runs(actor, network_id, page)


@router.post("/{network_id}/disconnect")
def disconnect(
    network_id: uuid.UUID,
    actor: Actor = Depends(require("network.disconnect")),
    service: NetworkService = Depends(network_service),
) -> NetworkDetailOut:
    """Desconecta uma network da Empresa."""
    return service.disconnect(actor, network_id)
