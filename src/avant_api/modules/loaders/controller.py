"""Loaders da Empresa ativa: /api/v1/loaders.

Valem as permissões das ad tags: ver pede ``ad_tags.view``; criar, editar e apagar pedem
``ad_tags.manage``. Salvar um loader limpa o cache das tags que o usam.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require
from avant_api.modules.loaders.dependencies import loader_service
from avant_api.modules.loaders.dto import LoaderIn, LoaderOptionOut, LoaderOut
from avant_api.modules.loaders.service import LoaderService
from avant_api.shared.dto import PageOut

VIEW = "ad_tags.view"
MANAGE = "ad_tags.manage"

router = APIRouter(tags=["loaders"])


@router.get("/loaders")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: LoaderService = Depends(loader_service),
) -> PageOut[LoaderOut]:
    """Uma página dos loaders, o mais novo primeiro, com busca no nome."""
    return service.page(actor, page, query)


@router.get("/loaders/options")
def options(
    actor: Actor = Depends(require(VIEW)),
    service: LoaderService = Depends(loader_service),
) -> list[LoaderOptionOut]:
    """Todos os loaders pelo nome, para o seletor da ad tag."""
    return service.options(actor)


@router.post("/loaders", status_code=status.HTTP_201_CREATED)
def create(
    body: LoaderIn,
    actor: Actor = Depends(require(MANAGE)),
    service: LoaderService = Depends(loader_service),
) -> LoaderOut:
    """Cria um loader."""
    return service.create(actor, body)


@router.get("/loaders/{loader_id}")
def show(
    loader_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: LoaderService = Depends(loader_service),
) -> LoaderOut:
    """Um loader com as tags que o usam."""
    return service.get(actor, loader_id)


@router.put("/loaders/{loader_id}")
def update(
    loader_id: uuid.UUID,
    body: LoaderIn,
    actor: Actor = Depends(require(MANAGE)),
    service: LoaderService = Depends(loader_service),
) -> LoaderOut:
    """Troca todos os campos do loader; a mudança chega às tags que o usam sem publicar."""
    return service.update(actor, loader_id, body)


@router.delete("/loaders/{loader_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    loader_id: uuid.UUID,
    actor: Actor = Depends(require(MANAGE)),
    service: LoaderService = Depends(loader_service),
) -> None:
    """Apaga um loader que nenhuma ad tag usa."""
    service.delete(actor, loader_id)
