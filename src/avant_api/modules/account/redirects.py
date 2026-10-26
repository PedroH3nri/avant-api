"""Redirecionamentos e cookie do fluxo do Google, que volta para telas do painel."""

from urllib.parse import urlencode

from fastapi.responses import RedirectResponse

from avant_api.app.settings import Settings

WEB_LOGIN = "/entrar"
WEB_MFA = "/entrar/2fa"
WEB_ACCOUNT = "/configuracoes/conta"

GOOGLE_COOKIE = "avant_google"
GOOGLE_COOKIE_PATH = "/api/v1/auth/google"
GOOGLE_COOKIE_TTL = 600


class GoogleRedirects:
    """Monta as respostas de ida ao Google e de volta ao painel."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def to_google(self, url: str, flow: str) -> RedirectResponse:
        """Manda o navegador ao Google com o estado do fluxo num cookie curto."""
        redirect = RedirectResponse(url, status_code=302)
        redirect.set_cookie(
            GOOGLE_COOKIE,
            flow,
            max_age=GOOGLE_COOKIE_TTL,
            path=GOOGLE_COOKIE_PATH,
            httponly=True,
            secure=self._settings.cookie_secure,
            samesite="lax",
        )
        return redirect

    def back(
        self, path: str, *, error: str | None = None, google: str | None = None
    ) -> RedirectResponse:
        """Redireciona de volta ao painel com o resultado na query string."""
        query = {key: value for key, value in (("erro", error), ("google", google)) if value}
        url = self._settings.app_base_url.rstrip("/") + path
        redirect = RedirectResponse(
            url + (f"?{urlencode(query)}" if query else ""), status_code=302
        )
        redirect.delete_cookie(GOOGLE_COOKIE, path=GOOGLE_COOKIE_PATH)
        return redirect
