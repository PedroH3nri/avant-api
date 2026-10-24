"""Conta da pessoa: senha, sessões ativas e login com Google, em /api/v1/auth.

Tudo aqui é da pessoa e não de uma Empresa, por isso usa trusted_uow, como o login.
"""

import hmac
import secrets
import uuid
from typing import Literal
from urllib.parse import urlencode

from avant_core.identity.account import (
    change_password,
    has_google,
    link_google,
    list_sessions,
    login_with_google,
    request_password_reset,
    reset_password,
    revoke_other_sessions,
    revoke_session,
    unlink_google,
)
from avant_core.identity.application import Authenticated, authenticate
from avant_core.shared.errors import DomainError, InvalidToken, NotAuthenticated
from fastapi import APIRouter, Depends, Query, Request, Response, status
from fastapi.responses import RedirectResponse

from avant_api.deps import get_auth, get_services, get_session_auth, optional_auth
from avant_api.errors import GoogleFailed, GoogleUnavailable
from avant_api.google import GoogleAuth, new_verifier
from avant_api.limits import PASSWORD_IP
from avant_api.routes.auth import _client, _end, _set_cookies
from avant_api.schemas import (
    ChangePasswordIn,
    ForgotPasswordIn,
    GoogleStatusOut,
    ResetPasswordIn,
    RevokedOut,
    SessionOut,
)
from avant_api.services import Services

router = APIRouter(prefix="/auth", tags=["account"])

# Telas do painel para onde o callback do Google volta.
WEB_LOGIN = "/entrar"
WEB_MFA = "/entrar/2fa"
WEB_ACCOUNT = "/configuracoes/conta"

GOOGLE_COOKIE = "avant_google"
GOOGLE_COOKIE_PATH = "/api/v1/auth/google"
GOOGLE_COOKIE_TTL = 600


# --- Senha -----------------------------------------------------------------------------


@router.post("/password/forgot", status_code=status.HTTP_202_ACCEPTED)
def forgot_password(
    body: ForgotPasswordIn, request: Request, services: Services = Depends(get_services)
) -> None:
    """Responde 202 exista ou não a conta, para não revelar quem tem cadastro."""
    _, ip = _client(request)
    services.limiter.check((PASSWORD_IP, ip))
    services.limiter.fail((PASSWORD_IP, ip))  # todo pedido conta
    request_password_reset(
        services.trusted_uow(), email=body.email, clock=services.clock, mailer=services.mailer
    )


@router.post("/password/reset", status_code=status.HTTP_204_NO_CONTENT)
def do_reset_password(
    body: ResetPasswordIn,
    request: Request,
    response: Response,
    services: Services = Depends(get_services),
) -> None:
    """Encerra todas as sessões, inclusive a deste navegador: a pessoa entra de novo."""
    _, ip = _client(request)
    services.limiter.check((PASSWORD_IP, ip))
    try:
        reset_password(
            services.trusted_uow(),
            token=body.token,
            password=body.password,
            mfa_code=body.mfa_code,
            hasher=services.hasher,
            box=services.box,
            clock=services.clock,
            mailer=services.mailer,
        )
    except InvalidToken:
        services.limiter.fail((PASSWORD_IP, ip))
        raise
    _end(response, services)


