"""Chaves de API da Empresa ativa: /api/v1/api-keys.

Criar só pela sessão do painel; o valor da chave volta uma única vez. Listar e revogar
também funcionam com a própria chave (por exemplo, para um sistema revogar a sua).
"""

import uuid

from avant_core.access.api_keys import create_api_key, list_api_keys, revoke_api_key
from avant_core.company.application import Actor
from fastapi import APIRouter, Depends, status

from avant_api.deps import get_actor, get_services, require_session
from avant_api.schemas import ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ItemsOut
from avant_api.services import Services

router = APIRouter(prefix="/api-keys", tags=["api-keys"])


@router.get("")
def index(
    actor: Actor = Depends(get_actor), services: Services = Depends(get_services)
) -> ItemsOut[ApiKeyOut]:
    """Com ``api_keys.manage``, as da Empresa toda; sem, só as próprias."""
    views = list_api_keys(services.uow(actor.company_id), actor=actor)
    return ItemsOut(items=[ApiKeyOut.of(v) for v in views])


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: ApiKeyIn,
    actor: Actor = Depends(require_session("api_keys.manage")),
    services: Services = Depends(get_services),
) -> ApiKeyCreatedOut:
    created = create_api_key(
        services.uow(actor.company_id),
        actor=actor,
        name=body.name,
        permissions=body.permissions,
        expires_in_days=body.expires_in_days,
        clock=services.clock,
    )
    view = next(
        v
        for v in list_api_keys(services.uow(actor.company_id), actor=actor)
        if v.key.id == created.key.id
    )
    return ApiKeyCreatedOut(**ApiKeyOut.of(view).model_dump(), token=created.token)


@router.delete("/{key_id}", status_code=status.HTTP_204_NO_CONTENT)
def revoke(
    key_id: uuid.UUID,
    actor: Actor = Depends(get_actor),
    services: Services = Depends(get_services),
) -> None:
    """A dona da chave ou quem tem ``api_keys.manage``."""
    revoke_api_key(services.uow(actor.company_id), actor=actor, key_id=key_id, clock=services.clock)
