"""Service dos loaders do painel do cliente: chama os casos de uso e limpa o cache das tags."""

import uuid

from avant_core.access.models import Actor
from avant_core.loaders.services import (
    create_loader,
    delete_loader,
    get_loader,
    loader_options,
    page_loaders,
    update_loader,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.loaders.cache import forget_tags
from avant_api.modules.loaders.dto import LoaderIn, LoaderOptionOut, LoaderOut
from avant_api.shared.dto import PageOut, page_out


class LoaderService:
    """Loaders da Empresa ativa, com o RLS dela."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, cache: RewardCache) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache

    def page(self, actor: Actor, page: int, query: str | None) -> PageOut[LoaderOut]:
        """Uma página dos loaders, o mais novo primeiro."""
        found = page_loaders(self._uows.uow(actor.company_id), actor=actor, page=page, query=query)
        return page_out(found, LoaderOut.of)

    def options(self, actor: Actor) -> list[LoaderOptionOut]:
        """Todos os loaders pelo nome, para o seletor da ad tag."""
        found = loader_options(self._uows.uow(actor.company_id), actor=actor)
        return [LoaderOptionOut.of(loader) for loader in found]

    def get(self, actor: Actor, loader_id: uuid.UUID) -> LoaderOut:
        """Um loader com as tags que o usam."""
        found = get_loader(self._uows.uow(actor.company_id), actor=actor, loader_id=loader_id)
        return LoaderOut.of(found)

    def create(self, actor: Actor, body: LoaderIn) -> LoaderOut:
        """Cria um loader."""
        created = create_loader(
            self._uows.uow(actor.company_id), actor=actor, data=body.to_core(), clock=self._clock
        )
        return LoaderOut.of(created)

    def update(self, actor: Actor, loader_id: uuid.UUID, body: LoaderIn) -> LoaderOut:
        """Troca os campos e limpa o cache das tags que usam o loader."""
        changed = update_loader(
            self._uows.uow(actor.company_id),
            actor=actor,
            loader_id=loader_id,
            data=body.to_core(),
            clock=self._clock,
        )
        forget_tags(self._cache, changed)
        return LoaderOut.of(changed)

    def delete(self, actor: Actor, loader_id: uuid.UUID) -> None:
        """Apaga um loader que nenhuma tag usa."""
        delete_loader(
            self._uows.uow(actor.company_id), actor=actor, loader_id=loader_id, clock=self._clock
        )
