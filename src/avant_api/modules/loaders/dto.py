"""DTOs dos loaders, usados pelo painel do cliente e pelo interno. Datas em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.loaders.enums import LoaderAdblock, LoaderStyle, LoaderTemplate
from avant_core.loaders.models import Loader, LoaderDetails, LoaderInput, LoaderTagUse
from pydantic import BaseModel, Field


class LoaderIn(BaseModel):
    name: str = Field(max_length=200)
    template: LoaderTemplate = LoaderTemplate.GROONE
    blur: int = Field(default=2, ge=0, le=3)
    background: str = Field(default="#ffffff", max_length=7)
    accent: str = Field(default="#171717", max_length=7)
    style: LoaderStyle = LoaderStyle.SPINNER
    text: str | None = Field(default=None, max_length=200)
    max_seconds: int = 3
    adblock: LoaderAdblock = LoaderAdblock.WARN

    def to_core(self) -> LoaderInput:
        """O formulário no formato do caso de uso."""
        return LoaderInput(**self.model_dump())


class ClientLoaderIn(LoaderIn):
    # A Empresa cliente dona do loader (só no painel interno).
    company_id: uuid.UUID

    def to_core(self) -> LoaderInput:
        """O formulário sem a Empresa."""
        return LoaderInput(**self.model_dump(exclude={"company_id"}))


class LoaderTagOut(BaseModel):
    id: uuid.UUID
    name: str
    domain: str
    key: str

    @classmethod
    def of(cls, use: LoaderTagUse) -> "LoaderTagOut":
        """Monta a tag que usa o loader."""
        return cls(id=use.ad_tag_id, name=use.name, domain=use.domain, key=use.key)


class LoaderClientOut(BaseModel):
    id: uuid.UUID
    name: str


class LoaderOptionOut(BaseModel):
    id: uuid.UUID
    name: str
    template: LoaderTemplate

    @classmethod
    def of(cls, loader: Loader) -> "LoaderOptionOut":
        """Monta a opção do seletor."""
        return cls(id=loader.id, name=loader.name, template=loader.template)


class LoaderOut(BaseModel):
    id: uuid.UUID
    # Só no painel interno.
    client: LoaderClientOut | None = None
    name: str
    template: LoaderTemplate
    blur: int
    background: str
    accent: str
    style: LoaderStyle
    text: str | None
    max_seconds: int
    adblock: LoaderAdblock
    tags: list[LoaderTagOut]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, details: LoaderDetails) -> "LoaderOut":
        """Monta o loader com as tags que o usam e, no painel interno, o cliente."""
        loader = details.loader
        client = (
            LoaderClientOut(id=loader.company_id, name=details.company_name)
            if details.company_name is not None
            else None
        )
        return cls(
            id=loader.id,
            client=client,
            name=loader.name,
            template=loader.template,
            blur=loader.blur,
            background=loader.background,
            accent=loader.accent,
            style=loader.style,
            text=loader.text,
            max_seconds=loader.max_seconds,
            adblock=loader.adblock,
            tags=[LoaderTagOut.of(use) for use in details.tags],
            created_at=loader.created_at,
            updated_at=loader.updated_at,
        )
