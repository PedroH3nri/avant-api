"""Loaders de todos os clientes: /api/v1/internal/loaders.

Ver pede ``internal.ad_tags.view``; mexer pede ``internal.ad_tags.manage``. Toda ação grava na
auditoria do cliente.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.loaders.dependencies import client_loader_service
from avant_api.modules.internal.loaders.dto import (
    ClientLoaderIn,
    LoaderIn,
    LoaderOptionOut,
    LoaderOut,
)
from avant_api.modules.internal.loaders.service import ClientLoaderService
from avant_api.shared.dto import PageOut

VIEW = "internal.ad_tags.view"
MANAGE = "internal.ad_tags.manage"

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/loaders")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    company_id: uuid.UUID | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> PageOut[LoaderOut]:
    """Uma página dos loaders dos clientes (ou de um), o mais novo primeiro."""
    return service.page(actor, page, company_id, query)


@router.get("/loaders/options")
def options(
    company_id: uuid.UUID = Query(),
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> list[LoaderOptionOut]:
    """Os loaders de um cliente pelo nome, para o seletor da ad tag."""
    return service.options(actor, company_id)


@router.post("/loaders", status_code=status.HTTP_201_CREATED)
def create(
    body: ClientLoaderIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> LoaderOut:
    """Cria um loader para um cliente."""
    return service.create(actor, body)


@router.get("/loaders/{loader_id}")
def show(
    loader_id: uuid.UUID,
    actor: Actor = Depends(require_staff(VIEW)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> LoaderOut:
    """Um loader com as tags que o usam."""
    return service.get(actor, loader_id)


@router.put("/loaders/{loader_id}")
def update(
    loader_id: uuid.UUID,
    body: LoaderIn,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> LoaderOut:
    """Troca todos os campos do loader."""
    return service.update(actor, loader_id, body)


@router.delete("/loaders/{loader_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    loader_id: uuid.UUID,
    actor: Actor = Depends(require_staff(MANAGE)),
    service: ClientLoaderService = Depends(client_loader_service),
) -> None:
    """Apaga um loader que nenhuma ad tag usa."""
    service.delete(actor, loader_id)
