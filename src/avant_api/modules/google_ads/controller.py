"""Google Ads da Empresa ativa (decisão 17), em /api/v1/google-ads.

Ver pede ``google_ads.view``; conectar logins do Google pede ``google_ads.connect``; passar
contas para pessoas, limites, o sufixo de URL e quem recebe os avisos pedem
``google_ads.accounts.manage``. Quem não tem ``google_ads.accounts.manage`` vê só as contas que
usa e os logins que conectou (o core confere).
"""

import hmac
import secrets
import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.google_ads.enums import GoogleAdsChangeOrigin, GoogleAdsLevel
from avant_core.google_ads.models import GoogleAdsObjectFilter
from avant_core.shared.errors import DomainError
from fastapi import APIRouter, Depends, Query, Request, status
from fastapi.responses import RedirectResponse

from avant_api.app.errors import GoogleAdsDenied, GoogleAdsStateInvalid
from avant_api.app.security import require, require_session
from avant_api.modules.google_ads.dependencies import google_ads_redirects, google_ads_service
from avant_api.modules.google_ads.dto import (
    GoogleAdsAccountIn,
    GoogleAdsAccountOut,
    GoogleAdsAlertOut,
    GoogleAdsAlertSettingOut,
    GoogleAdsChangeOut,
    GoogleAdsKeywordOut,
    GoogleAdsLoginOut,
    GoogleAdsObjectDetailOut,
    GoogleAdsObjectOut,
    GoogleAdsPersonIn,
    GoogleAdsPersonOut,
    GoogleAdsTermOut,
)
from avant_api.modules.google_ads.http import object_filter
from avant_api.modules.google_ads.oauth import GOOGLE_ADS_COOKIE, GoogleAdsRedirects
from avant_api.modules.google_ads.service import GoogleAdsService
from avant_api.shared.ads import period
from avant_api.shared.dto import PageOut

VIEW = "google_ads.view"
CONNECT = "google_ads.connect"
ACCOUNTS = "google_ads.accounts.manage"

router = APIRouter(prefix="/google-ads", tags=["google-ads"])


@router.get("/oauth/start")
def oauth_start(
    actor: Actor = Depends(require_session(CONNECT)),
    service: GoogleAdsService = Depends(google_ads_service),
    redirects: GoogleAdsRedirects = Depends(google_ads_redirects),
) -> RedirectResponse:
    """Manda o navegador ao login do Google para conectar as contas do Google Ads."""
    service.ensure_available()
    return redirects.to_google(secrets.token_urlsafe(24))


@router.get("/oauth/callback")
def oauth_callback(
    request: Request,
    code: str | None = Query(default=None, max_length=2048),
    state: str | None = Query(default=None, max_length=200),
    error: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require_session(CONNECT)),
    service: GoogleAdsService = Depends(google_ads_service),
    redirects: GoogleAdsRedirects = Depends(google_ads_redirects),
) -> RedirectResponse:
    """Volta do Google. Sempre termina na tela do Google Ads do painel, com ``?erro=`` quando
    algo deu errado; o painel traduz o código."""
    expected = request.cookies.get(GOOGLE_ADS_COOKIE, "")
    try:
        if not expected or not state or not hmac.compare_digest(expected, state):
            raise GoogleAdsStateInvalid("state ausente ou diferente")
        if error or not code:
            raise GoogleAdsDenied("login do Google cancelado ou sem acesso ao Google Ads")
        service.connect(actor, code=code, redirect_uri=redirects.redirect_uri)
    except DomainError as failure:
        return redirects.back(error=failure.code)
    return redirects.back()


@router.get("/logins")
def logins(
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsLoginOut]:
    """Os logins do Google conectados que a pessoa vê, sem o token."""
    return service.logins(actor)


