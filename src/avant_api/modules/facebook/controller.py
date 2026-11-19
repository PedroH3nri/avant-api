"""Facebook da Empresa ativa (decisão 16), em /api/v1/facebook.

Ver pede ``facebook.view``; conectar perfis pede ``facebook.connect``; ligar, pausar, mudar
orçamento e regras pede ``facebook.manage``; passar contas para pessoas, limites e quem recebe
os avisos pedem ``facebook.accounts.manage``. Quem não tem
``facebook.accounts.manage`` vê só as contas que usa e os perfis que conectou (o core confere).
"""

import hmac
import secrets
import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.facebook.enums import FacebookChangeOrigin
from avant_core.facebook.models import FacebookObjectFilter
from avant_core.shared.errors import DomainError
from fastapi import APIRouter, Depends, Query, Request, status
from fastapi.responses import RedirectResponse

from avant_api.app.errors import FacebookDenied, FacebookStateInvalid
from avant_api.app.security import require, require_session
from avant_api.modules.facebook.dependencies import facebook_redirects, facebook_service
from avant_api.modules.facebook.dto import (
    FacebookAccountIn,
    FacebookAccountOut,
    FacebookAlertOut,
    FacebookAlertSettingOut,
    FacebookBudgetIn,
    FacebookBudgetOut,
    FacebookChangeOut,
    FacebookControlOut,
    FacebookObjectDetailOut,
    FacebookObjectOut,
    FacebookPersonIn,
    FacebookPersonOut,
    FacebookProfileOut,
    FacebookRuleDecisionOut,
    FacebookRuleIn,
    FacebookRuleOut,
    FacebookStatusIn,
)
from avant_api.modules.facebook.http import object_filter, period
from avant_api.modules.facebook.oauth import FACEBOOK_COOKIE, FacebookRedirects
from avant_api.modules.facebook.service import FacebookService
from avant_api.shared.dto import PageOut

VIEW = "facebook.view"
CONNECT = "facebook.connect"
ACCOUNTS = "facebook.accounts.manage"
MANAGE = "facebook.manage"

router = APIRouter(prefix="/facebook", tags=["facebook"])


@router.get("/oauth/start")
def oauth_start(
    actor: Actor = Depends(require_session(CONNECT)),
    service: FacebookService = Depends(facebook_service),
    redirects: FacebookRedirects = Depends(facebook_redirects),
) -> RedirectResponse:
    """Manda o navegador ao login do Facebook para conectar um perfil."""
    service.ensure_available()
    return redirects.to_facebook(secrets.token_urlsafe(24))


@router.get("/oauth/callback")
def oauth_callback(
    request: Request,
    code: str | None = Query(default=None, max_length=2048),
    state: str | None = Query(default=None, max_length=200),
    error: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require_session(CONNECT)),
    service: FacebookService = Depends(facebook_service),
    redirects: FacebookRedirects = Depends(facebook_redirects),
) -> RedirectResponse:
    """Volta do Facebook. Sempre termina na tela do Facebook do painel, com ``?erro=`` quando
    algo deu errado; o painel traduz o código."""
    expected = request.cookies.get(FACEBOOK_COOKIE, "")
    try:
        if not expected or not state or not hmac.compare_digest(expected, state):
            raise FacebookStateInvalid("state ausente ou diferente")
        if error or not code:
            raise FacebookDenied("login do Facebook cancelado ou sem permissão")
        service.connect(actor, code=code, redirect_uri=redirects.redirect_uri)
    except DomainError as failure:
        return redirects.back(error=failure.code)
    return redirects.back()


