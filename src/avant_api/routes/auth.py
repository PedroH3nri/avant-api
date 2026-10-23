"""Login, sessão, Empresa ativa e aceite de convite: /api/v1/auth."""

import ipaddress
import secrets

from avant_core.company.application import (
    ExistingAccount,
    NewAccount,
    NewCompany,
    accept_invitation,
    preview_invitation,
)
from avant_core.identity.application import (
    Authenticated,
    LoginResult,
    authenticate,
    login_with_password,
    logout,
    start_session,
    switch_active_company,
)
from avant_core.shared.errors import WrongInvitationKind
from fastapi import APIRouter, Depends, Request, Response, status

from avant_api.deps import get_auth, get_services, optional_auth
from avant_api.schemas import (
    AcceptInvitationIn,
    ActiveCompanyIn,
    InvitationPreviewOut,
    LoginIn,
    MeOut,
)
from avant_api.services import Services

router = APIRouter(prefix="/auth", tags=["auth"])


def _client(request: Request) -> tuple[str | None, str | None]:
    """User-Agent e IP. Atrás do nginx, o uvicorn roda com --proxy-headers e o client já é
    o IP real. Socket unix ou cliente de teste não têm IP válido: fica vazio."""
    host = request.client.host if request.client else None
    try:
        ip = str(ipaddress.ip_address(host)) if host else None
    except ValueError:
        ip = None
    return request.headers.get("User-Agent"), ip


def _start(response: Response, services: Services, result: LoginResult) -> Authenticated:
    s = services.settings
    max_age = int((result.session.expires_at - services.clock.now()).total_seconds())
    common = {"max_age": max_age, "secure": s.cookie_secure, "samesite": "lax", "path": "/"}
    response.set_cookie(s.session_cookie, result.token, httponly=True, **common)  # type: ignore[arg-type]
    response.set_cookie(s.csrf_cookie, secrets.token_urlsafe(32), httponly=False, **common)  # type: ignore[arg-type]
    return authenticate(services.trusted_uow(), token=result.token, clock=services.clock)


def _end(response: Response, services: Services) -> None:
    response.delete_cookie(services.settings.session_cookie, path="/")
    response.delete_cookie(services.settings.csrf_cookie, path="/")


@router.post("/login")
def login(
    body: LoginIn,
    request: Request,
    response: Response,
    services: Services = Depends(get_services),
) -> MeOut:
    user_agent, ip = _client(request)
    result = login_with_password(
        services.trusted_uow(),
        email=body.email,
        password=body.password,
        hasher=services.hasher,
        clock=services.clock,
        user_agent=user_agent,
        ip=ip,
    )
    return MeOut.of(_start(response, services, result))


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def do_logout(
    response: Response,
    auth: Authenticated = Depends(get_auth),
    services: Services = Depends(get_services),
) -> None:
    logout(services.trusted_uow(), session_id=auth.session.id, clock=services.clock)
    _end(response, services)


@router.get("/me")
def me(auth: Authenticated = Depends(get_auth)) -> MeOut:
    return MeOut.of(auth)


@router.post("/me/active-company")
def set_active_company(
    body: ActiveCompanyIn,
    request: Request,
    auth: Authenticated = Depends(get_auth),
    services: Services = Depends(get_services),
) -> MeOut:
    switch_active_company(
        services.trusted_uow(), session_id=auth.session.id, company_id=body.company_id
    )
    token = request.cookies[services.settings.session_cookie]
    return MeOut.of(authenticate(services.trusted_uow(), token=token, clock=services.clock))


@router.get("/invitations/{token}")
def get_invitation(token: str, services: Services = Depends(get_services)) -> InvitationPreviewOut:
    p = preview_invitation(services.trusted_uow(), token=token, clock=services.clock)
    return InvitationPreviewOut(**p.__dict__)


@router.post("/invitations/{token}/accept")
def accept(
    token: str,
    body: AcceptInvitationIn,
    request: Request,
    response: Response,
    auth: Authenticated | None = Depends(optional_auth),
    services: Services = Depends(get_services),
) -> MeOut:
    if auth is not None:
        account: NewAccount | ExistingAccount = ExistingAccount(auth.user.id)
    elif body.name and body.password:
        account = NewAccount(name=body.name, password=body.password, locale=body.locale)
    else:
        raise WrongInvitationKind("sem sessão, informe name e password para criar a conta")
    company = NewCompany(body.company.name, body.company.accent_color) if body.company else None
    membership = accept_invitation(
        services.trusted_uow(),
        token=token,
        account=account,
        company=company,
        clock=services.clock,
        hasher=services.hasher,
    )
    if auth is not None:
        switch_active_company(
            services.trusted_uow(), session_id=auth.session.id, company_id=membership.company_id
        )
        cookie = request.cookies[services.settings.session_cookie]
        return MeOut.of(authenticate(services.trusted_uow(), token=cookie, clock=services.clock))
    # Conta nova: já entra logada, na Empresa do convite.
    user_agent, ip = _client(request)
    result = start_session(
        services.trusted_uow(),
        user_id=membership.user_id,
        clock=services.clock,
        user_agent=user_agent,
        ip=ip,
    )
    return MeOut.of(_start(response, services, result))
