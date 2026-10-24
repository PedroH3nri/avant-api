"""2FA: /api/v1/auth/mfa."""

from avant_core.identity.application import Authenticated
from avant_core.identity.mfa import (
    begin_mfa_setup,
    confirm_mfa_setup,
    disable_mfa,
    regenerate_recovery_codes,
    verify_mfa,
)
from avant_core.shared.errors import NotAuthenticated
from fastapi import APIRouter, Depends, Request, Response, status

from avant_api.deps import get_services, get_session_auth
from avant_api.routes.auth import _client, _start
from avant_api.schemas import MeOut, MfaCodeIn, MfaSetupOut, RecoveryCodesOut
from avant_api.services import Services

router = APIRouter(prefix="/auth/mfa", tags=["auth"])


@router.post("/verify")
def verify(
    body: MfaCodeIn,
    request: Request,
    response: Response,
    services: Services = Depends(get_services),
) -> MeOut:
    """Segundo passo do login: o cookie tem a pré-sessão e vira uma sessão completa."""
    token = request.cookies.get(services.settings.session_cookie)
    if not token:
        raise NotAuthenticated()
    user_agent, ip = _client(request)
    result = verify_mfa(
        services.trusted_uow(),
        token=token,
        code=body.code,
        box=services.box,
        clock=services.clock,
        user_agent=user_agent,
        ip=ip,
    )
    return MeOut.of(_start(response, services, result))


@router.post("/setup")
def setup(
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> MfaSetupOut:
    """Começa a configurar o 2FA e devolve o segredo e o link do QR code."""
    mfa_setup = begin_mfa_setup(services.trusted_uow(), user_id=auth.user.id, box=services.box)
    return MfaSetupOut(secret=mfa_setup.secret, uri=mfa_setup.uri)


@router.post("/confirm")
def confirm(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> RecoveryCodesOut:
    """Liga o 2FA com o primeiro código e devolve os códigos de recuperação."""
    codes = confirm_mfa_setup(
        services.trusted_uow(),
        user_id=auth.user.id,
        session_id=auth.session.id,
        code=body.code,
        box=services.box,
        clock=services.clock,
    )
    return RecoveryCodesOut(recovery_codes=codes)


@router.post("/recovery-codes")
def new_recovery_codes(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> RecoveryCodesOut:
    """Gera códigos de recuperação novos depois de conferir um código."""
    codes = regenerate_recovery_codes(
        services.trusted_uow(),
        user_id=auth.user.id,
        code=body.code,
        box=services.box,
        clock=services.clock,
    )
    return RecoveryCodesOut(recovery_codes=codes)


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def disable(
    body: MfaCodeIn,
    auth: Authenticated = Depends(get_session_auth),
    services: Services = Depends(get_services),
) -> None:
    """Desliga o 2FA depois de conferir um código."""
    disable_mfa(
        services.trusted_uow(),
        user_id=auth.user.id,
        code=body.code,
        box=services.box,
        clock=services.clock,
    )
