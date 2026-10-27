"""Service do perfil da pessoa: aparência do painel e foto de perfil."""

import uuid

from avant_core.identity.model import Accent, Theme, UserImage
from avant_core.identity.profile_service import (
    get_user_image,
    remove_user_image,
    set_appearance,
    set_user_image,
)
from avant_core.identity.service import Authenticated
from avant_core.ports import ImageProcessor
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.profile.dto import AppearanceIn, AppearanceOut
from avant_api.shared.dto import UserOut


class ProfileService:
    """Preferências e foto de perfil de quem está na sessão."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, images: ImageProcessor) -> None:
        self._uows = uows
        self._clock = clock
        self._images = images

    def set_appearance(self, auth: Authenticated, body: AppearanceIn) -> AppearanceOut:
        """Troca o tema e a cor do painel da pessoa (a tabela users não tem RLS)."""
        user = set_appearance(
            self._uows.trusted_uow(),
            user_id=auth.user.id,
            theme=body.theme,
            accent=body.accent,
        )
        return AppearanceOut(theme=Theme(user.theme), accent=Accent(user.accent))

    def set_image(self, auth: Authenticated, content: bytes) -> UserOut:
        """Troca a foto de perfil da pessoa."""
        user = set_user_image(
            self._uows.trusted_uow(),
            user_id=auth.user.id,
            content=content,
            images=self._images,
            clock=self._clock,
        )
        return UserOut.of(user)

    def remove_image(self, auth: Authenticated) -> UserOut:
        """Tira a foto de perfil da pessoa."""
        return UserOut.of(remove_user_image(self._uows.trusted_uow(), user_id=auth.user.id))

    def image(self, auth: Authenticated, user_id: uuid.UUID) -> UserImage:
        """A foto da própria pessoa ou de alguém da Empresa ativa dela, com RLS na Empresa."""
        company_id = auth.active.company.id if auth.active else None
        uow = self._uows.uow(company_id) if company_id else self._uows.trusted_uow()
        return get_user_image(uow, viewer_id=auth.user.id, company_id=company_id, user_id=user_id)
