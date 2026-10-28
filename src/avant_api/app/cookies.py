"""Cookies da sessão do painel: o de sessão (httponly) e o de CSRF (legível pelo Vue)."""

import secrets

from avant_core.identity.services import LoginResult
from avant_core.shared.clock import Clock
from fastapi import Response

from avant_api.app.settings import Settings


class SessionCookies:
    """Grava e apaga os cookies da sessão com a validade dela."""

    def __init__(self, settings: Settings, clock: Clock) -> None:
        self._settings = settings
        self._clock = clock

    def open(self, response: Response, result: LoginResult) -> None:
        """Grava os cookies de sessão e de CSRF com a validade da sessão."""
        max_age = int((result.session.expires_at - self._clock.now()).total_seconds())
        self._set(response, self._settings.session_cookie, result.token, max_age, httponly=True)
        self._set(
            response, self._settings.csrf_cookie, secrets.token_urlsafe(32), max_age, httponly=False
        )

    def _set(
        self, response: Response, name: str, value: str, max_age: int, *, httponly: bool
    ) -> None:
        """Grava um cookie do painel com a validade e a segurança da sessão."""
        response.set_cookie(
            name,
            value,
            max_age=max_age,
            secure=self._settings.cookie_secure,
            samesite="lax",
            path="/",
            httponly=httponly,
        )

    def close(self, response: Response) -> None:
        """Apaga os cookies de sessão e de CSRF."""
        response.delete_cookie(self._settings.session_cookie, path="/")
        response.delete_cookie(self._settings.csrf_cookie, path="/")

    def session_token(self, cookies: dict[str, str]) -> str | None:
        """O token da sessão que veio no cookie, se veio."""
        return cookies.get(self._settings.session_cookie)
