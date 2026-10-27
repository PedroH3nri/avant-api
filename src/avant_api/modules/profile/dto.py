"""DTOs de entrada e saída do perfil da pessoa: aparência do painel e foto."""

from avant_core.identity.model import Accent, Theme
from pydantic import BaseModel


class AppearanceIn(BaseModel):
    theme: Theme | None = None
    accent: Accent | None = None


class AppearanceOut(BaseModel):
    theme: Theme
    accent: Accent
