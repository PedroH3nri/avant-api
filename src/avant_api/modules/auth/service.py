"""Service do login, da sessão, da Empresa ativa e do aceite de convite.

Tudo aqui acontece antes de haver uma Empresa escolhida, por isso usa trusted_uow.
"""

import uuid

from avant_core.company.model import Membership
from avant_core.company.service import (
    ExistingAccount,
    NewAccount,
    accept_invitation,
    preview_invitation,
)
from avant_core.identity.model import normalize_email
from avant_core.identity.service import (
    Authenticated,
    LoginResult,
    authenticate,
    login_with_password,
    logout,
    start_session,
    switch_active_company,
)
from avant_core.ports import PasswordHasher
from avant_core.shared.clock import Clock
from avant_core.shared.errors import InvalidCredentials, WrongInvitationKind

from avant_api.app.limits import LOGIN_EMAIL, LOGIN_IP, Limiter
from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.auth.dto import AcceptInvitationIn, InvitationPreviewOut, LoginIn


class AuthService:
    """Entrada com senha, sessão e convites de quem ainda não está numa Empresa."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, hasher: PasswordHasher, limiter: Limiter
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._hasher = hasher
        self._limiter = limiter

    def login(self, body: LoginIn, user_agent: str | None, ip: str | None) -> LoginResult:
        """Confere a senha com limite de 5 erros por e-mail e 20 por IP em 15 minutos."""
        email = normalize_email(body.email)
        keys = ((LOGIN_EMAIL, email), (LOGIN_IP, ip))
        self._limiter.check(*keys)
        try:
            result = login_with_password(
                self._uows.trusted_uow(),
                email=email,
                password=body.password,
                hasher=self._hasher,
                clock=self._clock,
                user_agent=user_agent,
                ip=ip,
            )
        except InvalidCredentials:
            self._limiter.fail(*keys)
            raise
        self._limiter.clear(LOGIN_EMAIL, email)
        return result

    def authenticate(self, token: str) -> Authenticated:
        """A pessoa autenticada pelo token da sessão."""
        return authenticate(self._uows.trusted_uow(), token=token, clock=self._clock)

    def logout(self, session_id: uuid.UUID) -> None:
        """Encerra a sessão."""
        logout(self._uows.trusted_uow(), session_id=session_id, clock=self._clock)

    def switch_company(
        self, auth: Authenticated, company_id: uuid.UUID, token: str
    ) -> Authenticated:
        """Troca a Empresa ativa da sessão e devolve a pessoa já nela."""
        switch_active_company(
            self._uows.trusted_uow(), session_id=auth.session.id, company_id=company_id
        )
        return self.authenticate(token)

    def preview_invitation(self, token: str) -> InvitationPreviewOut:
        """O convite antes do aceite."""
        preview = preview_invitation(self._uows.trusted_uow(), token=token, clock=self._clock)
        return InvitationPreviewOut(**preview.__dict__)

    def accept_logged_in(
        self, token: str, auth: Authenticated, session_token: str
    ) -> Authenticated:
        """Aceita com a conta logada e passa a sessão para a Empresa do convite."""
        membership = self._accept(token, ExistingAccount(auth.user.id))
        return self.switch_company(auth, membership.company_id, session_token)

    def accept_new_account(
        self, token: str, body: AcceptInvitationIn, user_agent: str | None, ip: str | None
    ) -> LoginResult:
        """Cria a conta pelo convite e já abre uma sessão na Empresa dele."""
        if not (body.name and body.password):
            raise WrongInvitationKind("sem sessão, informe name e password para criar a conta")
        account = NewAccount(name=body.name, password=body.password, locale=body.locale)
        membership = self._accept(token, account)
        return start_session(
            self._uows.trusted_uow(),
            user_id=membership.user_id,
            clock=self._clock,
            user_agent=user_agent,
            ip=ip,
        )

    def _accept(self, token: str, account: NewAccount | ExistingAccount) -> Membership:
        """Aceita o convite com a conta dada."""
        return accept_invitation(
            self._uows.trusted_uow(),
            token=token,
            account=account,
            clock=self._clock,
            hasher=self._hasher,
        )
