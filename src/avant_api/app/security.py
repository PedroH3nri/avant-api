"""Dependências das rotas: serviços, sessão, chave de API, CSRF e permissões.

As rotas de Empresa aceitam a sessão do painel (cookie + CSRF) ou uma chave de API
(``Authorization: Bearer avk_...``, sem CSRF: não há cookie para roubar). Login, 2FA,
conta, sessões, criar chave, sair da Empresa e o painel interno são só pela sessão.
"""

import hmac
import time
from collections.abc import Callable

from avant_core.access.api_keys import authenticate_api_key
from avant_core.company.application import Actor
from avant_core.identity.application import Authenticated, authenticate
from avant_core.shared.errors import MfaRequired, NotAuthenticated, StaffOnly
from fastapi import Depends, Request

from avant_api.app.container import Services
from avant_api.app.cookies import SessionCookies
from avant_api.app.errors import CsrfFailed, NoActiveCompany, RateLimited
from avant_api.app.limits import API_KEY

SAFE_METHODS = frozenset({"GET", "HEAD", "OPTIONS"})
CSRF_HEADER = "X-CSRF-Token"


def get_services(request: Request) -> Services:
    """Devolve os serviços montados na subida da aplicação."""
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
    """Autentica pelo cookie de sessão, se houver; sem cookie devolve None."""
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
    """Exige sessão válida; equipe Groone sem 2FA só pode configurar o 2FA."""
    if auth.mfa_setup_required:
        raise MfaRequired("configure o 2FA para continuar")
    return auth


def get_session_actor(auth: Authenticated = Depends(get_auth)) -> Actor:
    """Só pela sessão do painel, nunca por chave de API."""
    if auth.active is None or auth.grants is None:
        raise NoActiveCompany("a pessoa não é membro ativo de nenhuma Empresa")
    return Actor(user_id=auth.user.id, company_id=auth.active.company.id, grants=auth.grants)


def bearer_token(request: Request) -> str | None:
    """Lê o token do cabeçalho ``Authorization: Bearer``, se houver."""
    scheme, _, token = request.headers.get("Authorization", "").partition(" ")
    return token.strip() if scheme.lower() == "bearer" and token.strip() else None


def api_key_actor(request: Request, services: Services, token: str) -> Actor:
    """Autentica a chave de API e aplica o limite de pedidos por chave."""
    auth = authenticate_api_key(services.trusted_uow(), token=token, clock=services.clock)
    result = services.bucket.take(f"key:{auth.key.id}", API_KEY, time.time())
    request.state.rate_limit = {
        "X-RateLimit-Limit": str(API_KEY.burst),
        "X-RateLimit-Remaining": str(result.remaining),
    }
    if not result.allowed:
        raise RateLimited(retry_after=max(result.retry_after, 1))
    request.state.api_key_id = auth.key.id
    return auth.actor


def get_actor(request: Request, services: Services = Depends(get_services)) -> Actor:
    """Sessão do painel ou chave de API. Com o cabeçalho Bearer, o cookie é ignorado."""
    token = bearer_token(request)
    if token is not None:
        return api_key_actor(request, services, token)
    return get_session_actor(get_auth(get_session_auth(optional_auth(request, services))))


def require(permission: str) -> Callable[[Actor], Actor]:
    """Depends(require("team.invite")): a permissão da rota fica declarada nela."""

    def dependency(actor: Actor = Depends(get_actor)) -> Actor:
        """Exige que o Actor tenha a permissão."""
        actor.grants.require(permission)
        return actor

    return dependency


def require_session(permission: str) -> Callable[[Actor], Actor]:
    """Como ``require``, mas recusa chave de API (criar chave, por exemplo)."""

    def dependency(actor: Actor = Depends(get_session_actor)) -> Actor:
        """Exige que o Actor da sessão tenha a permissão."""
        actor.grants.require(permission)
        return actor

    return dependency


def require_staff(permission: str) -> Callable[[Authenticated], Actor]:
    """Painel interno: a Company Groone ativa, 2FA verificado nesta sessão e a permissão.

    O core confere de novo a Company Groone em cada caso de uso."""

    def dependency(auth: Authenticated = Depends(get_auth)) -> Actor:
        """Exige a equipe Groone com a Company Groone ativa e a permissão."""
        if auth.active is None or auth.grants is None or not auth.active.company.is_internal:
            raise StaffOnly("só a equipe Groone, com a Company Groone ativa")
        if auth.session.mfa_verified_at is None:
            raise MfaRequired("entre com o 2FA para usar o painel interno")
        auth.grants.require(permission)
        return Actor(user_id=auth.user.id, company_id=auth.active.company.id, grants=auth.grants)

    return dependency


def get_cookies(services: Services = Depends(get_services)) -> SessionCookies:
    """Os cookies da sessão do painel, com as configurações e o relógio da aplicação."""
    return SessionCookies(services.settings, services.clock)
