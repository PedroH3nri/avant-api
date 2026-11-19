"""Ida ao login do Google para o Google Ads e volta ao painel, com o ``state`` num cookie curto."""

from urllib.parse import urlencode

from fastapi.responses import RedirectResponse

from avant_api.app.settings import Settings

WEB_GOOGLE_ADS = "/google-ads"
AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
CALLBACK_PATH = "/api/v1/google-ads/oauth/callback"
SCOPES = ("openid", "email", "https://www.googleapis.com/auth/adwords")

GOOGLE_ADS_COOKIE = "__Secure-avant_google_ads"
GOOGLE_ADS_COOKIE_PATH = "/api/v1/google-ads/oauth"
GOOGLE_ADS_COOKIE_TTL = 600


class GoogleAdsRedirects:
    """Monta o endereço do login do Google e as respostas de ida e de volta."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def redirect_uri(self) -> str:
        """O retorno que o cliente OAuth tem cadastrado."""
        return self._settings.app_base_url.rstrip("/") + CALLBACK_PATH

    def to_google(self, state: str) -> RedirectResponse:
        """Manda o navegador ao login do Google pedindo acesso offline ao Google Ads e guarda o
        ``state`` num cookie de 10 minutos."""
        query = {
            "client_id": self._settings.google_ads_client_id or "",
            "redirect_uri": self.redirect_uri,
            "state": state,
            "scope": " ".join(SCOPES),
            "response_type": "code",
            "access_type": "offline",
            "prompt": "consent",
            "include_granted_scopes": "true",
        }
        redirect = RedirectResponse(f"{AUTHORIZE_URL}?{urlencode(query)}", status_code=302)
        redirect.set_cookie(
            GOOGLE_ADS_COOKIE,
            state,
            max_age=GOOGLE_ADS_COOKIE_TTL,
            path=GOOGLE_ADS_COOKIE_PATH,
            httponly=True,
            secure=True,
            samesite="lax",
        )
        return redirect

    def back(self, *, error: str | None = None) -> RedirectResponse:
        """Volta à tela do Google Ads no painel com ``?google_ads=conectado`` ou ``?erro=``."""
        query = {"erro": error} if error else {"google_ads": "conectado"}
        url = self._settings.app_base_url.rstrip("/") + WEB_GOOGLE_ADS
        redirect = RedirectResponse(f"{url}?{urlencode(query)}", status_code=302)
        redirect.delete_cookie(
            GOOGLE_ADS_COOKIE,
            path=GOOGLE_ADS_COOKIE_PATH,
            secure=True,
            httponly=True,
            samesite="lax",
        )
        return redirect
