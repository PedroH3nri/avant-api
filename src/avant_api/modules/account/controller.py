"""Conta da pessoa: senha e sessões ativas, em /api/v1/auth."""

import uuid

from avant_core.identity.services import Authenticated
from fastapi import APIRouter, Depends, Request, Response, status

from avant_api.app.cookies import SessionCookies
from avant_api.app.security import get_cookies, get_session_auth
from avant_api.modules.account.dependencies import account_service
from avant_api.modules.account.dto import (
    ChangePasswordIn,
    ForgotPasswordIn,
    ResetPasswordIn,
    RevokedOut,
    SessionOut,
)
from avant_api.modules.account.service import AccountService
from avant_api.shared.http import client_info

router = APIRouter(prefix="/auth", tags=["account"])


@router.post("/password/forgot", status_code=status.HTTP_202_ACCEPTED)
def forgot_password(
    body: ForgotPasswordIn,
    request: Request,
    service: AccountService = Depends(account_service),
) -> None:
    """Responde 202 exista ou não a conta, para não revelar quem tem cadastro."""
    _, ip = client_info(request)
    service.forgot_password(body.email, ip)


@router.post("/password/reset", status_code=status.HTTP_204_NO_CONTENT)
def do_reset_password(
    body: ResetPasswordIn,
    request: Request,
    response: Response,
    service: AccountService = Depends(account_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> None:
    """Encerra todas as sessões, inclusive a deste navegador: a pessoa entra de novo."""
    _, ip = client_info(request)
    service.reset_password(body, ip)
    cookies.close(response)


@router.post("/password/change", status_code=status.HTTP_204_NO_CONTENT)
def do_change_password(
    body: ChangePasswordIn,
    auth: Authenticated = Depends(get_session_auth),
    service: AccountService = Depends(account_service),
) -> None:
    """Mantém a sessão atual e encerra as outras."""
    service.change_password(auth, body)


@router.get("/sessions")
def get_sessions(
    auth: Authenticated = Depends(get_session_auth),
    service: AccountService = Depends(account_service),
) -> list[SessionOut]:
    """Lista as sessões abertas da pessoa, da mais recente para a mais antiga."""
    return service.sessions(auth)


@router.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(
    session_id: uuid.UUID,
    response: Response,
    auth: Authenticated = Depends(get_session_auth),
    service: AccountService = Depends(account_service),
    cookies: SessionCookies = Depends(get_cookies),
) -> None:
    """Encerra uma sessão da pessoa; se for a atual, apaga os cookies."""
    service.revoke_session(auth.user.id, session_id)
    if session_id == auth.session.id:
        cookies.close(response)


@router.post("/sessions/revoke-others")
def revoke_others(
    auth: Authenticated = Depends(get_session_auth),
    service: AccountService = Depends(account_service),
) -> RevokedOut:
    """Encerra todas as sessões da pessoa menos a atual."""
    return RevokedOut(revoked=service.revoke_others(auth))
