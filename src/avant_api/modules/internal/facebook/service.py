"""Service do Facebook dos clientes no painel interno (sem RLS, só leitura)."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.facebook.enums import FacebookChangeOrigin
from avant_core.facebook.models import FacebookObjectFilter
from avant_core.facebook.services import (
    internal_facebook_accounts,
    internal_get_facebook_object,
    internal_page_facebook_alerts,
    internal_page_facebook_changes,
    internal_page_facebook_objects,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.facebook.dto import (
    FacebookAccountOut,
    FacebookAlertOut,
    FacebookChangeOut,
    FacebookObjectDetailOut,
    FacebookObjectOut,
)
from avant_api.shared.dto import PageOut, page_out


class ClientFacebookService:
    """Contas, campanhas, histórico e avisos de todos os clientes; o core confere a Company
    Groone e a permissão."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def accounts(self, actor: Actor, company_id: uuid.UUID | None) -> list[FacebookAccountOut]:
        """As contas de todos os clientes, ou de um."""
        found = internal_facebook_accounts(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, company_id=company_id
        )
        return [FacebookAccountOut.of(view) for view in found]

    def objects(
        self,
        actor: Actor,
        filters: FacebookObjectFilter,
        start: date,
        end: date,
        page: int,
        company_id: uuid.UUID | None,
    ) -> PageOut[FacebookObjectOut]:
        """Uma página das campanhas, conjuntos ou anúncios dos clientes com os números."""
        found = internal_page_facebook_objects(
            self._uows.trusted_uow(),
            actor=actor,
            filters=filters,
            start=start,
            end=end,
            page=page,
            company_id=company_id,
        )
        return page_out(found, FacebookObjectOut.of)

    def object(
        self, actor: Actor, external_id: str, start: date, end: date
    ) -> FacebookObjectDetailOut:
        """Uma campanha, conjunto ou anúncio de um cliente com os números por dia e país."""
        found = internal_get_facebook_object(
            self._uows.trusted_uow(), actor=actor, external_id=external_id, start=start, end=end
        )
        return FacebookObjectDetailOut.detail(found)

    def changes(
        self,
        actor: Actor,
        page: int,
        company_id: uuid.UUID | None,
        account_id: uuid.UUID | None,
        object_external_id: str | None,
        origin: FacebookChangeOrigin | None,
    ) -> PageOut[FacebookChangeOut]:
        """Uma página do histórico dos clientes."""
        found = internal_page_facebook_changes(
            self._uows.trusted_uow(),
            actor=actor,
            page=page,
            company_id=company_id,
            account_id=account_id,
            object_external_id=object_external_id,
            origin=origin,
        )
        return page_out(found, FacebookChangeOut.of)

    def alerts(
        self, actor: Actor, page: int, company_id: uuid.UUID | None
    ) -> PageOut[FacebookAlertOut]:
        """Uma página dos avisos dos clientes."""
        found = internal_page_facebook_alerts(
            self._uows.trusted_uow(), actor=actor, page=page, company_id=company_id
        )
        return page_out(found, FacebookAlertOut.of)