@router.get("/profiles")
def profiles(
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> list[FacebookProfileOut]:
    """Os perfis conectados que a pessoa vê, sem o token."""
    return service.profiles(actor)


@router.delete("/profiles/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
def disconnect(
    profile_id: uuid.UUID,
    actor: Actor = Depends(require_session(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> None:
    """Desconecta o perfil: a sincronia para, o Avant revoga as permissões e os números ficam."""
    service.disconnect(actor, profile_id)


@router.get("/accounts")
def accounts(
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> list[FacebookAccountOut]:
    """As contas de anúncio que a pessoa vê, com quem usa e o gasto do mês."""
    return service.accounts(actor)


@router.put("/accounts/{account_id}")
def update_account(
    account_id: uuid.UUID,
    body: FacebookAccountIn,
    actor: Actor = Depends(require(ACCOUNTS)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookAccountOut:
    """Troca o site, quem usa e os limites da conta."""
    return service.update_account(actor, account_id, body)


@router.get("/people")
def people(
    actor: Actor = Depends(require(ACCOUNTS)),
    service: FacebookService = Depends(facebook_service),
) -> list[FacebookPersonOut]:
    """As pessoas da Empresa com as contas que usam e os limites."""
    return service.people(actor)


@router.put("/people/{user_id}")
def set_person(
    user_id: uuid.UUID,
    body: FacebookPersonIn,
    actor: Actor = Depends(require(ACCOUNTS)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookPersonOut:
    """Passa as contas para a pessoa (tira de quem usava) e grava os limites dela."""
    return service.set_person(actor, user_id, body)


@router.get("/objects")
def objects(
    filters: FacebookObjectFilter = Depends(object_filter),
    dates: tuple[date, date] = Depends(period),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> PageOut[FacebookObjectOut]:
    """Uma página das campanhas, conjuntos ou anúncios, com gasto, receita, lucro e ROI."""
    return service.objects(actor, filters, dates[0], dates[1], page)


@router.post("/objects/status")
def set_status(
    body: FacebookStatusIn,
    actor: Actor = Depends(require(MANAGE)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookControlOut:
    """Liga ou pausa campanhas, conjuntos ou anúncios; ligar confere os limites antes."""
    return service.set_status(actor, body)


@router.put("/objects/{external_id}/budget")
def set_budget(
    external_id: str,
    body: FacebookBudgetIn,
    actor: Actor = Depends(require(MANAGE)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookBudgetOut:
    """Troca o orçamento diário ou o vitalício da campanha ou do conjunto."""
    return service.set_budget(actor, external_id, body)


@router.get("/objects/{external_id}/rules")
def rule(
    external_id: str,
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookRuleOut:
    """As regras automáticas do objeto (as sugeridas, desligadas, quando não há)."""
    return service.rule(actor, external_id)


@router.put("/objects/{external_id}/rules")
def set_rule(
    external_id: str,
    body: FacebookRuleIn,
    actor: Actor = Depends(require(MANAGE)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookRuleOut:
    """Grava as regras automáticas do objeto: escalar, pausar e duplicar pelo ROI."""
    return service.set_rule(actor, external_id, body)


@router.get("/objects/{external_id}/rule-decisions")
def rule_decisions(
    external_id: str,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> PageOut[FacebookRuleDecisionOut]:
    """Uma página do que as regras decidiram, a decisão mais nova primeiro."""
    return service.rule_decisions(actor, external_id, page)


@router.get("/objects/{external_id}")
def show_object(
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> FacebookObjectDetailOut:
    """Uma campanha, conjunto ou anúncio com os números por dia e por país."""
    return service.object(actor, external_id, dates[0], dates[1])


@router.get("/changes")
def changes(
    page: int = Query(default=1, ge=1),
    account_id: uuid.UUID | None = Query(default=None),
    object_id: str | None = Query(default=None, max_length=40),
    origin: FacebookChangeOrigin | None = Query(default=None),
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> PageOut[FacebookChangeOut]:
    """Uma página do histórico: quem mudou o quê, no Avant ou direto no Facebook."""
    return service.changes(actor, page, account_id, object_id, origin)


@router.get("/alerts")
def alerts(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> PageOut[FacebookAlertOut]:
    """Uma página dos avisos da pessoa, o mais novo primeiro."""
    return service.alerts(actor, page)


@router.post("/alerts/{alert_id}/read", status_code=status.HTTP_204_NO_CONTENT)
def read_alert(
    alert_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: FacebookService = Depends(facebook_service),
) -> None:
    """Marca o aviso como lido."""
    service.read_alert(actor, alert_id)


@router.get("/alert-settings")
def alert_settings(
    actor: Actor = Depends(require(ACCOUNTS)),
    service: FacebookService = Depends(facebook_service),
) -> list[FacebookAlertSettingOut]:
    """Quem recebe cada tipo de aviso e se vai por e-mail."""
    return service.alert_settings(actor)


@router.put("/alert-settings")
def set_alert_settings(
    body: list[FacebookAlertSettingOut],
    actor: Actor = Depends(require(ACCOUNTS)),
    service: FacebookService = Depends(facebook_service),
) -> list[FacebookAlertSettingOut]:
    """Grava quem recebe os tipos de aviso enviados; os outros ficam como estavam."""
    return service.set_alert_settings(actor, body)
