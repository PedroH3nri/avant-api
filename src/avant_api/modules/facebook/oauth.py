"""Ida ao login do Facebook e volta ao painel, com o ``state`` num cookie curto."""

from urllib.parse import urlencode

from fastapi.responses import RedirectResponse

from avant_api.app.settings import Settings

WEB_FACEBOOK = "/facebook"
DIALOG = "https://www.facebook.com/{version}/dialog/oauth"
CALLBACK_PATH = "/api/v1/facebook/oauth/callback"
SCOPES = ("ads_read", "ads_management", "business_management")

FACEBOOK_COOKIE = "__Secure-avant_facebook"
FACEBOOK_COOKIE_PATH = "/api/v1/facebook/oauth"
FACEBOOK_COOKIE_TTL = 600


class FacebookRedirects:
    """Monta o endereço do login do Facebook e as respostas de ida e de volta."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    @property
    def redirect_uri(self) -> str:
        """O retorno que o app da Meta tem cadastrado."""
        return self._settings.app_base_url.rstrip("/") + CALLBACK_PATH

    def to_facebook(self, state: str) -> RedirectResponse:
        """Manda o navegador ao login do Facebook e guarda o ``state`` num cookie de 10 minutos."""
        query = {
            "client_id": self._settings.facebook_app_id or "",
            "redirect_uri": self.redirect_uri,
            "state": state,
            "scope": ",".join(SCOPES),
            "response_type": "code",
        }
        url = DIALOG.format(version=self._settings.facebook_graph_version)
        redirect = RedirectResponse(f"{url}?{urlencode(query)}", status_code=302)
        redirect.set_cookie(
            FACEBOOK_COOKIE,
            state,
            max_age=FACEBOOK_COOKIE_TTL,
            path=FACEBOOK_COOKIE_PATH,
            httponly=True,
            secure=True,
            samesite="lax",
        )
        return redirect

    def back(self, *, error: str | None = None) -> RedirectResponse:
        """Volta à tela do Facebook no painel com ``?facebook=conectado`` ou ``?erro=``."""
        query = {"erro": error} if error else {"facebook": "conectado"}
        url = self._settings.app_base_url.rstrip("/") + WEB_FACEBOOK
        redirect = RedirectResponse(f"{url}?{urlencode(query)}", status_code=302)
        redirect.delete_cookie(
            FACEBOOK_COOKIE, path=FACEBOOK_COOKIE_PATH, secure=True, httponly=True, samesite="lax"
        )
        return redirect
