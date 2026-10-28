"""Service dos papéis e do catálogo de permissões da Empresa ativa."""

import uuid

from avant_core.access.models import Actor
from avant_core.company.services import (
    client_permissions,
    create_role,
    delete_role,
    list_roles,
    update_role,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.roles.dto import PermissionOut, RoleIn, RoleOut, RolePatchIn


class RoleService:
    """Papéis predefinidos e personalizados da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def permissions(self, actor: Actor) -> list[PermissionOut]:
        """As permissões que um papel de cliente pode ter."""
        return [PermissionOut.of(permission) for permission in client_permissions(actor=actor)]

    def list_all(self, actor: Actor) -> list[RoleOut]:
        """Os papéis da Empresa ativa."""
        return [
            RoleOut.of(role) for role in list_roles(self._uows.uow(actor.company_id), actor=actor)
        ]

    def create(self, actor: Actor, body: RoleIn) -> RoleOut:
        """Cria um papel personalizado."""
        view = create_role(
            self._uows.uow(actor.company_id),
            actor=actor,
            name=body.name,
            permissions=set(body.permissions),
            site_scope=body.site_scope,
            clock=self._clock,
        )
        return RoleOut.of(view)

    def update(self, actor: Actor, role_id: uuid.UUID, body: RolePatchIn) -> RoleOut:
        """Muda um papel personalizado."""
        view = update_role(
            self._uows.uow(actor.company_id),
            actor=actor,
            role_id=role_id,
            clock=self._clock,
            name=body.name,
            permissions=set(body.permissions) if body.permissions is not None else None,
            site_scope=body.site_scope,
        )
        return RoleOut.of(view)

    def delete(self, actor: Actor, role_id: uuid.UUID) -> None:
        """Apaga um papel personalizado sem uso."""
        delete_role(
            self._uows.uow(actor.company_id), actor=actor, role_id=role_id, clock=self._clock
        )
