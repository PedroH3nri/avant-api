"""Rewards no painel do cliente e no interno contra o Postgres: CRUD, ícone, ad units, métricas,
contatos, cache das páginas e os casos sem permissão."""

import uuid
from datetime import UTC, date, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import AdUnit, Site
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from avant_core.rewards.enums import RewardEventKind
from avant_core.rewards.models import RewardBatch, RewardEvent, RewardLeadSubmission
from avant_core.rewards.services import record_reward_batch
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.container import Services
from avant_api.app.reward_cache import MemoryRewardCache, reward_cache_key
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_company_image import _png
from tests.test_internal import _staff
from tests.test_team import _member_client

NOW = datetime(2026, 11, 9, 12, tzinfo=UTC)


def _site(engine: Engine, company_id: uuid.UUID) -> uuid.UUID:
    """O site blog.com com o bloco pai e dois grupos de ad units de reward."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "2100", ConnectionType.MCM, NOW)
        uow.networks.add(network)
        site = Site(company_id, "blog.com", network.id, "s1", NOW, "APPROVED")
        uow.sites.add(site)
        parent = AdUnit(company_id, network.id, "u1", "blog.com", NOW, site_id=site.id)
        uow.ad_units.add(parent)
        for number, name in enumerate(
            (
                "Blog_Rewards_20260302",
                "Blog_Rewards_Desktop_20261028",
                "Blog_Rewards_Mobile_20261028",
            )
        ):
            uow.ad_units.add(
                AdUnit(
                    company_id,
                    network.id,
                    f"r{number}",
                    name,
                    NOW,
                    ad_unit_code=name,
                    parent_id=parent.id,
                    site_id=site.id,
                )
            )
        uow.commit()
        return site.id


def _body(site_id: uuid.UUID, **changes: object) -> dict[str, object]:
    """O formulário de um reward com uma pergunta e o pedido de e-mail."""
    body: dict[str, object] = {
        "site_id": str(site_id),
        "name": "Receita do bolo",
        "page_path": "https://blog.com/receitas/bolo/",
        "title": "Libere a receita",
        "button_text": "Ver anúncio",
        "style": {"layout": "header", "button_color": "#EA580C"},
        "questions": [{"title": "Qual bolo?", "answers": ["Cenoura", "Chocolate", "Fubá"]}],
        "lead": {"kind": "email", "position": "end", "title": "Seu e-mail", "button": "Ok"},
    }
    return {**body, **changes}


def _cache(client: TestClient) -> MemoryRewardCache:
    """O cache em memória da aplicação de teste."""
    services: Services = client.app.state.services  # type: ignore[attr-defined]
    assert isinstance(services.rewards, MemoryRewardCache)
    return services.rewards


def test_rewards_panel(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    site_id = _site(engine, company_id)
    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get("/api/v1/rewards").status_code == 403
    denied = ana.post("/api/v1/rewards", json=_body(site_id), headers=_csrf(ana))
    assert denied.status_code == 403

    groups = client.get(f"/api/v1/sites/{site_id}/reward-ad-units").json()
    assert [(group["day"], group["desktop"], group["mobile"]) for group in groups] == [
        ("2026-10-28", True, True),
        ("2026-03-02", True, True),
    ]
    key = reward_cache_key("blog.com", "receitas/bolo")
    _cache(client).values[key] = ""
    created = client.post("/api/v1/rewards", json=_body(site_id), headers=_csrf(client))
    assert created.status_code == 201, created.text
    reward = created.json()
    assert reward["page_path"] == "receitas/bolo" and reward["domain"] == "blog.com"
    assert reward["style"]["button_color"] == "#ea580c" and reward["client"] is None
    assert key not in _cache(client).values
    taken = client.post("/api/v1/rewards", json=_body(site_id), headers=_csrf(client))
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "reward_page_taken"
    missing = client.post(
        "/api/v1/rewards",
        json=_body(site_id, page_path="outra", ad_unit_day="2026-01-01"),
        headers=_csrf(client),
    )
    assert missing.json()["error"]["code"] == "reward_ad_unit_day_missing"
    invalid = client.post(
        "/api/v1/rewards",
        json=_body(site_id, page_path="outra", cooldown_minutes=1),
        headers=_csrf(client),
    )
    assert invalid.status_code == 422

    reward_id = reward["id"]
    _cache(client).values[key] = "{}"
    moved = client.put(
        f"/api/v1/rewards/{reward_id}",
        json=_body(site_id, page_path="receitas/torta"),
        headers=_csrf(client),
    )
    assert moved.status_code == 200 and moved.json()["page_path"] == "receitas/torta"
    question = moved.json()["questions"][0]
    kept = client.put(
        f"/api/v1/rewards/{reward_id}",
        json=_body(
            site_id,
            page_path="receitas/torta",
            questions=[{**question, "title": "Qual torta?"}],
        ),
        headers=_csrf(client),
    )
    assert kept.json()["questions"][0]["id"] == question["id"]
    assert kept.json()["questions"][0]["title"] == "Qual torta?"
    question_id = uuid.UUID(question["id"])
    assert key not in _cache(client).values
    paused = client.patch(
        f"/api/v1/rewards/{reward_id}", json={"active": False}, headers=_csrf(client)
    )
    assert paused.json()["active"] is False
    icon = client.put(
        f"/api/v1/rewards/{reward_id}/icon",
        content=_png(40, 40),
        headers={**_csrf(client), "Content-Type": "image/png"},
    )
    assert icon.status_code == 200, icon.text
    assert icon.json()["icon_url"].startswith(f"/api/reward/icon/{reward_id}?v=")
    listed = client.get("/api/v1/rewards", params={"q": "torta"}).json()
    assert [item["id"] for item in listed["items"]] == [reward_id]

    events = (
        RewardEvent(uuid.UUID(reward_id), date(2026, 11, 9), RewardEventKind.OPEN),
        RewardEvent(
            uuid.UUID(reward_id),
            date(2026, 11, 9),
            RewardEventKind.ANSWER,
            question_id=question_id,
            answer=2,
        ),
    )
    lead = RewardLeadSubmission(
        uuid.UUID(reward_id), "Bia", "bia@email.com", "es", ((question_id, 2),), NOW
    )
    record_reward_batch(
        SqlAlchemyUnitOfWork(engine, bypass_rls=True),
        batch=RewardBatch("lote", events, (lead,)),
        clock=SystemClock(),
    )
    metrics = client.get(
        f"/api/v1/rewards/{reward_id}/metrics", params={"from": "2026-11-08", "to": "2026-11-09"}
    ).json()
    assert metrics["total"]["opens"] == 1 and len(metrics["days"]) == 2
    assert metrics["answers"] == [{"question_id": str(question_id), "answer": 2, "count": 1}]
    assert ana.get(f"/api/v1/rewards/{reward_id}/leads").status_code == 403
    leads = client.get(
        f"/api/v1/rewards/{reward_id}/leads", params={"question_id": str(question_id), "answer": 2}
    ).json()
    assert [item["contact"] for item in leads["items"]] == ["bia@email.com"]
    assert leads["items"][0]["answers"] == [{"question_id": str(question_id), "answer": 2}]
    csv = client.get(f"/api/v1/rewards/{reward_id}/leads/export")
    assert csv.headers["content-type"].startswith("text/csv")
    assert "Bia,bia@email.com,Espanhol,Fubá" in csv.text

    gone = client.delete(f"/api/v1/rewards/{reward_id}", headers=_csrf(client))
    assert gone.status_code == 204
    assert client.get(f"/api/v1/rewards/{reward_id}").status_code == 404
    deleted = client.get("/api/v1/rewards", params={"deleted": "true"}).json()["items"]
    assert [item["id"] for item in deleted] == [reward_id] and deleted[0]["deleted_at"]
    assert client.get("/api/v1/rewards").json()["total"] == 0
    still = client.get(f"/api/v1/rewards/{reward_id}/leads").json()["items"]
    assert [item["name"] for item in still] == ["Bia"]
    lead_url = f"/api/v1/rewards/{reward_id}/leads/{still[0]['id']}"
    assert ana.delete(lead_url, headers=_csrf(ana)).status_code == 403
    assert client.delete(lead_url, headers=_csrf(client)).status_code == 204
    assert client.get(f"/api/v1/rewards/{reward_id}/leads").json()["total"] == 0
    actions = {item["action"] for item in client.get("/api/v1/audit").json()["items"]}
    assert {"reward.leads_exported", "reward.lead_deleted"} <= actions


def test_rewards_internal(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    site_id = _site(engine, uuid.UUID(me["active_company_id"]))
    staff = _staff(client, engine)
    assert client.get("/api/v1/internal/rewards").status_code == 403
    created = staff.post("/api/v1/internal/rewards", json=_body(site_id), headers=_csrf(staff))
    assert created.status_code == 201, created.text
    reward = created.json()
    assert reward["client"]["id"] == me["active_company_id"]
    listed = staff.get("/api/v1/internal/rewards").json()
    assert [item["id"] for item in listed["items"]] == [reward["id"]]
    assert [item["id"] for item in client.get("/api/v1/rewards").json()["items"]] == [reward["id"]]
    groups = staff.get(f"/api/v1/internal/sites/{site_id}/reward-ad-units").json()
    assert len(groups) == 2
    metrics = staff.get(f"/api/v1/internal/rewards/{reward['id']}/metrics").json()
    assert metrics["total"]["opens"] == 0 and len(metrics["days"]) == 30
    assert staff.get(f"/api/v1/internal/rewards/{reward['id']}/leads").json()["total"] == 0
    paused = staff.patch(
        f"/api/v1/internal/rewards/{reward['id']}", json={"active": False}, headers=_csrf(staff)
    )
    assert paused.json()["active"] is False
    audit = client.get("/api/v1/audit").json()["items"]
    assert {"reward.created", "reward.paused"} <= {item["action"] for item in audit}
