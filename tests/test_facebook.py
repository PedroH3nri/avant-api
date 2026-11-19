"""Facebook no painel do cliente e no interno contra o Postgres: login, perfis, contas, pessoas,
campanhas, histórico, avisos e os casos sem permissão e sem o app configurado."""

import uuid
from urllib.parse import parse_qs, urlparse

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.facebook.services import sync_facebook_insights, sync_facebook_profile
from avant_core.identity.security.crypto import FernetSecretBox
from avant_core.shared.clock import SystemClock
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.container import Services
from tests.conftest import CapturingMailer
from tests.fakes import FakeFacebook
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_team import _member_client

RULE_FIELDS = {
    "scale",
    "up_roi",
    "up_by",
    "down_roi",
    "down_by",
    "pause",
    "min_roi",
    "days",
    "duplicate",
    "duplicate_roi",
}


def _services(client: TestClient) -> Services:
    """Os serviços da aplicação de teste."""
    return client.app.state.services  # type: ignore[attr-defined,no-any-return]


def _configure(client: TestClient) -> FakeFacebook:
    """Liga a Graph API falsa e uma chave de tokens nova na aplicação de teste."""
    services = _services(client)
    fake = FakeFacebook()
    services.facebook = fake
    services.facebook_box = FernetSecretBox(Fernet.generate_key().decode())
    services.settings.facebook_app_id = "app-1"
    return fake


def _connect(client: TestClient) -> str:
    """Faz o login do Facebook de ponta a ponta e devolve para onde o painel voltou."""
    start = client.get("/api/v1/facebook/oauth/start", follow_redirects=False)
    assert start.status_code == 302, start.text
    target = urlparse(start.headers["location"])
    query = parse_qs(target.query)
    assert target.netloc == "www.facebook.com" and query["client_id"] == ["app-1"]
    assert query["redirect_uri"][0].endswith("/api/v1/facebook/oauth/callback")
    back = client.get(
        "/api/v1/facebook/oauth/callback",
        params={"code": "codigo", "state": query["state"][0]},
        follow_redirects=False,
    )
    assert back.status_code == 302
    return str(back.headers["location"])


def _sync(engine: Engine, client: TestClient, company_id: uuid.UUID) -> None:
    """Faz o papel do worker: estrutura e números do perfil conectado."""
    services = _services(client)
    assert services.facebook is not None and services.facebook_box is not None
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        profile = uow.facebook_profiles.list_for_company(company_id)[0]
        accounts = uow.facebook_accounts.list_for_profile(profile.id)
    sync_facebook_profile(
        SqlAlchemyUnitOfWork(engine, company_id=company_id),
        gateway=services.facebook,
        box=services.facebook_box,
        profile_id=profile.id,
        clock=SystemClock(),
    )
    sync_facebook_insights(
        SqlAlchemyUnitOfWork(engine, company_id=company_id),
        gateway=services.facebook,
        box=services.facebook_box,
        account_id=accounts[0].id,
        days=1,
        clock=SystemClock(),
    )


