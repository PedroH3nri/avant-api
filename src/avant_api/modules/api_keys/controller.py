"""Chaves de API da Empresa ativa: /api/v1/api-keys.

Criar só pela sessão do painel; o valor da chave volta uma única vez. Listar e revogar
também funcionam com a própria chave (por exemplo, para um sistema revogar a sua).
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import get_actor, require_session
from avant_api.modules.api_keys.dependencies import api_key_service
from avant_api.modules.api_keys.dto import ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut
from avant_api.modules.api_keys.service import ApiKeyService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/api-keys", tags=["api-keys"])


@router.get("")
def index(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(get_actor),
    service: ApiKeyService = Depends(api_key_service),
) -> PageOut[ApiKeyOut]:
    """Com ``api_keys.manage``, as da Empresa toda; sem, só as próprias."""
    return service.page(actor, page)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: ApiKeyIn,
    actor: Actor = Depends(require_session("api_keys.manage")),
    service: ApiKeyService = Depends(api_key_service),
) -> ApiKeyCreatedOut:
    """Cria uma chave de API para quem está agindo; o token aparece só nesta resposta."""
    return service.create(actor, body)


@router.delete("/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
def revoke(
    key_id: uuid.UUID,
    actor: Actor = Depends(get_actor),
    service: ApiKeyService = Depends(api_key_service),
) -> None:
    """A dona da chave ou quem tem ``api_keys.manage``."""
    service.revoke(actor, key_id)
