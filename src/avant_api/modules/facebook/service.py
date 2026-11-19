"""Service do Facebook do painel do cliente: chama os casos de uso com o RLS da Empresa."""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.facebook.enums import FacebookChangeOrigin
from avant_core.facebook.interfaces import FacebookGateway
from avant_core.facebook.models import FacebookObjectFilter
from avant_core.facebook.services import (
    connect_facebook_profile,
    disconnect_facebook_profile,
    facebook_alert_settings,
    get_facebook_object,
    get_facebook_rule,
    list_facebook_accounts,
    list_facebook_people,
    list_facebook_profiles,
    mark_facebook_alert_read,
    page_facebook_alerts,
    page_facebook_changes,
    page_facebook_objects,
    page_facebook_rule_decisions,
    set_facebook_alert_settings,
    set_facebook_budget,
    set_facebook_person,
    set_facebook_rule,
    set_facebook_status,
    update_facebook_account,
)
from avant_core.ports import SecretBox
from avant_core.shared.clock import Clock

from avant_api.app.errors import FacebookNotConfigured
from avant_api.app.ports import UnitOfWorkFactory
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
    micros,
)
from avant_api.shared.dto import PageOut, page_out


class FacebookService:
    """Perfis, contas, pessoas, campanhas, histórico e avisos da Empresa ativa."""

    def __init__(
        self,
        uows: UnitOfWorkFactory,
        clock: Clock,
        gateway: FacebookGateway | None,
        box: SecretBox | None,
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._gateway = gateway
        self._box = box

    def ensure_available(self) -> None:
        """Recusa com ``facebook_not_configured`` quando a API não tem o app da Meta."""
        self._adapters()

    def connect(self, actor: Actor, *, code: str, redirect_uri: str) -> None:
        """Troca o código do login pelo token, grava o perfil e traz as contas dele."""
        gateway, box = self._adapters()
        connect_facebook_profile(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            code=code,
            redirect_uri=redirect_uri,
            clock=self._clock,
        )

    def profiles(self, actor: Actor) -> list[FacebookProfileOut]:
        """Os perfis que a pessoa vê."""
        found = list_facebook_profiles(self._uows.uow(actor.company_id), actor=actor)
        return [FacebookProfileOut.of(view) for view in found]

    def disconnect(self, actor: Actor, profile_id: uuid.UUID) -> None:
        """Desconecta o perfil e revoga as permissões dele no Facebook."""
        gateway, box = self._adapters()
        disconnect_facebook_profile(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            profile_id=profile_id,
            clock=self._clock,
        )

    def accounts(self, actor: Actor) -> list[FacebookAccountOut]:
        """As contas que a pessoa vê, com quem usa e o gasto do mês."""
        found = list_facebook_accounts(
            self._uows.uow(actor.company_id), actor=actor, clock=self._clock
        )
        return [FacebookAccountOut.of(view) for view in found]

    def update_account(
        self, actor: Actor, account_id: uuid.UUID, body: FacebookAccountIn
    ) -> FacebookAccountOut:
        """Troca o site, quem usa e os limites da conta."""
        update_facebook_account(
            self._uows.uow(actor.company_id),
            actor=actor,
            account_id=account_id,
            data=body.to_core(),
            clock=self._clock,
        )
        return next(item for item in self.accounts(actor) if item.id == account_id)

    def people(self, actor: Actor) -> list[FacebookPersonOut]:
        """As pessoas da Empresa com as contas que usam e os limites."""
        found = list_facebook_people(self._uows.uow(actor.company_id), actor=actor)
        return [FacebookPersonOut.of(view) for view in found]

    def set_person(
        self, actor: Actor, user_id: uuid.UUID, body: FacebookPersonIn
    ) -> FacebookPersonOut:
        """Passa as contas para a pessoa (tirando de quem usava) e grava os limites dela."""
        view = set_facebook_person(
            self._uows.uow(actor.company_id),
            actor=actor,
            user_id=user_id,
            account_ids=body.account_ids,
            daily_limit_micros=micros(body.daily_limit),
            monthly_limit_micros=micros(body.monthly_limit),
            clock=self._clock,
        )
        return FacebookPersonOut.of(view)

    def objects(
        self, actor: Actor, filters: FacebookObjectFilter, start: date, end: date, page: int
    ) -> PageOut[FacebookObjectOut]:
        """Uma página das campanhas, conjuntos ou anúncios com os números do período."""
        found = page_facebook_objects(
            self._uows.uow(actor.company_id),
            actor=actor,
            filters=filters,
            start=start,
            end=end,
            page=page,
        )
        return page_out(found, FacebookObjectOut.of)

    def object(
        self, actor: Actor, external_id: str, start: date, end: date
    ) -> FacebookObjectDetailOut:
        """Uma campanha, conjunto ou anúncio com os números por dia e por país."""
        found = get_facebook_object(
            self._uows.uow(actor.company_id),
            actor=actor,
            external_id=external_id,
            start=start,
            end=end,
        )
        return FacebookObjectDetailOut.detail(found)

    def changes(
        self,
        actor: Actor,
        page: int,
        account_id: uuid.UUID | None,
        object_external_id: str | None,
        origin: FacebookChangeOrigin | None,
    ) -> PageOut[FacebookChangeOut]:
        """Uma página do histórico, o mais novo primeiro."""
        found = page_facebook_changes(
            self._uows.uow(actor.company_id),
            actor=actor,
            page=page,
            account_id=account_id,
            object_external_id=object_external_id,
            origin=origin,
        )
        return page_out(found, FacebookChangeOut.of)

    def alerts(self, actor: Actor, page: int) -> PageOut[FacebookAlertOut]:
        """Uma página dos avisos da pessoa, o mais novo primeiro."""
        found = page_facebook_alerts(self._uows.uow(actor.company_id), actor=actor, page=page)
        return page_out(found, FacebookAlertOut.of)

    def read_alert(self, actor: Actor, alert_id: uuid.UUID) -> None:
        """Marca o aviso como lido para a pessoa."""
        mark_facebook_alert_read(
            self._uows.uow(actor.company_id), actor=actor, alert_id=alert_id, clock=self._clock
        )

    def alert_settings(self, actor: Actor) -> list[FacebookAlertSettingOut]:
        """Quem recebe cada tipo de aviso."""
        found = facebook_alert_settings(self._uows.uow(actor.company_id), actor=actor)
        return [FacebookAlertSettingOut.of(setting) for setting in found]

    def set_alert_settings(
        self, actor: Actor, body: list[FacebookAlertSettingOut]
    ) -> list[FacebookAlertSettingOut]:
        """Grava quem recebe os tipos de aviso enviados."""
        found = set_facebook_alert_settings(
            self._uows.uow(actor.company_id),
            actor=actor,
            settings=[setting.to_core(actor.company_id) for setting in body],
            clock=self._clock,
        )
        return [FacebookAlertSettingOut.of(setting) for setting in found]

    def set_status(self, actor: Actor, body: FacebookStatusIn) -> FacebookControlOut:
        """Liga ou pausa os objetos no Facebook, conferindo os limites antes de ligar."""
        gateway, box = self._adapters()
        result = set_facebook_status(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            external_ids=body.external_ids,
            active=body.active,
            clock=self._clock,
        )
        return FacebookControlOut.of(result)

    def set_budget(
        self, actor: Actor, external_id: str, body: FacebookBudgetIn
    ) -> FacebookBudgetOut:
        """Troca o orçamento diário ou o vitalício, conferindo o limite diário."""
        gateway, box = self._adapters()
        item = set_facebook_budget(
            self._uows.uow(actor.company_id),
            actor=actor,
            gateway=gateway,
            box=box,
            external_id=external_id,
            daily_budget_micros=micros(body.daily_budget),
            lifetime_budget_micros=micros(body.lifetime_budget),
            clock=self._clock,
        )
        return FacebookBudgetOut.of(item)

    def rule(self, actor: Actor, external_id: str) -> FacebookRuleOut:
        """As regras automáticas do objeto (as sugeridas, desligadas, quando não há)."""
        found = get_facebook_rule(
            self._uows.uow(actor.company_id), actor=actor, external_id=external_id
        )
        return FacebookRuleOut.of(found)

    def set_rule(self, actor: Actor, external_id: str, body: FacebookRuleIn) -> FacebookRuleOut:
        """Grava as regras automáticas do objeto."""
        found = set_facebook_rule(
            self._uows.uow(actor.company_id),
            actor=actor,
            external_id=external_id,
            data=body.to_core(),
            clock=self._clock,
        )
        return FacebookRuleOut.of(found)

    def rule_decisions(
        self, actor: Actor, external_id: str, page: int
    ) -> PageOut[FacebookRuleDecisionOut]:
        """Uma página das decisões das regras do objeto, a mais nova primeiro."""
        found = page_facebook_rule_decisions(
            self._uows.uow(actor.company_id), actor=actor, external_id=external_id, page=page
        )
        return page_out(found, FacebookRuleDecisionOut.of)

    def _adapters(self) -> tuple[FacebookGateway, SecretBox]:
        """A Graph API e a cifra dos tokens, ou recusa quando não estão configuradas."""
        if self._gateway is None or self._box is None:
            raise FacebookNotConfigured("integração com o Facebook não configurada")
        return self._gateway, self._box
