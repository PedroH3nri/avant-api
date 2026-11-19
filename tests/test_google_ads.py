"""Google Ads no painel do cliente e no interno contra o Postgres: login do Google, contas,
sufixo, pessoas, campanhas, palavras-chave, termos, histórico, avisos e os casos sem permissão
e sem o cliente configurado."""

import uuid
from urllib.parse import parse_qs, urlparse

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.google_ads.services import (
    AVANT_SUFFIX,
    sync_google_ads_login,
    sync_google_ads_metrics,
)
from avant_core.identity.security.crypto import FernetSecretBox
from avant_core.shared.clock import SystemClock
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.container import Services
from tests.conftest import CapturingMailer
from tests.fakes import FakeGoogleAds
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_team import _member_client

API = "/api/v1/google-ads"


def _services(client: TestClient) -> Services:
    """Os serviços da aplicação de teste."""
    return client.app.state.services  # type: ignore[attr-defined,no-any-return]


def _configure(client: TestClient) -> FakeGoogleAds:
    """Liga a API do Google Ads falsa e uma chave de tokens nova na aplicação de teste."""
    services = _services(client)
    fake = FakeGoogleAds()
    services.google_ads = fake
    services.google_ads_box = FernetSecretBox(Fernet.generate_key().decode())
    services.settings.google_ads_client_id = "cliente-1"
    return fake


def _connect(client: TestClient) -> str:
    """Faz o login do Google de ponta a ponta e devolve para onde o painel voltou."""
    start = client.get(f"{API}/oauth/start", follow_redirects=False)
    assert start.status_code == 302, start.text
    target = urlparse(start.headers["location"])
    query = parse_qs(target.query)
    assert target.netloc == "accounts.google.com" and query["client_id"] == ["cliente-1"]
    assert query["access_type"] == ["offline"] and "adwords" in query["scope"][0]
    assert query["redirect_uri"][0].endswith("/api/v1/google-ads/oauth/callback")
    back = client.get(
        f"{API}/oauth/callback",
        params={"code": "codigo", "state": query["state"][0]},
        follow_redirects=False,
    )
    assert back.status_code == 302
    return str(back.headers["location"])


def _sync(engine: Engine, client: TestClient, company_id: uuid.UUID) -> None:
    """Faz o papel do worker: estrutura e números do login conectado."""
    services = _services(client)
    assert services.google_ads is not None and services.google_ads_box is not None
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        login = uow.google_ads_logins.list_for_company(company_id)[0]
        accounts = uow.google_ads_accounts.list_for_login(login.id)
    sync_google_ads_login(
        SqlAlchemyUnitOfWork(engine, company_id=company_id),
        gateway=services.google_ads,
        box=services.google_ads_box,
        login_id=login.id,
        clock=SystemClock(),
    )
    sync_google_ads_metrics(
        SqlAlchemyUnitOfWork(engine, company_id=company_id),
        gateway=services.google_ads,
        box=services.google_ads_box,
        account_id=accounts[0].id,
        days=1,
        clock=SystemClock(),
        with_terms=True,
    )


