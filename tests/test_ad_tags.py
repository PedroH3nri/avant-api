"""Ad tags e loaders no painel do cliente, no interno e na rota pública contra o Postgres:
rascunho, publicar, versões, cache por chave, loader em uso e os casos sem permissão."""

import json
import uuid
from datetime import UTC, date, datetime

from avant_core.ad_tags.enums import AdTagDevice
from avant_core.ad_tags.models import AdTagHealthDay
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import AdUnit, Site
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.ad_tag_cache import ad_tag_cache_key
from avant_api.app.container import Services
from avant_api.app.reward_buffer import MemoryRewardBuffer
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_rewards import _cache
from tests.test_team import _member_client

NOW = datetime(2026, 11, 10, 12, tzinfo=UTC)
CONTENT = {"kind": "content", "number": 3, "selector": "article p", "side": "after"}


def _page_views(client: TestClient) -> MemoryRewardBuffer:
    """O buffer em memória das páginas vistas da aplicação de teste."""
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    assert isinstance(services.page_views, MemoryRewardBuffer)
    return services.page_views


def _site(engine: Engine, company_id: uuid.UUID) -> uuid.UUID:
    """O site blog.com com o bloco pai e os blocos de ad tag de um dia."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "2100", ConnectionType.MCM, NOW)
        uow.networks.add(network)
        site = Site(company_id, "blog.com", network.id, "s1", NOW, "APPROVED")
        uow.sites.add(site)
        parent = AdUnit(company_id, network.id, "u1", "blog.com", NOW, site_id=site.id)
        uow.ad_units.add(parent)
        for number, name in enumerate(("Blog_Content3_20261028", "Blog_Anchor_Mobile_20261028")):
            uow.ad_units.add(
                AdUnit(
                    company_id,
                    network.id,
                    f"t{number}",
                    name,
                    NOW,
                    ad_unit_code=name,
                    parent_id=parent.id,
                    site_id=site.id,
                )
            )
        uow.commit()
        return site.id


def test_ad_tags_and_loaders_panel(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    site_id = _site(engine, uuid.UUID(me["active_company_id"]))
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get("/api/v1/ad-tags").status_code == 403
    assert ana.get("/api/v1/loaders").status_code == 403
    denied = ana.post(
        "/api/v1/ad-tags", json={"site_id": str(site_id), "name": "X"}, headers=_csrf(ana)
    )
    assert denied.status_code == 403

    units = client.get(f"/api/v1/sites/{site_id}/ad-tag-units").json()
    assert units == [
        {
            "day": "2026-10-28",
            "units": [
                {"unit_type": "Content3", "desktop": True, "mobile": True},
                {"unit_type": "Anchor", "desktop": False, "mobile": True},
            ],
        }
    ]
    loader = client.post(
        "/api/v1/loaders",
        json={"name": "Padrão", "background": "#FFFFFF", "adblock": "block"},
        headers=_csrf(client),
    )
    assert loader.status_code == 201, loader.text
    loader_id = loader.json()["id"]
    assert loader.json()["background"] == "#ffffff" and loader.json()["tags"] == []
    taken = client.post("/api/v1/loaders", json={"name": "padrão"}, headers=_csrf(client))
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "loader_name_taken"
    assert [item["name"] for item in client.get("/api/v1/loaders/options").json()] == ["Padrão"]

    created = client.post(
        "/api/v1/ad-tags",
        json={"site_id": str(site_id), "name": "Principal"},
        headers=_csrf(client),
    )
    assert created.status_code == 201, created.text
    tag = created.json()
    tag_id, key = tag["id"], tag["key"]
    assert key.startswith("tg_") and tag["live"] is None and tag["has_changes"] is True
    draft = {"blocks": [CONTENT], "settings": {"loader_id": loader_id, "reward": True}}
    saved = client.put(
        f"/api/v1/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": draft},
        headers=_csrf(client),
    )
    assert saved.status_code == 200, saved.text
    assert saved.json()["draft"]["blocks"][0]["selector"] == "article p"
    anchor = {"kind": "anchor", "edge": "bottom"}
    with_anchor = {**draft, "blocks": [CONTENT, anchor]}
    client.put(
        f"/api/v1/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": with_anchor},
        headers=_csrf(client),
    )
    missing = client.post(f"/api/v1/ad-tags/{tag_id}/publish", json={}, headers=_csrf(client))
    assert missing.status_code == 422 and missing.json()["error"]["code"] == "ad_tag_unit_missing"
    client.put(
        f"/api/v1/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": draft},
        headers=_csrf(client),
    )
    visitor = TestClient(client.app)
    page = {"key": key, "url": "https://www.blog.com/receitas"}
    assert visitor.get("/api/tag/config", params=page).json() == {"tag": None}
    assert _cache(client).values[ad_tag_cache_key(key)] == "{}"
    published = client.post(
        f"/api/v1/ad-tags/{tag_id}/publish", json={"note": "primeira"}, headers=_csrf(client)
    )
    assert published.status_code == 200, published.text
    assert published.json()["live"]["number"] == 1 and published.json()["has_changes"] is False
    assert ad_tag_cache_key(key) not in _cache(client).values
    config = visitor.get("/api/tag/config", params=page)
    assert config.headers["access-control-allow-origin"] == "*"
    body = config.json()["tag"]
    assert body["version"] == 1 and body["reward"] is True
    assert body["loader"]["adblock"] == "block"
    assert body["blocks"][0]["desktop"] == "/2100/blog.com/Blog_Content3_20261028"
    other = visitor.get("/api/tag/config", params={"key": key, "url": "https://outro.com/"})
    assert other.json() == {"tag": None}

    edited = client.put(
        f"/api/v1/loaders/{loader_id}",
        json={"name": "Padrão", "blur": 3},
        headers=_csrf(client),
    )
    assert [item["key"] for item in edited.json()["tags"]] == [key]
    assert ad_tag_cache_key(key) not in _cache(client).values
    in_use = client.delete(f"/api/v1/loaders/{loader_id}", headers=_csrf(client))
    assert in_use.status_code == 409 and in_use.json()["error"]["code"] == "loader_in_use"

    restored = client.post(f"/api/v1/ad-tags/{tag_id}/versions/1/restore", headers=_csrf(client))
    assert restored.json()["live"]["number"] == 2
    versions = client.get(f"/api/v1/ad-tags/{tag_id}/versions").json()
    assert [(item["number"], item["live"]) for item in versions] == [(2, True), (1, False)]
    paused = client.patch(
        f"/api/v1/ad-tags/{tag_id}", json={"active": False}, headers=_csrf(client)
    )
    assert paused.json()["active"] is False
    assert visitor.get("/api/tag/config", params=page).json() == {"tag": None}
    listed = client.get("/api/v1/ad-tags", params={"q": "princ"}).json()
    assert [item["id"] for item in listed["items"]] == [tag_id]
    gone = client.delete(f"/api/v1/ad-tags/{tag_id}", headers=_csrf(client))
    assert gone.status_code == 204
    assert client.get(f"/api/v1/ad-tags/{tag_id}").status_code == 404
    assert client.delete(f"/api/v1/loaders/{loader_id}", headers=_csrf(client)).status_code == 204


def test_internal_ad_tags_and_loaders(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = me["active_company_id"]
    site_id = _site(engine, uuid.UUID(company_id))
    assert client.get("/api/v1/internal/ad-tags").status_code == 403
    staff = _staff(client, engine)
    loader = staff.post(
        "/api/v1/internal/loaders",
        json={"company_id": company_id, "name": "Da Groone"},
        headers=_csrf(staff),
    )
    assert loader.status_code == 201, loader.text
    assert loader.json()["client"]["id"] == company_id
    options = staff.get("/api/v1/internal/loaders/options", params={"company_id": company_id})
    assert [item["name"] for item in options.json()] == ["Da Groone"]
    created = staff.post(
        "/api/v1/internal/ad-tags",
        json={"site_id": str(site_id), "name": "Principal"},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    tag_id = created.json()["id"]
    draft = {"blocks": [CONTENT], "settings": {"loader_id": loader.json()["id"]}}
    staff.put(
        f"/api/v1/internal/ad-tags/{tag_id}",
        json={"name": "Principal", "draft": draft},
        headers=_csrf(staff),
    )
    published = staff.post(
        f"/api/v1/internal/ad-tags/{tag_id}/publish", json={}, headers=_csrf(staff)
    )
    assert published.status_code == 200, published.text
    listed = staff.get("/api/v1/internal/ad-tags", params={"company_id": company_id}).json()
    assert [item["client"]["id"] for item in listed["items"]] == [company_id]
    units = staff.get(f"/api/v1/internal/sites/{site_id}/ad-tag-units").json()
    assert units[0]["day"] == "2026-10-28"
    assert client.get(f"/api/v1/ad-tags/{tag_id}").json()["live"]["number"] == 1
    assert staff.get(f"/api/v1/internal/ad-tags/{tag_id}/health").json()["days"] == []
    assert client.get(f"/api/v1/internal/ad-tags/{tag_id}/health").status_code == 403


def test_page_views_go_to_the_buffer_and_health_reads_back(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    site_id = _site(engine, company_id)
    created = client.post(
        "/api/v1/ad-tags",
        json={"site_id": str(site_id), "name": "Principal"},
        headers=_csrf(client),
    )
    tag = created.json()
    visitor = TestClient(client.app)
    page = {
        "key": tag["key"],
        "url": "https://blog.com/receitas",
        "page_view_id": str(uuid.uuid4()),
        "visitor_id": str(uuid.uuid4()),
        "session_id": str(uuid.uuid4()),
        "version": 1,
        "device": "mobile",
        "language": "pt-BR",
        "referrer": None,
        "visible_ms": 1200,
        "scroll_percent": 40,
        "clicked": False,
        "adblock": False,
        "id_post": None,
        "content_hash": "abc",
        "blocks": [{"type": "Content3", "state": "rendered"}],
    }
    origin = {"Origin": "https://blog.com", "Content-Type": "text/plain"}
    sent = visitor.post("/api/tag/page-views", content=json.dumps(page), headers=origin)
    assert sent.status_code == 202
    assert sent.headers["access-control-allow-origin"] == "https://blog.com"
    stored = json.loads(_page_views(client).items[-1])
    assert stored["key"] == tag["key"] and stored["ip"] and stored["received_at"]
    assert stored["blocks"] == [{"type": "Content3", "state": "rendered"}]
    broken = visitor.post(
        "/api/tag/page-views", content=json.dumps({**page, "scroll_percent": 900}), headers=origin
    )
    assert broken.status_code == 422 and len(_page_views(client).items) == 1
    assert visitor.options("/api/tag/page-views", headers=origin).status_code == 204

    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        seen = datetime.now(UTC)
        row = AdTagHealthDay(date.today(), 1, "page", AdTagDevice.MOBILE, 3, 0, 0, seen)
        uow.ad_tag_health.add(company_id, uuid.UUID(tag["id"]), row)
        uow.commit()
    health = client.get(f"/api/v1/ad-tags/{tag['id']}/health", params={"days": 30})
    assert health.status_code == 200, health.text
    assert health.json()["seen_version"] == 1 and health.json()["days"][0]["page_views"] == 3
    assert client.get(f"/api/v1/ad-tags/{tag['id']}/health", params={"days": 91}).status_code == 422
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get(f"/api/v1/ad-tags/{tag['id']}/health").status_code == 403
