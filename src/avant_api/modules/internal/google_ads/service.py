"""Service do Google Ads dos clientes no painel interno (sem RLS, só leitura)."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.google_ads.enums import GoogleAdsChangeOrigin, GoogleAdsLevel
from avant_core.google_ads.models import GoogleAdsObjectFilter
from avant_core.google_ads.services import (
    internal_get_google_ads_object,
    internal_google_ads_accounts,
    internal_google_ads_keywords,
    internal_page_google_ads_alerts,
    internal_page_google_ads_changes,
    internal_page_google_ads_objects,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.google_ads.dto import (
    GoogleAdsAccountOut,
    GoogleAdsAlertOut,
    GoogleAdsChangeOut,
    GoogleAdsKeywordOut,
    GoogleAdsObjectDetailOut,
    GoogleAdsObjectOut,
)
from avant_api.shared.dto import PageOut, page_out


class ClientGoogleAdsService:
    """Contas, campanhas, palavras-chave, histórico e avisos de todos os clientes; o core confere
    a Company Groone e a permissão."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def accounts(self, actor: Actor, company_id: uuid.UUID | None) -> list[GoogleAdsAccountOut]:
        """As contas de todos os clientes, ou de um."""
        found = internal_google_ads_accounts(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, company_id=company_id
        )
        return [GoogleAdsAccountOut.of(view) for view in found]

    def objects(
        self,
        actor: Actor,
        filters: GoogleAdsObjectFilter,
        start: date,
        end: date,
        page: int,
        company_id: uuid.UUID | None,
    ) -> PageOut[GoogleAdsObjectOut]:
        """Uma página das campanhas, grupos ou anúncios dos clientes com os números."""
        found = internal_page_google_ads_objects(
            self._uows.trusted_uow(),
            actor=actor,
            filters=filters,
            start=start,
            end=end,
            page=page,
            company_id=company_id,
        )
        return page_out(found, GoogleAdsObjectOut.of)

    def object(
        self, actor: Actor, level: GoogleAdsLevel, external_id: str, start: date, end: date
    ) -> GoogleAdsObjectDetailOut:
        """Uma campanha, grupo ou anúncio de um cliente com os números por dia."""
        found = internal_get_google_ads_object(
            self._uows.trusted_uow(),
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
        """As palavras-chave de um grupo de um cliente com os números."""
        found = internal_google_ads_keywords(
            self._uows.trusted_uow(),
            actor=actor,
            ad_group_external_id=ad_group_external_id,
            start=start,
            end=end,
        )
        return [GoogleAdsKeywordOut.of(view) for view in found]

    def changes(
        self,
        actor: Actor,
        page: int,
        company_id: uuid.UUID | None,
        account_id: uuid.UUID | None,
        object_external_id: str | None,
        origin: GoogleAdsChangeOrigin | None,
    ) -> PageOut[GoogleAdsChangeOut]:
        """Uma página do histórico dos clientes."""
        found = internal_page_google_ads_changes(
            self._uows.trusted_uow(),
            actor=actor,
            page=page,
            company_id=company_id,
            account_id=account_id,
            object_external_id=object_external_id,
            origin=origin,
        )
        return page_out(found, GoogleAdsChangeOut.of)

    def alerts(
        self, actor: Actor, page: int, company_id: uuid.UUID | None
    ) -> PageOut[GoogleAdsAlertOut]:
        """Uma página dos avisos dos clientes."""
        found = internal_page_google_ads_alerts(
            self._uows.trusted_uow(), actor=actor, page=page, company_id=company_id
        )
        return page_out(found, GoogleAdsAlertOut.of)
