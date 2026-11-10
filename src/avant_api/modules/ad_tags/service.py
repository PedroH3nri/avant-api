"""Service das ad tags do painel do cliente: chama os casos de uso e limpa o cache da tag."""

import uuid

from avant_core.access.models import Actor
from avant_core.ad_tags.services import (
    create_ad_tag,
    delete_ad_tag,
    get_ad_tag,
    get_ad_tag_health,
    list_ad_tag_units,
    list_ad_tag_versions,
    page_ad_tags,
    publish_ad_tag,
    restore_ad_tag_version,
    set_ad_tag_active,
    update_ad_tag,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.app.reward_cache import RewardCache
from avant_api.modules.ad_tags.cache import forget_tag
from avant_api.modules.ad_tags.dto import (
    AdTagCreateIn,
    AdTagHealthOut,
    AdTagIn,
    AdTagOut,
    AdTagUnitDayOut,
    AdTagVersionOut,
)
from avant_api.shared.dto import PageOut, page_out


class AdTagService:
    """Ad tags da Empresa ativa, com o RLS dela."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, cache: RewardCache) -> None:
        self._uows = uows
        self._clock = clock
        self._cache = cache

    def page(
        self, actor: Actor, page: int, site_id: uuid.UUID | None, query: str | None
    ) -> PageOut[AdTagOut]:
        """Uma página das ad tags, a mais nova primeiro."""
        found = page_ad_tags(
            self._uows.uow(actor.company_id), actor=actor, page=page, site_id=site_id, query=query
        )
        return page_out(found, AdTagOut.of)

    def get(self, actor: Actor, ad_tag_id: uuid.UUID) -> AdTagOut:
        """Uma ad tag com o rascunho e a versão no ar."""
        return AdTagOut.of(
            get_ad_tag(self._uows.uow(actor.company_id), actor=actor, ad_tag_id=ad_tag_id)
        )

    def create(self, actor: Actor, body: AdTagCreateIn) -> AdTagOut:
        """Cria uma ad tag vazia no site."""
        created = create_ad_tag(
            self._uows.uow(actor.company_id),
            actor=actor,
            site_id=body.site_id,
            name=body.name,
            clock=self._clock,
        )
        return AdTagOut.of(created)

    def update(self, actor: Actor, ad_tag_id: uuid.UUID, body: AdTagIn) -> AdTagOut:
        """Guarda o nome e o rascunho, sem publicar."""
        changed = update_ad_tag(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_tag_id=ad_tag_id,
            name=body.name,
            draft=body.draft.to_core(),
            clock=self._clock,
        )
        return AdTagOut.of(changed)

    def publish(self, actor: Actor, ad_tag_id: uuid.UUID, note: str | None) -> AdTagOut:
        """Publica o rascunho e limpa o cache da tag."""
        published = publish_ad_tag(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_tag_id=ad_tag_id,
            note=note,
            clock=self._clock,
        )
        forget_tag(self._cache, published.tag.key)
        return AdTagOut.of(published)

    def health(self, actor: Actor, ad_tag_id: uuid.UUID, days: int) -> AdTagHealthOut:
        """A saúde da tag nos últimos dias."""
        found = get_ad_tag_health(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_tag_id=ad_tag_id,
            clock=self._clock,
            days=days,
        )
        return AdTagHealthOut.of(found)

    def versions(self, actor: Actor, ad_tag_id: uuid.UUID) -> list[AdTagVersionOut]:
        """As versões publicadas, a mais nova primeiro."""
        found = list_ad_tag_versions(
            self._uows.uow(actor.company_id), actor=actor, ad_tag_id=ad_tag_id
        )
        return [AdTagVersionOut.of(version) for version in found]

    def restore(self, actor: Actor, ad_tag_id: uuid.UUID, number: int) -> AdTagOut:
        """Volta para uma versão antiga e limpa o cache da tag."""
        restored = restore_ad_tag_version(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_tag_id=ad_tag_id,
            number=number,
            clock=self._clock,
        )
        forget_tag(self._cache, restored.tag.key)
        return AdTagOut.of(restored)

    def set_active(self, actor: Actor, ad_tag_id: uuid.UUID, active: bool) -> AdTagOut:
        """Pausa ou ativa e limpa o cache da tag."""
        changed = set_ad_tag_active(
            self._uows.uow(actor.company_id),
            actor=actor,
            ad_tag_id=ad_tag_id,
            active=active,
            clock=self._clock,
        )
        forget_tag(self._cache, changed.tag.key)
        return AdTagOut.of(changed)

    def delete(self, actor: Actor, ad_tag_id: uuid.UUID) -> None:
        """Apaga a tag e limpa o cache dela."""
        deleted = delete_ad_tag(
            self._uows.uow(actor.company_id), actor=actor, ad_tag_id=ad_tag_id, clock=self._clock
        )
        forget_tag(self._cache, deleted.key)

    def units(self, actor: Actor, site_id: uuid.UUID) -> list[AdTagUnitDayOut]:
        """Os dias com blocos de ad tag no site, o mais recente primeiro."""
        days = list_ad_tag_units(self._uows.uow(actor.company_id), actor=actor, site_id=site_id)
        return [AdTagUnitDayOut.of(day) for day in days]
