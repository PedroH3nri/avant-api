"""Papéis e catálogo de permissões: /api/v1/roles e /api/v1/permissions."""

import uuid

from avant_core.company.application import Actor
from avant_core.company.team import (
    client_permissions,
    create_role,
    delete_role,
    list_roles,
    update_role,
)
from fastapi import APIRouter, Depends, status

from avant_api.deps import get_services, require
from avant_api.schemas import ItemsOut, PermissionOut, RoleIn, RoleOut, RolePatchIn
from avant_api.services import Services

router = APIRouter(tags=["roles"])


@router.get("/permissions")
def permissions(actor: Actor = Depends(require("roles.view"))) -> ItemsOut[PermissionOut]:
    """Lista as permissões que um papel de cliente pode ter."""
    return ItemsOut(
        items=[PermissionOut.of(permission) for permission in client_permissions(actor=actor)]
    )


@router.get("/roles")
def index(
    actor: Actor = Depends(require("roles.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[RoleOut]:
    """Lista os papéis da Empresa ativa."""
    roles = list_roles(services.uow(actor.company_id), actor=actor)
    return ItemsOut(items=[RoleOut.of(role) for role in roles])


@router.post("/roles", status_code=status.HTTP_201_CREATED)
def create(
    body: RoleIn,
    actor: Actor = Depends(require("roles.manage")),
    services: Services = Depends(get_services),
) -> RoleOut:
    """Cria um papel personalizado."""
    view = create_role(
        services.uow(actor.company_id),
        actor=actor,
        name=body.name,
        permissions=set(body.permissions),
        site_scope=body.site_scope,
        clock=services.clock,
    )
    return RoleOut.of(view)


@router.patch("/roles/{role_id}")
def edit(
    role_id: uuid.UUID,
    body: RolePatchIn,
    actor: Actor = Depends(require("roles.manage")),
    services: Services = Depends(get_services),
) -> RoleOut:
    """Muda um papel personalizado."""
    view = update_role(
        services.uow(actor.company_id),
        actor=actor,
        role_id=role_id,
        clock=services.clock,
        name=body.name,
        permissions=set(body.permissions) if body.permissions is not None else None,
        site_scope=body.site_scope,
    )
    return RoleOut.of(view)


@router.delete("/roles/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove(
    role_id: uuid.UUID,
    actor: Actor = Depends(require("roles.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Apaga um papel personalizado sem uso."""
    delete_role(services.uow(actor.company_id), actor=actor, role_id=role_id, clock=services.clock)
