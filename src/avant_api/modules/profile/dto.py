"""DTOs de entrada e saída do perfil da pessoa: aparência do painel, idioma e foto."""

from avant_core.identity.enums import Accent, Locale, Theme
from pydantic import BaseModel


class AppearanceIn(BaseModel):
    theme: Theme | None = None
    accent: Accent | None = None
    locale: Locale | None = None


class AppearanceOut(BaseModel):
    theme: Theme
    accent: Accent
    locale: Locale
