"""Cookies da sessão do painel: o de sessão (httponly) e o de CSRF (legível pelo Vue).

Sempre com ``Secure`` e o prefixo ``__Host-``, em todo ambiente: nenhum subdomínio os grava e
nunca saem sem HTTPS. Chrome e Firefox aceitam ``Secure`` em ``http://localhost``.
"""

import secrets

from avant_core.identity.services import LoginResult
from avant_core.shared.clock import Clock
from fastapi import Response

SESSION_COOKIE = "__Host-avant_session"
CSRF_COOKIE = "__Host-avant_csrf"


class SessionCookies:
    """Grava e apaga os cookies da sessão com a validade dela."""

    def __init__(self, clock: Clock) -> None:
        self._clock = clock

    def open(self, response: Response, result: LoginResult) -> None:
        """Grava os cookies de sessão e de CSRF com a validade da sessão."""
        max_age = int((result.session.expires_at - self._clock.now()).total_seconds())
        self._set(response, SESSION_COOKIE, result.token, max_age, httponly=True)
        self._set(response, CSRF_COOKIE, secrets.token_urlsafe(32), max_age, httponly=False)

    def _set(
        self, response: Response, name: str, value: str, max_age: int, *, httponly: bool
    ) -> None:
        """Grava um cookie do painel com a validade e a segurança da sessão."""
        response.set_cookie(
            name,
            value,
            max_age=max_age,
            secure=True,
            samesite="lax",
            path="/",
            httponly=httponly,
        )

    def close(self, response: Response) -> None:
        """Apaga os cookies de sessão e de CSRF com os mesmos atributos da gravação, que o
        navegador exige para apagar um cookie ``__Host-``."""
        self._delete(response, SESSION_COOKIE, httponly=True)
        self._delete(response, CSRF_COOKIE, httponly=False)

    def _delete(self, response: Response, name: str, *, httponly: bool) -> None:
        """Apaga um cookie do painel com a segurança da sessão."""
        response.delete_cookie(
            name,
            secure=True,
            samesite="lax",
            path="/",
            httponly=httponly,
        )

    def session_token(self, cookies: dict[str, str]) -> str | None:
        """O token da sessão que veio no cookie, se veio."""
        return cookies.get(SESSION_COOKIE)
