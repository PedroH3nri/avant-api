"""Formatos de entrada e saída das visões salvas e do catálogo de cada tela."""

import uuid
from datetime import datetime
from typing import Any

from avant_core.access.enums.visibility import Visibility
from avant_core.saved_views.enums import ViewScreen
from avant_core.saved_views.models import ScreenSpec
from avant_core.saved_views.services import SavedViewInput, SavedViewItem
from pydantic import BaseModel, Field


class SavedViewIn(BaseModel):
    screen: ViewScreen
    name: str = Field(min_length=1, max_length=80)
    # Colunas, filtros e ordem, conferidos no avant-core contra o catálogo da tela.
    definition: dict[str, Any]
    visibility: Visibility = Visibility.PRIVATE
    role_ids: list[uuid.UUID] = Field(default_factory=list, max_length=50)

    def input(self) -> SavedViewInput:
        """O formulário no formato do caso de uso."""
        return SavedViewInput(
            name=self.name,
            definition=self.definition,
            visibility=self.visibility,
            role_ids=tuple(self.role_ids),
        )


class SavedViewOut(BaseModel):
    id: uuid.UUID
    screen: ViewScreen
    name: str
    definition: dict[str, Any]
    visibility: Visibility
    role_ids: list[uuid.UUID]
    owner_user_id: uuid.UUID
    # Só o dono edita e apaga.
    editable: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, item: SavedViewItem) -> "SavedViewOut":
        """Monta a visão com a permissão de editar."""
        view = item.view
        return cls(
            id=view.id,
            screen=view.screen,
            name=view.name,
            definition=view.definition,
            visibility=view.visibility,
            role_ids=view.role_ids,
            owner_user_id=view.owner_user_id,
            editable=item.can_edit,
            created_at=view.created_at,
            updated_at=view.updated_at,
        )


class ViewFilterOut(BaseModel):
    key: str
    # text, id, id_list ou choice.
    kind: str
    choices: list[str]


class ViewSortOut(BaseModel):
    key: str
    direction: str


class ScreenCatalogOut(BaseModel):
    screen: ViewScreen
    # Na ordem padrão da tela.
    columns: list[str]
    filters: list[ViewFilterOut]
    # A primeira é a padrão.
    sorts: list[ViewSortOut]

    @classmethod
    def of(cls, spec: ScreenSpec) -> "ScreenCatalogOut":
        """Monta o catálogo da tela."""
        return cls(
            screen=spec.screen,
            columns=list(spec.columns),
            filters=[
                ViewFilterOut(key=key, kind=item.kind.value, choices=list(item.choices))
                for key, item in spec.filters.items()
            ],
            sorts=[
                ViewSortOut(key=sort.key, direction=sort.direction.value) for sort in spec.sorts
            ],
        )