@router.delete("/logins/{login_id}", status_code=status.HTTP_204_NO_CONTENT)
def disconnect(
    login_id: uuid.UUID,
    actor: Actor = Depends(require_session(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> None:
    """Desconecta o login: a sincronia para, o Avant revoga o acesso e os números ficam."""
    service.disconnect(actor, login_id)


@router.get("/accounts")
def accounts(
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsAccountOut]:
    """As contas do Google Ads que a pessoa vê, com quem usa, o sufixo e o gasto do mês."""
    return service.accounts(actor)


@router.put("/accounts/{account_id}")
def update_account(
    account_id: uuid.UUID,
    body: GoogleAdsAccountIn,
    actor: Actor = Depends(require(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> GoogleAdsAccountOut:
    """Troca o site, quem usa e os limites da conta."""
    return service.update_account(actor, account_id, body)


@router.post("/accounts/{account_id}/suffix")
def apply_suffix(
    account_id: uuid.UUID,
    actor: Actor = Depends(require_session(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> GoogleAdsAccountOut:
    """Grava o sufixo de URL do Avant na conta; recusa com ``google_ads_suffix_taken`` se a
    conta já tem outro sufixo ou um modelo de acompanhamento."""
    return service.apply_suffix(actor, account_id)


@router.get("/people")
def people(
    actor: Actor = Depends(require(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsPersonOut]:
    """As pessoas da Empresa com as contas que usam e os limites no Google Ads."""
    return service.people(actor)


@router.put("/people/{user_id}")
def set_person(
    user_id: uuid.UUID,
    body: GoogleAdsPersonIn,
    actor: Actor = Depends(require(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> GoogleAdsPersonOut:
    """Passa as contas para a pessoa (tira de quem usava) e grava os limites dela."""
    return service.set_person(actor, user_id, body)


@router.get("/objects")
def objects(
    filters: GoogleAdsObjectFilter = Depends(object_filter),
    dates: tuple[date, date] = Depends(period),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> PageOut[GoogleAdsObjectOut]:
    """Uma página das campanhas, grupos ou anúncios, com gasto, receita, lucro e ROI."""
    return service.objects(actor, filters, dates[0], dates[1], page)


@router.get("/objects/{level}/{external_id}")
def show_object(
    level: GoogleAdsLevel,
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> GoogleAdsObjectDetailOut:
    """Uma campanha, grupo ou anúncio com os números por dia."""
    return service.object(actor, level, external_id, dates[0], dates[1])


@router.get("/objects/{level}/{external_id}/search-terms")
def search_terms(
    level: GoogleAdsLevel,
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsTermOut]:
    """Os termos de pesquisa da campanha ou do grupo, com gasto e a palavra-chave que casou."""
    return service.search_terms(actor, level, external_id, dates[0], dates[1])


@router.get("/objects/{level}/{external_id}/placements")
def placements(
    level: GoogleAdsLevel,
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsTermOut]:
    """Os posicionamentos (sites, apps e vídeos) da campanha ou do grupo, com gasto."""
    return service.placements(actor, level, external_id, dates[0], dates[1])


@router.get("/ad-groups/{external_id}/keywords")
def keywords(
    external_id: str,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsKeywordOut]:
    """As palavras-chave do grupo com gasto, receita (pela ``utm_keyword``), lucro e ROI."""
    return service.keywords(actor, external_id, dates[0], dates[1])


@router.get("/changes")
def changes(
    page: int = Query(default=1, ge=1),
    account_id: uuid.UUID | None = Query(default=None),
    object_id: str | None = Query(default=None, max_length=40),
    origin: GoogleAdsChangeOrigin | None = Query(default=None),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> PageOut[GoogleAdsChangeOut]:
    """Uma página do histórico: quem mudou o quê, no Avant ou direto no Google Ads."""
    return service.changes(actor, page, account_id, object_id, origin)


@router.get("/alerts")
def alerts(
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> PageOut[GoogleAdsAlertOut]:
    """Uma página dos avisos da pessoa, o mais novo primeiro."""
    return service.alerts(actor, page)


@router.post("/alerts/{alert_id}/read", status_code=status.HTTP_204_NO_CONTENT)
def read_alert(
    alert_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> None:
    """Marca o aviso como lido."""
    service.read_alert(actor, alert_id)


@router.get("/alert-settings")
def alert_settings(
    actor: Actor = Depends(require(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsAlertSettingOut]:
    """Quem recebe cada tipo de aviso e se vai por e-mail."""
    return service.alert_settings(actor)


@router.put("/alert-settings")
def set_alert_settings(
    body: list[GoogleAdsAlertSettingOut],
    actor: Actor = Depends(require(ACCOUNTS)),
    service: GoogleAdsService = Depends(google_ads_service),
) -> list[GoogleAdsAlertSettingOut]:
    """Grava quem recebe os tipos de aviso enviados; os outros ficam como estavam."""
    return service.set_alert_settings(actor, body)
