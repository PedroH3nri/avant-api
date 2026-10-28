"""Login, sessão, Empresa ativa e aceite de convite: /api/v1/auth."""

import uuid

from avant_core.identity.services import Authenticated
from avant_core.shared.errors import NotAuthenticated
from fastapi import APIRouter, Depends, Request, Response, status

from avant_api.app.cookies import SessionCookies
from avant_api.app.security import get_auth, get_cookies, get_session_auth, optional_auth
from avant_api.modules.auth.dependencies import auth_service
from avant_api.modules.auth.dto import (
    AcceptInvitationIn,
    ActiveCompanyIn,
    InvitationPreviewOut,
    LoginIn,
    LoginOut,
    MeOut,
)
from avant_api.modules.auth.service import AuthService
from avant_api.shared.http import client_info, image_response

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(
    body: LoginIn,
    request: Request,
    response: Response,
    service: AuthService = Depends(auth_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> LoginOut:
    """Entra com senha; com 2FA, responde mfa_required e segue em POST /auth/mfa/verify.

    Limite: 5 senhas erradas por e-mail e 20 por IP em 15 minutos; depois, 429.
    """
    user_agent, ip = client_info(request)
    result = service.login(body, user_agent, ip)
    cookies.open(response, result)
    if result.mfa_required:
        return LoginOut(mfa_required=True, me=None)
    return LoginOut(mfa_required=False, me=MeOut.of(service.authenticate(result.token)))


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def do_logout(
    response: Response,
    auth: Authenticated = Depends(get_session_auth),
    service: AuthService = Depends(auth_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> None:
    """Encerra a sessão atual e apaga os cookies."""
    service.logout(auth.session.id)
    cookies.close(response)


@router.get("/me")
def me(auth: Authenticated = Depends(get_session_auth)) -> MeOut:
    """Devolve a pessoa, as Empresas dela e as permissões na Empresa ativa."""
    return MeOut.of(auth)


@router.get("/me/companies/{company_id}/image", response_class=Response)
def company_image(
    company_id: uuid.UUID,
    request: Request,
    auth: Authenticated = Depends(get_session_auth),
    service: AuthService = Depends(auth_service),
) -> Response:
    """Imagem de uma Empresa em que a pessoa é membro ativo, para o seletor de Empresas."""
    return image_response(request, service.company_image(auth, company_id))


@router.post("/me/active-company")
def set_active_company(
    body: ActiveCompanyIn,
    request: Request,
    auth: Authenticated = Depends(get_auth),
    service: AuthService = Depends(auth_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> MeOut:
    """Troca a Empresa ativa da sessão."""
    token = cookies.session_token(request.cookies)
    if not token:
        raise NotAuthenticated()
    return MeOut.of(service.switch_company(auth, body.company_id, token))


@router.get("/invitations/{token}")
def get_invitation(
    token: str, service: AuthService = Depends(auth_service)
) -> InvitationPreviewOut:
    """Mostra o convite antes do aceite."""
    return service.preview_invitation(token)


@router.post("/invitations/{token}/accept")
def accept(
    token: str,
    body: AcceptInvitationIn,
    request: Request,
    response: Response,
    auth: Authenticated | None = Depends(optional_auth),
    service: AuthService = Depends(auth_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> MeOut:
    """Aceita o convite com a conta logada ou criando uma conta nova, que já entra logada."""
    if auth is not None:
        session_token = cookies.session_token(request.cookies)
        if not session_token:
            raise NotAuthenticated()
        return MeOut.of(service.accept_logged_in(token, auth, session_token))
    user_agent, ip = client_info(request)
    result = service.accept_new_account(token, body, user_agent, ip)
    cookies.open(response, result)
    return MeOut.of(service.authenticate(result.token))
