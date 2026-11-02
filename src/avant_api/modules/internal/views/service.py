"""Service das visões salvas: o catálogo da tela, listar, criar, editar e apagar.

As visões são da Company Groone e usam o Unit of Work dela; a permissão de cada tela é
conferida no avant-core.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.saved_views.enums import ViewScreen
from avant_core.saved_views.services import (
    SavedViewItem,
    create_view,
    delete_view,
    list_views,
    screen_catalog,
    update_view,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.views.dto import SavedViewIn, SavedViewOut, ScreenCatalogOut


class SavedViewService:
    """Visões salvas das tabelas internas."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def catalog(self, actor: Actor, screen: ViewScreen) -> ScreenCatalogOut:
        """O que uma visão da tela pode guardar."""
        spec = screen_catalog(self._uows.uow(actor.company_id), actor=actor, screen=screen)
        return ScreenCatalogOut.of(spec)

    def list(self, actor: Actor, screen: ViewScreen) -> list[SavedViewOut]:
        """As visões da tela que a pessoa vê, na ordem das abas."""
        items = list_views(self._uows.uow(actor.company_id), actor=actor, screen=screen)
        return [SavedViewOut.of(item) for item in items]

    def create(self, actor: Actor, body: SavedViewIn) -> SavedViewOut:
        """Salva uma visão nova, da pessoa."""
        view = create_view(
            self._uows.uow(actor.company_id),
            actor=actor,
            screen=body.screen,
            data=body.input(),
            clock=self._clock,
        )
        return SavedViewOut.of(SavedViewItem(view, True))

    def update(self, actor: Actor, view_id: uuid.UUID, body: SavedViewIn) -> SavedViewOut:
        """Troca o nome, a definição e quem vê; a tela fica a mesma."""
        view = update_view(
            self._uows.uow(actor.company_id),
            actor=actor,
            view_id=view_id,
            data=body.input(),
            clock=self._clock,
        )
        return SavedViewOut.of(SavedViewItem(view, True))

    def delete(self, actor: Actor, view_id: uuid.UUID) -> None:
        """Apaga uma visão da pessoa."""
        delete_view(
            self._uows.uow(actor.company_id), actor=actor, view_id=view_id, clock=self._clock
        )
