"""Papéis e catálogo de permissões: /api/v1/roles e /api/v1/permissions."""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require
from avant_api.modules.roles.dependencies import role_service
from avant_api.modules.roles.dto import PermissionOut, RoleIn, RoleOptionOut, RoleOut, RolePatchIn
from avant_api.modules.roles.service import RoleService
from avant_api.shared.dto import ItemsOut

router = APIRouter(tags=["roles"])


@router.get("/permissions")
def permissions(
    actor: Actor = Depends(require("roles.view")), service: RoleService = Depends(role_service)
) -> ItemsOut[PermissionOut]:
    """Lista as permissões que um papel de cliente pode ter."""
    return ItemsOut(items=service.permissions(actor))


@router.get("/roles/options")
def options(
    actor: Actor = Depends(require("roles.view")),
    service: RoleService = Depends(role_service),
) -> ItemsOut[RoleOptionOut]:
    """Os papéis só com id e nome, inteiros, para os seletores (sem paginar)."""
    return ItemsOut(items=service.options(actor))


@router.get("/roles")
def index(
    actor: Actor = Depends(require("roles.view")),
    service: RoleService = Depends(role_service),
) -> ItemsOut[RoleOut]:
    """Lista os papéis da Empresa ativa."""
    return ItemsOut(items=service.list_all(actor))


@router.post("/roles", status_code=status.HTTP_201_CREATED)
def create(
    body: RoleIn,
    actor: Actor = Depends(require("roles.manage")),
    service: RoleService = Depends(role_service),
) -> RoleOut:
    """Cria um papel personalizado."""
    return service.create(actor, body)


@router.patch("/roles/{role_id}")
def edit(
    role_id: uuid.UUID,
    body: RolePatchIn,
    actor: Actor = Depends(require("roles.manage")),
    service: RoleService = Depends(role_service),
) -> RoleOut:
    """Muda um papel personalizado."""
    return service.update(actor, role_id, body)


@router.delete("/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    role_id: uuid.UUID,
    actor: Actor = Depends(require("roles.manage")),
    service: RoleService = Depends(role_service),
) -> None:
    """Apaga um papel personalizado sem uso."""
    service.delete(actor, role_id)