def test_without_the_meta_app_the_login_is_unavailable(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    start = client.get("/api/v1/facebook/oauth/start", follow_redirects=False)
    assert start.status_code == 503
    assert start.json()["error"]["code"] == "facebook_not_configured"


def test_facebook_panel(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    fake = _configure(client)

    forged = client.get(
        "/api/v1/facebook/oauth/callback",
        params={"code": "codigo", "state": "outro"},
        follow_redirects=False,
    )
    assert forged.headers["location"].endswith("/facebook?erro=facebook_state_invalid")
    assert _connect(client).endswith("/facebook?facebook=conectado")
    assert fake.codes[0][0] == "codigo"

    profiles = client.get("/api/v1/facebook/profiles").json()
    assert [profile["name"] for profile in profiles] == ["Dono no Facebook"]
    assert "token-1" not in str(profiles)
    accounts = client.get("/api/v1/facebook/accounts").json()
    assert [account["external_id"] for account in accounts] == ["act_123"]
    assert accounts[0]["holder"] is None
    account_id = accounts[0]["id"]

    limited = client.put(
        f"/api/v1/facebook/accounts/{account_id}",
        json={"daily_limit": "150.50", "on_limit": "pause"},
        headers=_csrf(client),
    )
    assert limited.status_code == 200, limited.text
    assert limited.json()["daily_limit"] == "150.5" and limited.json()["on_limit"] == "pause"

    _sync(engine, client, company_id)
    campaigns = client.get("/api/v1/facebook/objects").json()
    assert [item["external_id"] for item in campaigns["items"]] == ["c1"]
    assert campaigns["items"][0]["totals"]["spend"] == "5"
    ads = client.get("/api/v1/facebook/objects", params={"level": "ad", "parent": "s1"}).json()
    assert [item["name"] for item in ads["items"]] == ["Carrossel"]
    detail = client.get("/api/v1/facebook/objects/a1").json()
    assert detail["adset"]["external_id"] == "s1" and detail["campaign"]["name"] == "Bolo"
    assert [point["totals"]["spend"] for point in detail["daily"]] == ["5"]
    wide = client.get("/api/v1/facebook/objects", params={"from": "2020-01-01", "to": "2026-01-01"})
    assert wide.status_code == 422

    history = client.get("/api/v1/facebook/changes").json()
    assert history["total"] >= 1 and history["items"][0]["origin"] == "avant"
    assert client.get("/api/v1/facebook/alerts").json()["total"] == 0
    settings = client.get("/api/v1/facebook/alert-settings").json()
    changed = [{**setting, "email": False} for setting in settings[:1]]
    saved = client.put("/api/v1/facebook/alert-settings", json=changed, headers=_csrf(client))
    assert saved.status_code == 200 and saved.json()[0]["email"] is False

    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get("/api/v1/facebook/accounts").status_code == 403
    assert ana.get("/api/v1/facebook/oauth/start", follow_redirects=False).status_code == 403
    people = client.get("/api/v1/facebook/people").json()
    ana_id = next(
        item["person"]["id"] for item in people if item["person"]["email"] == "ana@acai.com"
    )
    moved = client.put(
        f"/api/v1/facebook/people/{ana_id}",
        json={"account_ids": [account_id], "monthly_limit": "3000"},
        headers=_csrf(client),
    )
    assert moved.status_code == 200, moved.text
    assert moved.json()["account_ids"] == [account_id]
    holder = client.get("/api/v1/facebook/accounts").json()[0]["holder"]
    assert holder["email"] == "ana@acai.com"

    staff = _staff(client, engine)
    internal = staff.get("/api/v1/internal/facebook/accounts").json()
    assert [account["company_id"] for account in internal] == [str(company_id)]
    internal_ads = staff.get(
        "/api/v1/internal/facebook/objects", params={"company_id": str(company_id)}
    ).json()
    assert internal_ads["total"] == 1
    assert staff.get("/api/v1/internal/facebook/objects/c1").status_code == 200
    assert staff.get("/api/v1/internal/facebook/changes").json()["total"] >= 1
    assert staff.get("/api/v1/internal/facebook/alerts").status_code == 200
    assert client.get("/api/v1/internal/facebook/accounts").status_code == 403

    gone = client.delete(f"/api/v1/facebook/profiles/{profiles[0]['id']}", headers=_csrf(client))
    assert gone.status_code == 204 and fake.revoked == ["token-1"]
    assert client.get("/api/v1/facebook/profiles").json()[0]["status"] != "ok"


def test_facebook_control_and_rules(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    fake = _configure(client)
    _connect(client)
    account_id = client.get("/api/v1/facebook/accounts").json()[0]["id"]
    client.put(
        f"/api/v1/facebook/accounts/{account_id}",
        json={"daily_limit": "150", "on_limit": "pause"},
        headers=_csrf(client),
    )
    _sync(engine, client, company_id)

    paused = client.post(
        "/api/v1/facebook/objects/status",
        json={"external_ids": ["c1"], "active": False},
        headers=_csrf(client),
    )
    assert paused.status_code == 200, paused.text
    assert paused.json() == {"done": ["c1"], "failed": {}}
    assert ("status", "c1", "PAUSED") in fake.calls

    too_much = client.put(
        "/api/v1/facebook/objects/c1/budget",
        json={"daily_budget": "200"},
        headers=_csrf(client),
    )
    assert too_much.status_code == 200, too_much.text
    refused = client.post(
        "/api/v1/facebook/objects/status",
        json={"external_ids": ["c1"], "active": True},
        headers=_csrf(client),
    )
    assert refused.status_code == 409
    error = refused.json()["error"]
    assert error["code"] == "facebook_limit_exceeded"
    assert error["details"] == {
        "period": "daily",
        "scope": "account",
        "room": "150",
        "currency": "BRL",
    }
    lowered = client.put(
        "/api/v1/facebook/objects/c1/budget",
        json={"daily_budget": "120.5"},
        headers=_csrf(client),
    )
    assert lowered.json()["daily_budget"] == "120.5"
    both = client.put(
        "/api/v1/facebook/objects/c1/budget",
        json={"daily_budget": "1", "lifetime_budget": "1"},
        headers=_csrf(client),
    )
    assert both.status_code == 422

    suggested = client.get("/api/v1/facebook/objects/c1/rules").json()
    assert suggested["enabled"] is False and suggested["up_roi"] == 50
    rules = {**{key: suggested[key] for key in suggested if key in RULE_FIELDS}, "scale": True}
    saved = client.put("/api/v1/facebook/objects/c1/rules", json=rules, headers=_csrf(client))
    assert saved.status_code == 200, saved.text
    assert saved.json()["enabled"] is True
    wrong = client.put(
        "/api/v1/facebook/objects/c1/rules",
        json={**rules, "up_by": 0},
        headers=_csrf(client),
    )
    assert wrong.status_code == 422
    decisions = client.get("/api/v1/facebook/objects/c1/rule-decisions").json()
    assert decisions["total"] == 0

    ana = _member_client(client, mailer, "ana@acai.com")
    assert (
        ana.post(
            "/api/v1/facebook/objects/status",
            json={"external_ids": ["c1"], "active": False},
            headers=_csrf(ana),
        ).status_code
        == 403
    )
    staff = _staff(client, engine)
    assert staff.get("/api/v1/internal/facebook/objects/c1/rules").json()["scale"] is True
    assert staff.get("/api/v1/internal/facebook/objects/c1/rule-decisions").status_code == 200
    assert client.get("/api/v1/internal/facebook/objects/c1/rules").status_code == 403
