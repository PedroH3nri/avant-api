"""Service da conta da pessoa: senha e sessões ativas.

Tudo aqui é da pessoa e não de uma Empresa, por isso usa trusted_uow, como o login.
"""

import uuid

from avant_core.identity.account import (
    change_password,
    list_sessions,
    request_password_reset,
    reset_password,
    revoke_other_sessions,
    revoke_session,
)
from avant_core.identity.application import Authenticated
from avant_core.ports import Mailer, PasswordHasher, SecretBox
from avant_core.shared.clock import Clock
from avant_core.shared.errors import InvalidToken

from avant_api.app.limits import PASSWORD_IP, Limiter
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.account.dto import ChangePasswordIn, ResetPasswordIn, SessionOut


class AccountService:
    """Senha esquecida, troca de senha e sessões abertas da pessoa."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        hasher: PasswordHasher,
        box: SecretBox,
        mailer: Mailer,
        limiter: Limiter,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._hasher = hasher
        self._box = box
        self._mailer = mailer
        self._limiter = limiter

    def forgot_password(self, email: str, ip: str | None) -> None:
        """Manda o link de redefinição; todo pedido conta no limite por IP."""
        self._limiter.check((PASSWORD_IP, ip))
        self._limiter.fail((PASSWORD_IP, ip))
        request_password_reset(
            self._uows.trusted_uow(), email=email, clock=self._clock, mailer=self._mailer
        )

    def reset_password(self, body: ResetPasswordIn, ip: str | None) -> None:
        """Troca a senha pelo link e encerra todas as sessões da pessoa."""
        self._limiter.check((PASSWORD_IP, ip))
        try:
            reset_password(
                self._uows.trusted_uow(),
                token=body.token,
                password=body.password,
                mfa_code=body.mfa_code,
                hasher=self._hasher,
                box=self._box,
                clock=self._clock,
                mailer=self._mailer,
            )
        except InvalidToken:
            self._limiter.fail((PASSWORD_IP, ip))
            raise

    def change_password(self, auth: Authenticated, body: ChangePasswordIn) -> None:
        """Troca a senha, mantém a sessão atual e encerra as outras."""
        change_password(
            self._uows.trusted_uow(),
            user_id=auth.user.id,
            session_id=auth.session.id,
            current=body.current_password,
            new=body.new_password,
            hasher=self._hasher,
            clock=self._clock,
            mailer=self._mailer,
        )

    def sessions(self, auth: Authenticated) -> list[SessionOut]:
        """As sessões abertas da pessoa, da mais recente para a mais antiga."""
        rows = list_sessions(self._uows.trusted_uow(), user_id=auth.user.id, clock=self._clock)
        rows.sort(key=lambda session: session.last_seen_at, reverse=True)
        return [
            SessionOut(
                id=session.id,
                created_at=session.created_at,
                last_seen_at=session.last_seen_at,
                expires_at=session.expires_at,
                user_agent=session.user_agent,
                ip=str(session.ip) if session.ip is not None else None,
                current=session.id == auth.session.id,
            )
            for session in rows
        ]

    def revoke_session(self, user_id: uuid.UUID, session_id: uuid.UUID) -> None:
        """Encerra uma sessão da pessoa."""
        revoke_session(
            self._uows.trusted_uow(), user_id=user_id, session_id=session_id, clock=self._clock
        )

    def revoke_others(self, auth: Authenticated) -> int:
        """Encerra todas as sessões da pessoa menos a atual e diz quantas foram."""
        return revoke_other_sessions(
            self._uows.trusted_uow(),
            user_id=auth.user.id,
            keep_session_id=auth.session.id,
            clock=self._clock,
        )
