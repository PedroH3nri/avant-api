"""Dependências das rotas: serviços, sessão, CSRF e permissões."""

import hmac
from collections.abc import Callable

from avant_core.company.application import Actor
from avant_core.identity.application import Authenticated, authenticate
from avant_core.shared.errors import MfaRequired, NotAuthenticated
from fastapi import Depends, Request

from avant_api.errors import CsrfFailed, NoActiveCompany
from avant_api.services import Services

SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
CSRF_HEADER = "X-CSRF-Token"


def get_services(request: Request) -> Services:
    services: Services = request.app.state.services
    return services


def check_csrf(request: Request, services: Services) -> None:
    """Double submit: o cookie avant_csrf (legível pelo Vue) precisa vir também no cabeçalho."""
    if request.method in SAFE_METHODS:
        return
    cookie = request.cookies.get(services.settings.csrf_cookie, "")
    header = request.headers.get(CSRF_HEADER, "")
    if not cookie or not hmac.compare_digest(cookie, header):
        raise CsrfFailed("cabeçalho X-CSRF-Token ausente ou diferente do cookie")


def optional_auth(
    request: Request, services: Services = Depends(get_services)
) -> Authenticated | None:
    token = request.cookies.get(services.settings.session_cookie)
    if not token:
        return None
    try:
        auth = authenticate(services.trusted_uow(), token=token, clock=services.clock)
    except NotAuthenticated:
        return None
    check_csrf(request, services)
    return auth


def get_session_auth(auth: Authenticated | None = Depends(optional_auth)) -> Authenticated:
    """Qualquer sessão válida, mesmo da equipe Groone ainda sem 2FA. Só para /me, logout e
    as rotas de configuração do 2FA."""
    if auth is None:
        raise NotAuthenticated()
    return auth


def get_auth(auth: Authenticated = Depends(get_session_auth)) -> Authenticated:
    if auth.mfa_setup_required:
        raise MfaRequired("configure o 2FA para continuar")
    return auth


def get_actor(auth: Authenticated = Depends(get_auth)) -> Actor:
    if auth.active is None or auth.grants is None:
        raise NoActiveCompany("a pessoa não é membro ativo de nenhuma Empresa")
    return Actor(user_id=auth.user.id, company_id=auth.active.company.id, grants=auth.grants)


def require(permission: str) -> Callable[[Actor], Actor]:
    """Depends(require("team.invite")): a permissão da rota fica declarada nela."""

    def dependency(actor: Actor = Depends(get_actor)) -> Actor:
        actor.grants.require(permission)
        return actor

    return dependency
