"""Perfil da pessoa: aparência do painel em /auth/appearance, foto em /auth/me/image e
/users/{id}/image."""

import uuid

from avant_core.identity.service import Authenticated
from fastapi import APIRouter, Depends, Request, Response

from avant_api.app.security import get_auth
from avant_api.modules.profile.dependencies import profile_service
from avant_api.modules.profile.dto import AppearanceIn, AppearanceOut
from avant_api.modules.profile.service import ProfileService
from avant_api.shared.dto import UserOut
from avant_api.shared.http import image_response, image_upload

router = APIRouter(tags=["profile"])


@router.patch("/auth/appearance")
def edit_appearance(
    body: AppearanceIn,
    auth: Authenticated = Depends(get_auth),
    service: ProfileService = Depends(profile_service),
) -> AppearanceOut:
    """Troca o tema e a cor de destaque do painel; vale em todas as Empresas da pessoa."""
    return service.set_appearance(auth, body)


@router.put("/auth/me/image")
def edit_image(
    content: bytes = Depends(image_upload),
    auth: Authenticated = Depends(get_auth),
    service: ProfileService = Depends(profile_service),
) -> UserOut:
    """Troca a foto de perfil: o corpo é o arquivo PNG, JPEG ou WebP de até 2 MB."""
    return service.set_image(auth, content)


@router.delete("/auth/me/image")
def remove_image(
    auth: Authenticated = Depends(get_auth),
    service: ProfileService = Depends(profile_service),
) -> UserOut:
    """Tira a foto de perfil; volta a inicial do nome."""
    return service.remove_image(auth)


@router.get("/users/{user_id}/image", response_class=Response)
def image(
    user_id: uuid.UUID,
    request: Request,
    auth: Authenticated = Depends(get_auth),
    service: ProfileService = Depends(profile_service),
) -> Response:
    """Foto de perfil da própria pessoa ou de alguém da Empresa ativa, com cache pela URL."""
    return image_response(request, service.image(auth, user_id))
