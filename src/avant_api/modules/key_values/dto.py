"""Entrada da rota dos key-values da g-tag."""

from pydantic import BaseModel, Field


class KeyValueIn(BaseModel):
    name: str = Field(max_length=64)
    value: str = Field(max_length=256)
    network: str = Field(max_length=64)
