"""2FA: /api/v1/auth/mfa."""

from avant_core.identity.services import Authenticated
from avant_core.shared.errors import NotAuthenticated
from fastapi import APIRouter, Depends, Request, Response, status

from avant_api.app.cookies import SessionCookies
from avant_api.app.security import get_cookies, get_session_auth
from avant_api.modules.auth.dependencies import auth_service
from avant_api.modules.auth.dto import MeOut
from avant_api.modules.auth.service import AuthService
from avant_api.modules.mfa.dependencies import mfa_service
from avant_api.modules.mfa.dto import MfaCodeIn, MfaSetupOut, RecoveryCodesOut
from avant_api.modules.mfa.service import MfaService
from avant_api.shared.http import client_info

router = APIRouter(prefix="/auth/mfa", tags=["auth"])


@router.post("/verify")
def verify(
    body: MfaCodeIn,
    request: Request,
    response: Response,
    service: MfaService = Depends(mfa_service),
    login_service: AuthService = Depends(auth_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> MeOut:
    """Segundo passo do login: o cookie tem a pré-sessão e vira uma sessão completa."""
    token = cookies.session_token(request.cookies)
    if not token:
        raise NotAuthenticated()
    user_agent, ip = client_info(request)
    result = service.verify(token, body.code, user_agent, ip)
    cookies.open(response, result)
    return MeOut.of(login_service.authenticate(result.token))


@router.post("/setup")
def setup(
    auth: Authenticated = Depends(get_session_auth),
    service: MfaService = Depends(mfa_service),
) -> MfaSetupOut:
    """Começa a configurar o 2FA e devolve o segredo e o link do QR code."""
    mfa_setup = service.begin_setup(auth.user.id)
    return MfaSetupOut(secret=mfa_setup.secret, uri=mfa_setup.uri)


@router.post("/confirm")
def confirm(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    service: MfaService = Depends(mfa_service),
) -> RecoveryCodesOut:
    """Liga o 2FA com o primeiro código e devolve os códigos de recuperação."""
    codes = service.confirm(auth.user.id, auth.session.id, body.code)
    return RecoveryCodesOut(recovery_codes=codes)


@router.post("/recovery-codes")
def new_recovery_codes(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    service: MfaService = Depends(mfa_service),
) -> RecoveryCodesOut:
    """Gera códigos de recuperação novos depois de conferir um código."""
    return RecoveryCodesOut(recovery_codes=service.new_recovery_codes(auth.user.id, body.code))


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def disable(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    service: MfaService = Depends(mfa_service),
) -> None:
    """Desliga o 2FA depois de conferir um código."""
    service.disable(auth.user.id, body.code)
