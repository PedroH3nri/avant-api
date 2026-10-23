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
from avant_core.identity.account import GoogleIdentity

from avant_api.errors import GoogleFailed

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
ISSUERS = frozenset({"https://accounts.google.com", "accounts.google.com"})


class GoogleAuth(Protocol):
    def authorize_url(self, *, state: str, verifier: str, nonce: str) -> str: ...
    def exchange(self, *, code: str, verifier: str, nonce: str) -> GoogleIdentity: ...


def new_verifier() -> str:
    return secrets.token_urlsafe(48)


def challenge(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode()


def _claims(id_token: str) -> dict[str, Any]:
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
    c = _claims(id_token)
    if c.get("iss") not in ISSUERS or c.get("aud") != client_id:
        raise GoogleFailed("id_token de outro emissor ou cliente")
    if float(c.get("exp", 0)) <= (now if now is not None else time.time()):
        raise GoogleFailed("id_token vencido")
    if not secrets.compare_digest(str(c.get("nonce", "")), nonce):
        raise GoogleFailed("nonce diferente")
    if not c.get("sub") or not c.get("email"):
        raise GoogleFailed("id_token sem sub ou e-mail")
    return GoogleIdentity(
        subject=str(c["sub"]), email=str(c["email"]), email_verified=c.get("email_verified") is True
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
        try:
            r = self._client.post(
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
        if r.status_code != 200:
            raise GoogleFailed(f"Google recusou o código (HTTP {r.status_code})")
        id_token = r.json().get("id_token")
        if not isinstance(id_token, str):
            raise GoogleFailed("resposta do Google sem id_token")
        return identity_from_id_token(id_token, client_id=self._id, nonce=nonce)
