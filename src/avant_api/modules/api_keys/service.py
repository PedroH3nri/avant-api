"""Service das chaves de API da Empresa ativa."""

import uuid

from avant_core.access.models import Actor
from avant_core.access.services import create_api_key, list_api_keys, page_api_keys, revoke_api_key
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.api_keys.dto import ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut
from avant_api.shared.dto import PageOut, page_out


class ApiKeyService:
    """Criar, listar e revogar chaves de API."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def page(self, actor: Actor, page: int) -> PageOut[ApiKeyOut]:
        """Uma página das chaves: as da Empresa com ``api_keys.manage``; senão, só as próprias."""
        found = page_api_keys(
            self._uows.uow(actor.company_id), actor=actor, clock=self._clock, page=page
        )
        return page_out(found, ApiKeyOut.of)

    def create(self, actor: Actor, body: ApiKeyIn) -> ApiKeyCreatedOut:
        """Cria uma chave para quem está agindo; o token só volta aqui."""
        created = create_api_key(
            self._uows.uow(actor.company_id),
            actor=actor,
            name=body.name,
            permissions=body.permissions,
            expires_in_days=body.expires_in_days,
            clock=self._clock,
        )
        view = next(
            view
            for view in list_api_keys(self._uows.uow(actor.company_id), actor=actor)
            if view.key.id == created.key.id
        )
        return ApiKeyCreatedOut(**ApiKeyOut.of(view).model_dump(), token=created.token)

    def revoke(self, actor: Actor, key_id: uuid.UUID) -> None:
        """Revoga a chave: a dona ou quem tem ``api_keys.manage``."""
        revoke_api_key(
            self._uows.uow(actor.company_id), actor=actor, key_id=key_id, clock=self._clock
        )
