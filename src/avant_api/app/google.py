"""Login com Google: OpenID Connect com código de autorização e PKCE.

O id_token vem direto do endpoint de token do Google, numa conexão TLS da própria API,
então basta conferir aud, iss, exp e nonce (OpenID Connect Core, 3.1.3.7). O Avant usa
só o sub, o e-mail e o email_verified.
"""

import base64
import hashlib
import json
import secrets
import time
from typing import Any, Protocol
from urllib.parse import urlencode

import httpx
from avant_core.identity.services import GoogleIdentity

from avant_api.app.errors import GoogleFailed

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
ISSUERS = frozenset({"https://accounts.google.com", "accounts.google.com"})


class GoogleAuth(Protocol):
    def authorize_url(self, *, state: str, verifier: str, nonce: str) -> str:
        """Monta o link de login do Google com PKCE e nonce."""
        ...

    def exchange(self, *, code: str, verifier: str, nonce: str) -> GoogleIdentity:
        """Troca o código do Google pela identidade da pessoa."""
        ...


def new_verifier() -> str:
    """Gera o code_verifier do PKCE."""
    return secrets.token_urlsafe(48)


def challenge(verifier: str) -> str:
    """Calcula o code_challenge (S256) do code_verifier."""
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()


def _claims(id_token: str) -> dict[str, Any]:
    """Lê as claims do id_token; a assinatura não é conferida porque ele vem direto do Google."""
    try:
        payload = id_token.split(".")[1]
        data: dict[str, Any] = json.loads(
            base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4))
        )
    except (IndexError, ValueError) as exc:
        raise GoogleFailed("id_token ilegível") from exc
    return data


def identity_from_id_token(
    id_token: str, *, client_id: str, nonce: str, now: float | None = None
) -> GoogleIdentity:
    """Confere emissor, cliente, nonce e validade do id_token e devolve a identidade."""
    claims = _claims(id_token)
    if claims.get("iss") not in ISSUERS or claims.get("aud") != client_id:
        raise GoogleFailed("id_token de outro emissor ou cliente")
    if float(claims.get("exp", 0)) <= (now if now is not None else time.time()):
        raise GoogleFailed("id_token vencido")
    if not secrets.compare_digest(str(claims.get("nonce", "")), nonce):
        raise GoogleFailed("nonce diferente")
    if not claims.get("sub") or not claims.get("email"):
        raise GoogleFailed("id_token sem sub ou e-mail")
    return GoogleIdentity(
        subject=str(claims["sub"]),
        email=str(claims["email"]),
        email_verified=claims.get("email_verified") is True,
    )


class GoogleOAuth:
    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        redirect_uri: str,
        client: httpx.Client | None = None,
    ) -> None:
        self._id = client_id
        self._secret = client_secret
        self._redirect = redirect_uri
        self._client = client or httpx.Client(timeout=10.0)

    def authorize_url(self, *, state: str, verifier: str, nonce: str) -> str:
        """Monta o link de login do Google com PKCE e nonce."""
        query = {
            "client_id": self._id,
            "redirect_uri": self._redirect,
            "response_type": "code",
            "scope": "openid email",
            "state": state,
            "nonce": nonce,
            "code_challenge": challenge(verifier),
            "code_challenge_method": "S256",
            "prompt": "select_account",
        }
        return f"{AUTHORIZE_URL}?{urlencode(query)}"

    def exchange(self, *, code: str, verifier: str, nonce: str) -> GoogleIdentity:
        """Troca o código do Google pelo id_token e devolve a identidade conferida."""
        try:
            response = self._client.post(
                TOKEN_URL,
                data={
                    "code": code,
                    "client_id": self._id,
                    "client_secret": self._secret,
                    "redirect_uri": self._redirect,
                    "grant_type": "authorization_code",
                    "code_verifier": verifier,
                },
            )
        except httpx.HTTPError as exc:
            raise GoogleFailed("sem resposta do Google") from exc
        if response.status_code != 200:
            raise GoogleFailed(f"Google recusou o código (HTTP {response.status_code})")
        id_token = response.json().get("id_token")
        if not isinstance(id_token, str):
            raise GoogleFailed("resposta do Google sem id_token")
        return identity_from_id_token(id_token, client_id=self._id, nonce=nonce)
