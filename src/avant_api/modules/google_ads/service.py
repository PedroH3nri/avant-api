"""Service do Google Ads do painel do cliente: chama os casos de uso com o RLS da Empresa."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.google_ads.enums import GoogleAdsChangeOrigin, GoogleAdsLevel
from avant_core.google_ads.interfaces import GoogleAdsGateway
from avant_core.google_ads.models import GoogleAdsObjectFilter
from avant_core.google_ads.services import (
    apply_google_ads_suffix,
    connect_google_ads_login,
    disconnect_google_ads_login,
    get_google_ads_object,
    google_ads_alert_settings,
    list_google_ads_accounts,
    list_google_ads_keywords,
    list_google_ads_logins,
    list_google_ads_people,
    list_google_ads_placements,
    list_google_ads_search_terms,
    mark_google_ads_alert_read,
    page_google_ads_alerts,
    page_google_ads_changes,
    page_google_ads_objects,
    set_google_ads_alert_settings,
    set_google_ads_person,
    update_google_ads_account,
)
from avant_core.ports import SecretBox
from avant_core.shared.clock import Clock

from avant_api.app.errors import GoogleAdsNotConfigured
from avant_api.app.ports import UnitOfWorkFactory
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
from avant_api.shared.ads import micros
from avant_api.shared.dto import PageOut, page_out


class GoogleAdsService:
    """Logins, contas, pessoas, campanhas, palavras-chave, histórico e avisos da Empresa ativa."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        gateway: GoogleAdsGateway | None,
        box: SecretBox | None,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._gateway = gateway
        self._box = box

    def ensure_available(self) -> None:
        """Recusa com ``google_ads_not_configured`` quando a API não tem o cliente do Google."""
        self._adapters()

    def connect(self, actor: Actor, *, code: str, redirect_uri: str) -> None:
        """Troca o código do login pelo token, grava o login e traz as contas dele."""
        gateway, box = self._adapters()
        connect_google_ads_login(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            code=code,
            redirect_uri=redirect_uri,
            clock=self._clock,
        )

    def logins(self, actor: Actor) -> list[GoogleAdsLoginOut]:
        """Os logins que a pessoa vê."""
        found = list_google_ads_logins(self._uows.uow(actor.company_id), actor=actor)
        return [GoogleAdsLoginOut.of(view) for view in found]

    def disconnect(self, actor: Actor, login_id: uuid.UUID) -> None:
        """Desconecta o login e revoga o acesso dele no Google."""
        gateway, box = self._adapters()
        disconnect_google_ads_login(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            login_id=login_id,
            clock=self._clock,
        )

    def accounts(self, actor: Actor) -> list[GoogleAdsAccountOut]:
        """As contas que a pessoa vê, com quem usa e o gasto do mês."""
        found = list_google_ads_accounts(
            self._uows.uow(actor.company_id), actor=actor, clock=self._clock
        )
        return [GoogleAdsAccountOut.of(view) for view in found]

    def update_account(
        self, actor: Actor, account_id: uuid.UUID, body: GoogleAdsAccountIn
    ) -> GoogleAdsAccountOut:
        """Troca o site, quem usa e os limites da conta."""
        update_google_ads_account(
            self._uows.uow(actor.company_id),
            actor=actor,
            account_id=account_id,
            data=body.to_core(),
            clock=self._clock,
        )
        return self._account(actor, account_id)

    def apply_suffix(self, actor: Actor, account_id: uuid.UUID) -> GoogleAdsAccountOut:
        """Grava o sufixo de URL do Avant na conta do Google Ads, se ela não tem outro."""
        gateway, box = self._adapters()
        apply_google_ads_suffix(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            account_id=account_id,
            clock=self._clock,
        )
        return self._account(actor, account_id)

    def people(self, actor: Actor) -> list[GoogleAdsPersonOut]:
        """As pessoas da Empresa com as contas que usam e os limites."""
        found = list_google_ads_people(self._uows.uow(actor.company_id), actor=actor)
        return [GoogleAdsPersonOut.of(view) for view in found]

    def set_person(
        self, actor: Actor, user_id: uuid.UUID, body: GoogleAdsPersonIn
    ) -> GoogleAdsPersonOut:
        """Passa as contas para a pessoa (tirando de quem usava) e grava os limites dela."""
        view = set_google_ads_person(
            self._uows.uow(actor.company_id),
            actor=actor,
            user_id=user_id,
            account_ids=body.account_ids,
            daily_limit_micros=micros(body.daily_limit),
            monthly_limit_micros=micros(body.monthly_limit),
            clock=self._clock,
        )
        return GoogleAdsPersonOut.of(view)

    def objects(
        self, actor: Actor, filters: GoogleAdsObjectFilter, start: date, end: date, page: int
    ) -> PageOut[GoogleAdsObjectOut]:
        """Uma página das campanhas, grupos ou anúncios com os números do período."""
        found = page_google_ads_objects(
            self._uows.uow(actor.company_id),
            actor=actor,
            filters=filters,
            start=start,
            end=end,
            page=page,
        )
        return page_out(found, GoogleAdsObjectOut.of)

    def object(
        self, actor: Actor, level: GoogleAdsLevel, external_id: str, start: date, end: date
    ) -> GoogleAdsObjectDetailOut:
        """Uma campanha, grupo ou anúncio com os números por dia."""
        found = get_google_ads_object(
            self._uows.uow(actor.company_id),
            actor=actor,
            level=level,
            external_id=external_id,
            start=start,
            end=end,
        )
        return GoogleAdsObjectDetailOut.detail(found)

    def keywords(
        self, actor: Actor, ad_group_external_id: str, start: date, end: date
    ) -> list[GoogleAdsKeywordOut]:
        """As palavras-chave do grupo com os números e a receita."""
        found = list_google_ads_keywords(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_group_external_id=ad_group_external_id,
            start=start,
            end=end,
        )
        return [GoogleAdsKeywordOut.of(view) for view in found]

    def search_terms(
        self, actor: Actor, level: GoogleAdsLevel, external_id: str, start: date, end: date
    ) -> list[GoogleAdsTermOut]:
        """Os termos de pesquisa da campanha ou do grupo, os de mais gasto primeiro."""
        found = list_google_ads_search_terms(
            self._uows.uow(actor.company_id),
            actor=actor,
            level=level,
            external_id=external_id,
            start=start,
            end=end,
        )
        return [GoogleAdsTermOut.of(row) for row in found]

    def placements(
        self, actor: Actor, level: GoogleAdsLevel, external_id: str, start: date, end: date
    ) -> list[GoogleAdsTermOut]:
        """Os posicionamentos da campanha ou do grupo, os de mais gasto primeiro."""
        found = list_google_ads_placements(
            self._uows.uow(actor.company_id),
            actor=actor,
            level=level,
            external_id=external_id,
            start=start,
            end=end,
        )
        return [GoogleAdsTermOut.of(row) for row in found]

    def changes(
        self,
        actor: Actor,
        page: int,
        account_id: uuid.UUID | None,
        object_external_id: str | None,
        origin: GoogleAdsChangeOrigin | None,
    ) -> PageOut[GoogleAdsChangeOut]:
        """Uma página do histórico, o mais novo primeiro."""
        found = page_google_ads_changes(
            self._uows.uow(actor.company_id),
            actor=actor,
            page=page,
            account_id=account_id,
            object_external_id=object_external_id,
            origin=origin,
        )
        return page_out(found, GoogleAdsChangeOut.of)

    def alerts(self, actor: Actor, page: int) -> PageOut[GoogleAdsAlertOut]:
        """Uma página dos avisos da pessoa, o mais novo primeiro."""
        found = page_google_ads_alerts(self._uows.uow(actor.company_id), actor=actor, page=page)
        return page_out(found, GoogleAdsAlertOut.of)

    def read_alert(self, actor: Actor, alert_id: uuid.UUID) -> None:
        """Marca o aviso como lido para a pessoa."""
        mark_google_ads_alert_read(
            self._uows.uow(actor.company_id), actor=actor, alert_id=alert_id, clock=self._clock
        )

    def alert_settings(self, actor: Actor) -> list[GoogleAdsAlertSettingOut]:
        """Quem recebe cada tipo de aviso."""
        found = google_ads_alert_settings(self._uows.uow(actor.company_id), actor=actor)
        return [GoogleAdsAlertSettingOut.of(setting) for setting in found]

    def set_alert_settings(
        self, actor: Actor, body: list[GoogleAdsAlertSettingOut]
    ) -> list[GoogleAdsAlertSettingOut]:
        """Grava quem recebe os tipos de aviso enviados."""
        found = set_google_ads_alert_settings(
            self._uows.uow(actor.company_id),
            actor=actor,
            settings=[setting.to_core(actor.company_id) for setting in body],
            clock=self._clock,
        )
        return [GoogleAdsAlertSettingOut.of(setting) for setting in found]

    def _account(self, actor: Actor, account_id: uuid.UUID) -> GoogleAdsAccountOut:
        """A conta como a lista mostra, depois de uma mudança."""
        return next(item for item in self.accounts(actor) if item.id == account_id)

    def _adapters(self) -> tuple[GoogleAdsGateway, SecretBox]:
        """A API do Google Ads e a cifra dos tokens, ou recusa quando não estão configuradas."""
        if self._gateway is None or self._box is None:
            raise GoogleAdsNotConfigured("integração com o Google Ads não configurada")
        return self._gateway, self._box