@router.post("/password/change", status_code=status.HTTP_204_NO_CONTENT)
def do_change_password(
    body: ChangePasswordIn,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> None:
    """Mantém a sessão atual e encerra as outras."""
    change_password(
        services.trusted_uow(),
        user_id=auth.user.id,
        session_id=auth.session.id,
        current=body.current_password,
        new=body.new_password,
        hasher=services.hasher,
        clock=services.clock,
        mailer=services.mailer,
    )


# --- Sessões ---------------------------------------------------------------------------


@router.get("/sessions")
def get_sessions(
    auth: Authenticated = Depends(get_session_auth), services: Services = Depends(get_services)
) -> list[SessionOut]:
    rows = list_sessions(services.trusted_uow(), user_id=auth.user.id, clock=services.clock)
    rows.sort(key=lambda s: s.last_seen_at, reverse=True)
    return [
        SessionOut(
            id=s.id,
            created_at=s.created_at,
            last_seen_at=s.last_seen_at,
            expires_at=s.expires_at,
            user_agent=s.user_agent,
            ip=str(s.ip) if s.ip is not None else None,  # inet volta como IPv4Address
            current=s.id == auth.session.id,
        )
        for s in rows
    ]


@router.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(
    session_id: uuid.UUID,
    response: Response,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> None:
    revoke_session(
        services.trusted_uow(), user_id=auth.user.id, session_id=session_id, clock=services.clock
    )
    if session_id == auth.session.id:
        _end(response, services)


@router.post("/sessions/revoke-others")
def revoke_others(
    auth: Authenticated = Depends(get_session_auth), services: Services = Depends(get_services)
) -> RevokedOut:
    count = revoke_other_sessions(
        services.trusted_uow(),
        user_id=auth.user.id,
        keep_session_id=auth.session.id,
        clock=services.clock,
    )
    return RevokedOut(revoked=count)


# --- Google ----------------------------------------------------------------------------


def _google(services: Services) -> GoogleAuth:
    if services.google is None:
        raise GoogleUnavailable("login com Google não configurado")
    return services.google


@router.get("/google")
def google_status(
    auth: Authenticated = Depends(get_auth), services: Services = Depends(get_services)
) -> GoogleStatusOut:
    linked = has_google(services.trusted_uow(), user_id=auth.user.id)
    return GoogleStatusOut(available=services.google is not None, linked=linked)


@router.delete("/google", status_code=status.HTTP_204_NO_CONTENT)
def google_unlink(
    auth: Authenticated = Depends(get_auth), services: Services = Depends(get_services)
) -> None:
    unlink_google(services.trusted_uow(), user_id=auth.user.id)


@router.get("/google/start")
def google_start(
    mode: Literal["login", "link"] = "login",
    auth: Authenticated | None = Depends(optional_auth),
    services: Services = Depends(get_services),
) -> RedirectResponse:
    """Manda o navegador para o Google. Para ligar a conta (mode=link), precisa de sessão."""
    google = _google(services)
    if mode == "link" and (auth is None or auth.mfa_setup_required):
        return _back(services, WEB_LOGIN, error="not_authenticated")
    state, verifier, nonce = secrets.token_urlsafe(24), new_verifier(), secrets.token_urlsafe(24)
    redirect = RedirectResponse(
        google.authorize_url(state=state, verifier=verifier, nonce=nonce), status_code=302
    )
    redirect.set_cookie(
        GOOGLE_COOKIE,
        f"{mode}.{state}.{verifier}.{nonce}",
        max_age=GOOGLE_COOKIE_TTL,
        path=GOOGLE_COOKIE_PATH,
        httponly=True,
        secure=services.settings.cookie_secure,
        samesite="lax",
    )
    return redirect


@router.get("/google/callback")
def google_callback(
    request: Request,
    code: str | None = Query(default=None, max_length=2048),
    state: str | None = Query(default=None, max_length=200),
    services: Services = Depends(get_services),
) -> RedirectResponse:
    """Volta do Google. Sempre termina num redirecionamento para o painel, com ?erro= quando
    algo deu errado; o painel traduz o código."""
    parts = request.cookies.get(GOOGLE_COOKIE, "").split(".")
    mode = parts[0] if len(parts) == 4 else "login"
    screen = WEB_ACCOUNT if mode == "link" else WEB_LOGIN
    try:
        google = _google(services)
        if len(parts) != 4 or not state or not code or not hmac.compare_digest(parts[1], state):
            raise GoogleFailed("state ausente ou diferente")
        identity = google.exchange(code=code, verifier=parts[2], nonce=parts[3])
        if mode == "link":
            auth = _session(request, services)
            link_google(
                services.trusted_uow(),
                user_id=auth.user.id,
                identity=identity,
                clock=services.clock,
                mailer=services.mailer,
            )
            return _back(services, WEB_ACCOUNT, google="ligado")
        user_agent, ip = _client(request)
        result = login_with_google(
            services.trusted_uow(),
            identity=identity,
            clock=services.clock,
            user_agent=user_agent,
            ip=ip,
        )
    except DomainError as exc:
        return _back(services, screen, error=exc.code)
    redirect = _back(services, WEB_MFA if result.mfa_required else "/")
    _set_cookies(redirect, services, result)
    return redirect


def _session(request: Request, services: Services) -> Authenticated:
    token = request.cookies.get(services.settings.session_cookie)
    if not token:
        raise NotAuthenticated()
    auth = authenticate(services.trusted_uow(), token=token, clock=services.clock)
    if auth.mfa_setup_required:
        raise NotAuthenticated()
    return auth


def _back(
    services: Services, path: str, *, error: str | None = None, google: str | None = None
) -> RedirectResponse:
    query = {k: v for k, v in (("erro", error), ("google", google)) if v}
    url = services.settings.app_base_url.rstrip("/") + path
    redirect = RedirectResponse(url + (f"?{urlencode(query)}" if query else ""), status_code=302)
    redirect.delete_cookie(GOOGLE_COOKIE, path=GOOGLE_COOKIE_PATH)
    return redirect