def test_without_the_google_client_the_login_is_unavailable(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    start = client.get(f"{API}/oauth/start", follow_redirects=False)
    assert start.status_code == 503
    assert start.json()["error"]["code"] == "google_ads_not_configured"


def test_google_ads_panel(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    fake = _configure(client)

    forged = client.get(
        f"{API}/oauth/callback",
        params={"code": "codigo", "state": "outro"},
        follow_redirects=False,
    )
    assert forged.headers["location"].endswith("/google-ads?erro=google_ads_state_invalid")
    assert _connect(client).endswith("/google-ads?google_ads=conectado")
    assert fake.codes[0][0] == "codigo"

    logins = client.get(f"{API}/logins").json()
    assert [login["email"] for login in logins] == ["dono@gmail.com"]
    assert "refresh-1" not in str(logins)
    accounts = client.get(f"{API}/accounts").json()
    assert [account["customer_id"] for account in accounts] == ["1234567890"]
    assert accounts[0]["suffix_state"] == "missing"
    account_id = accounts[0]["id"]

    suffixed = client.post(f"{API}/accounts/{account_id}/suffix", headers=_csrf(client))
    assert suffixed.status_code == 200, suffixed.text
    assert suffixed.json()["suffix_state"] == "ok"
    assert fake.calls == [("suffix", "5550001111", "1234567890", AVANT_SUFFIX)]
    limited = client.put(
        f"{API}/accounts/{account_id}",
        json={"daily_limit": "150.50", "on_limit": "pause"},
        headers=_csrf(client),
    )
    assert limited.status_code == 200, limited.text
    assert limited.json()["daily_limit"] == "150.5" and limited.json()["on_limit"] == "pause"

    _sync(engine, client, company_id)
    campaigns = client.get(f"{API}/objects").json()
    assert [item["external_id"] for item in campaigns["items"]] == ["111"]
    assert campaigns["items"][0]["totals"]["spend"] == "5"
    ads = client.get(f"{API}/objects", params={"level": "ad", "parent": "222"}).json()
    assert [item["name"] for item in ads["items"]] == ["Anúncio"]
    detail = client.get(f"{API}/objects/ad/333").json()
    assert detail["ad_group"]["external_id"] == "222" and detail["campaign"]["name"] == "Bolo"
    assert [point["totals"]["spend"] for point in detail["daily"]] == ["5"]
    assert client.get(f"{API}/objects/campaign/333").status_code == 404
    keywords = client.get(f"{API}/ad-groups/222/keywords").json()
    assert [(word["text"], word["target_id"]) for word in keywords] == [
        ("bolo de cenoura", "kwd-44")
    ]
    terms = client.get(f"{API}/objects/campaign/111/search-terms").json()
    assert [(term["text"], term["detail"]) for term in terms] == [("bolo", "bolo de cenoura")]
    assert client.get(f"{API}/objects/ad/333/search-terms").status_code == 422
    assert client.get(f"{API}/objects/ad_group/222/placements").json() == []
    wide = client.get(f"{API}/objects", params={"from": "2020-01-01", "to": "2026-01-01"})
    assert wide.status_code == 422

    history = client.get(f"{API}/changes").json()
    assert history["total"] >= 1 and history["items"][0]["origin"] == "avant"
    assert client.get(f"{API}/alerts").json()["total"] == 0
    settings = client.get(f"{API}/alert-settings").json()
    changed = [{**setting, "email": False} for setting in settings[:1]]
    saved = client.put(f"{API}/alert-settings", json=changed, headers=_csrf(client))
    assert saved.status_code == 200 and saved.json()[0]["email"] is False

    ana = _member_client(client, mailer, "ana@acai.com")
    assert ana.get(f"{API}/accounts").status_code == 403
    assert ana.get(f"{API}/oauth/start", follow_redirects=False).status_code == 403
    people = client.get(f"{API}/people").json()
    ana_id = next(
        item["person"]["id"] for item in people if item["person"]["email"] == "ana@acai.com"
    )
    moved = client.put(
        f"{API}/people/{ana_id}",
        json={"account_ids": [account_id], "monthly_limit": "3000"},
        headers=_csrf(client),
    )
    assert moved.status_code == 200, moved.text
    assert moved.json()["account_ids"] == [account_id]
    assert client.get(f"{API}/accounts").json()[0]["holder"]["email"] == "ana@acai.com"

    staff = _staff(client, engine)
    internal = staff.get("/api/v1/internal/google-ads/accounts").json()
    assert [account["company_id"] for account in internal] == [str(company_id)]
    internal_ads = staff.get(
        "/api/v1/internal/google-ads/objects", params={"company_id": str(company_id)}
    ).json()
    assert internal_ads["total"] == 1
    assert staff.get("/api/v1/internal/google-ads/objects/campaign/111").status_code == 200
    assert staff.get("/api/v1/internal/google-ads/ad-groups/222/keywords").status_code == 200
    assert staff.get("/api/v1/internal/google-ads/changes").json()["total"] >= 1
    assert staff.get("/api/v1/internal/google-ads/alerts").status_code == 200
    assert client.get("/api/v1/internal/google-ads/accounts").status_code == 403

    gone = client.delete(f"{API}/logins/{logins[0]['id']}", headers=_csrf(client))
    assert gone.status_code == 204 and fake.revoked == ["refresh-1"]
    assert client.get(f"{API}/logins").json()[0]["status"] != "ok"
