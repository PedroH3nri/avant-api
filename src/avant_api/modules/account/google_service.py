"""Service do login com Google e da ligação da conta Google à pessoa."""

import uuid

from avant_core.identity.account_service import (
    has_google,
    link_google,
    login_with_google,
    unlink_google,
)
from avant_core.identity.service import LoginResult, authenticate
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock
from avant_core.shared.errors import NotAuthenticated

from avant_api.app.errors import GoogleUnavailable
from avant_api.app.google import GoogleAuth
from avant_api.app.ports import UnitOfWorkFactory


class GoogleService:
    """Fluxo OAuth do Google; sem cliente configurado, o login com Google não existe."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer, google: GoogleAuth | None
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer
        self._google = google

    @property
    def available(self) -> bool:
        """Se o login com Google está configurado."""
        return self._google is not None

    def ensure_available(self) -> None:
        """Recusa com ``google_unavailable`` quando o login com Google não está configurado."""
        self._client()

    def is_linked(self, user_id: uuid.UUID) -> bool:
        """Se a pessoa já ligou uma conta Google."""
        return has_google(self._uows.trusted_uow(), user_id=user_id)

    def unlink(self, user_id: uuid.UUID) -> None:
        """Desliga a conta Google da pessoa."""
        unlink_google(self._uows.trusted_uow(), user_id=user_id)

    def authorize_url(self, *, state: str, verifier: str, nonce: str) -> str:
        """O endereço do Google para onde o navegador vai."""
        return self._client().authorize_url(state=state, verifier=verifier, nonce=nonce)

    def link(self, session_token: str | None, *, code: str, verifier: str, nonce: str) -> None:
        """Liga a conta Google que voltou do callback à pessoa da sessão; sem sessão é 401."""
        identity = self._client().exchange(code=code, verifier=verifier, nonce=nonce)
        if not session_token:
            raise NotAuthenticated()
        auth = authenticate(self._uows.trusted_uow(), token=session_token, clock=self._clock)
        if auth.mfa_setup_required:
            raise NotAuthenticated()
        link_google(
            self._uows.trusted_uow(),
            user_id=auth.user.id,
            identity=identity,
            clock=self._clock,
            mailer=self._mailer,
        )

    def login(
        self, *, code: str, verifier: str, nonce: str, user_agent: str | None, ip: str | None
    ) -> LoginResult:
        """Entra com a conta Google que voltou do callback."""
        identity = self._client().exchange(code=code, verifier=verifier, nonce=nonce)
        return login_with_google(
            self._uows.trusted_uow(),
            identity=identity,
            clock=self._clock,
            user_agent=user_agent,
            ip=ip,
        )

    def _client(self) -> GoogleAuth:
        """O cliente OAuth do Google, ou recusa quando não está configurado."""
        if self._google is None:
            raise GoogleUnavailable("login com Google não configurado")
        return self._google
