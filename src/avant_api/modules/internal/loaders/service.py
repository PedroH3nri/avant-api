"""Service dos loaders dos clientes, vistos e editados pela equipe Groone (sem RLS)."""

import uuid

from avant_core.access.models import Actor
from avant_core.loaders.services import (
    client_loader_options,
    create_client_loader,
    delete_client_loader,
    get_client_loader,
    page_client_loaders,
    update_client_loader,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.internal.loaders.dto import (
    ClientLoaderIn,
    LoaderIn,
    LoaderOptionOut,
    LoaderOut,
)
from avant_api.modules.loaders.cache import forget_tags
from avant_api.shared.dto import PageOut, page_out


class ClientLoaderService:
    """Loaders de todas as Empresas cliente; o core confere a Company Groone e a permissão."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, cache: RewardCache) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache

    def page(
        self, actor: Actor, page: int, company_id: uuid.UUID | None, query: str | None
    ) -> PageOut[LoaderOut]:
        """Uma página dos loaders dos clientes, o mais novo primeiro."""
        found = page_client_loaders(
            self._uows.trusted_uow(), actor=actor, page=page, company_id=company_id, query=query
        )
        return page_out(found, LoaderOut.of)

    def options(self, actor: Actor, company_id: uuid.UUID) -> list[LoaderOptionOut]:
        """Os loaders de um cliente pelo nome, para o seletor da ad tag."""
        found = client_loader_options(self._uows.trusted_uow(), actor=actor, company_id=company_id)
        return [LoaderOptionOut.of(loader) for loader in found]

    def get(self, actor: Actor, loader_id: uuid.UUID) -> LoaderOut:
        """Um loader de qualquer cliente."""
        return LoaderOut.of(
            get_client_loader(self._uows.trusted_uow(), actor=actor, loader_id=loader_id)
        )

    def create(self, actor: Actor, body: ClientLoaderIn) -> LoaderOut:
        """Cria um loader para um cliente."""
        created = create_client_loader(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=body.company_id,
            data=body.to_core(),
            clock=self._clock,
        )
        return LoaderOut.of(created)

    def update(self, actor: Actor, loader_id: uuid.UUID, body: LoaderIn) -> LoaderOut:
        """Troca os campos e limpa o cache das tags que usam o loader."""
        changed = update_client_loader(
            self._uows.trusted_uow(),
            actor=actor,
            loader_id=loader_id,
            data=body.to_core(),
            clock=self._clock,
        )
        forget_tags(self._cache, changed)
        return LoaderOut.of(changed)

    def delete(self, actor: Actor, loader_id: uuid.UUID) -> None:
        """Apaga um loader que nenhuma tag usa."""
        delete_client_loader(
            self._uows.trusted_uow(), actor=actor, loader_id=loader_id, clock=self._clock
        )
