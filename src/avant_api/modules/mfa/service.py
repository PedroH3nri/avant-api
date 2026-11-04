"""Service do 2FA: segundo passo do login, configuração e códigos de recuperação."""

import uuid

from avant_core.identity.errors import InvalidMfaCode, MfaAttemptsExceeded, MfaLocked
from avant_core.identity.services import (
    LoginResult,
    MfaSetup,
    begin_mfa_setup,
    confirm_mfa_setup,
    disable_mfa,
    regenerate_recovery_codes,
    verify_mfa,
)
from avant_core.ports import Mailer, SecretBox
from avant_core.shared.clock import Clock

from avant_api.app.limits import MFA_IP, Limiter
from avant_api.app.ports import UnitOfWorkFactory


class MfaService:
    """2FA por TOTP da pessoa; é da conta e não de uma Empresa."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        box: SecretBox,
        mailer: Mailer,
        limiter: Limiter,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._box = box
        self._mailer = mailer
        self._limiter = limiter

    def verify(self, token: str, code: str, user_agent: str | None, ip: str | None) -> LoginResult:
        """Troca a pré-sessão do cookie por uma sessão completa, com limite de 20 erros por IP.

        Insistir com o 2FA travado também conta.
        """
        failures = (InvalidMfaCode, MfaAttemptsExceeded, MfaLocked)
        with self._limiter.attempt((MFA_IP, ip), counts=failures):
            return verify_mfa(
                self._uows.trusted_uow(),
                token=token,
                code=code,
                box=self._box,
                clock=self._clock,
                user_agent=user_agent,
                ip=ip,
            )

    def begin_setup(self, user_id: uuid.UUID) -> MfaSetup:
        """Começa a configurar o 2FA com um segredo novo."""
        return begin_mfa_setup(self._uows.trusted_uow(), user_id=user_id, box=self._box)

    def confirm(self, user_id: uuid.UUID, session_id: uuid.UUID, code: str) -> list[str]:
        """Liga o 2FA com o primeiro código e devolve os códigos de recuperação."""
        return confirm_mfa_setup(
            self._uows.trusted_uow(),
            user_id=user_id,
            session_id=session_id,
            code=code,
            box=self._box,
            clock=self._clock,
        )

    def new_recovery_codes(self, user_id: uuid.UUID, code: str) -> list[str]:
        """Gera códigos de recuperação novos depois de conferir um código e avisa por e-mail."""
        return regenerate_recovery_codes(
            self._uows.trusted_uow(),
            user_id=user_id,
            code=code,
            box=self._box,
            clock=self._clock,
            mailer=self._mailer,
        )

    def disable(self, user_id: uuid.UUID, code: str) -> None:
        """Desliga o 2FA depois de conferir um código."""
        disable_mfa(
            self._uows.trusted_uow(), user_id=user_id, code=code, box=self._box, clock=self._clock
        )
