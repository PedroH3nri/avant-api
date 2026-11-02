"""Visões salvas das tabelas do painel interno: /api/v1/internal/views.

Pede a equipe Groone com 2FA; o avant-core confere a permissão de ver a tela (clientes,
contratos, resultado, comissões ou invoices). A pessoa vê as visões dela, as da Empresa e as
dos papéis dela; só o dono edita e apaga.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.saved_views.enums import ViewScreen
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require_staff_member
from avant_api.modules.internal.views.dependencies import saved_view_service
from avant_api.modules.internal.views.dto import SavedViewIn, SavedViewOut, ScreenCatalogOut
from avant_api.modules.internal.views.service import SavedViewService
from avant_api.shared.dto import ItemsOut

router = APIRouter(prefix="/internal/views", tags=["internal"])


@router.get("/catalog/{screen}")
def catalog(
    screen: ViewScreen,
    actor: Actor = Depends(require_staff_member),
    service: SavedViewService = Depends(saved_view_service),
) -> ScreenCatalogOut:
    """As colunas, os filtros e as ordens que uma visão da tela pode guardar."""
    return service.catalog(actor, screen)


@router.get("")
def index(
    screen: ViewScreen,
    actor: Actor = Depends(require_staff_member),
    service: SavedViewService = Depends(saved_view_service),
) -> ItemsOut[SavedViewOut]:
    """As visões da tela que a pessoa vê, na ordem das abas."""
    return ItemsOut(items=service.list(actor, screen))


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: SavedViewIn,
    actor: Actor = Depends(require_staff_member),
    service: SavedViewService = Depends(saved_view_service),
) -> SavedViewOut:
    """Salva uma visão nova da tela, da pessoa."""
    return service.create(actor, body)


@router.put("/{view_id}")
def update(
    view_id: uuid.UUID,
    body: SavedViewIn,
    actor: Actor = Depends(require_staff_member),
    service: SavedViewService = Depends(saved_view_service),
) -> SavedViewOut:
    """Troca o nome, a definição e quem vê; a tela não muda."""
    return service.update(actor, view_id, body)


@router.delete("/{view_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    view_id: uuid.UUID,
    actor: Actor = Depends(require_staff_member),
    service: SavedViewService = Depends(saved_view_service),
) -> None:
    """Apaga uma visão da pessoa."""
    service.delete(actor, view_id)
