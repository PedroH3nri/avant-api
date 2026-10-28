"""Login com Google e ligação da conta Google à pessoa, em /api/v1/auth/google."""

import hmac
import secrets
from typing import Literal

from avant_core.identity.services import Authenticated
from avant_core.shared.errors import DomainError
from fastapi import APIRouter, Depends, Query, Request, status
from fastapi.responses import RedirectResponse

from avant_api.app.cookies import SessionCookies
from avant_api.app.errors import GoogleFailed
from avant_api.app.google import new_verifier
from avant_api.app.security import get_auth, get_cookies, optional_auth
from avant_api.modules.google.dependencies import google_redirects, google_service
from avant_api.modules.google.dto import GoogleStatusOut
from avant_api.modules.google.redirects import (
    GOOGLE_COOKIE,
    WEB_ACCOUNT,
    WEB_LOGIN,
    WEB_MFA,
    GoogleRedirects,
)
from avant_api.modules.google.service import GoogleService
from avant_api.shared.http import client_info

router = APIRouter(prefix="/auth", tags=["account"])


@router.get("/google")
def google_status(
    auth: Authenticated = Depends(get_auth),
    service: GoogleService = Depends(google_service),
) -> GoogleStatusOut:
    """Diz se o login com Google está disponível e se a pessoa já o ligou."""
    return GoogleStatusOut(available=service.available, linked=service.is_linked(auth.user.id))


@router.delete("/google", status_code=status.HTTP_204_NO_CONTENT)
def google_unlink(
    auth: Authenticated = Depends(get_auth),
    service: GoogleService = Depends(google_service),
) -> None:
    """Desliga a conta Google da pessoa."""
    service.unlink(auth.user.id)


@router.get("/google/start")
def google_start(
    mode: Literal["login", "link"] = "login",
    auth: Authenticated | None = Depends(optional_auth),
    service: GoogleService = Depends(google_service),
    redirects: GoogleRedirects = Depends(google_redirects),
) -> RedirectResponse:
    """Manda o navegador para o Google. Para ligar a conta (mode=link), precisa de sessão."""
    service.ensure_available()
    if mode == "link" and (auth is None or auth.mfa_setup_required):
        return redirects.back(WEB_LOGIN, error="not_authenticated")
    state, verifier, nonce = secrets.token_urlsafe(24), new_verifier(), secrets.token_urlsafe(24)
    url = service.authorize_url(state=state, verifier=verifier, nonce=nonce)
    return redirects.to_google(url, f"{mode}.{state}.{verifier}.{nonce}")


@router.get("/google/callback")
def google_callback(
    request: Request,
    code: str | None = Query(default=None, max_length=2048),
    state: str | None = Query(default=None, max_length=200),
    service: GoogleService = Depends(google_service),
    redirects: GoogleRedirects = Depends(google_redirects),
    cookies: SessionCookies = Depends(get_cookies),
) -> RedirectResponse:
    """Volta do Google. Sempre termina num redirecionamento para o painel, com ?erro= quando
    algo deu errado; o painel traduz o código."""
    parts = request.cookies.get(GOOGLE_COOKIE, "").split(".")
    mode = parts[0] if len(parts) == 4 else "login"
    screen = WEB_ACCOUNT if mode == "link" else WEB_LOGIN
    try:
        service.ensure_available()
        if len(parts) != 4 or not state or not code or not hmac.compare_digest(parts[1], state):
            raise GoogleFailed("state ausente ou diferente")
        if mode == "link":
            service.link(
                cookies.session_token(request.cookies),
                code=code,
                verifier=parts[2],
                nonce=parts[3],
            )
            return redirects.back(WEB_ACCOUNT, google="ligado")
        user_agent, ip = client_info(request)
        result = service.login(
            code=code, verifier=parts[2], nonce=parts[3], user_agent=user_agent, ip=ip
        )
    except DomainError as error:
        return redirects.back(screen, error=error.code)
    redirect = redirects.back(WEB_MFA if result.mfa_required else "/")
    cookies.open(redirect, result)
    return redirect
