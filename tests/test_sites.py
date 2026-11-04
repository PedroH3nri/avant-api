"""Sites, ad units e sites por membro contra o Postgres. A importação é do worker: aqui
o inventário entra direto pelo Unit of Work."""

import uuid
from datetime import UTC, datetime

import pytest
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import AdUnit, Site
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.shared import options as options_module
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_team import _member_client

NOW = datetime(2026, 11, 2, 12, 0, tzinfo=UTC)


def _inventory(engine: Engine, company_id: uuid.UUID) -> dict[str, uuid.UUID]:
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        net = Network(company_id, "123", ConnectionType.SERVICE_ACCOUNT, NOW)
        uow.networks.add(net)
        acai = Site(company_id, "acai.com.br", net.id, "s1", NOW, "APPROVED")
        blog = Site(company_id, "blog.com", net.id, "s2", NOW, "DRAFT")
        for s in (acai, blog):
            uow.sites.add(s)
        root = AdUnit(company_id, net.id, "u1", "acai.com.br", NOW, site_id=acai.id)
        uow.ad_units.add(root)
        child = AdUnit(company_id, net.id, "u2", "topo", NOW, parent_id=root.id, site_id=acai.id)
        uow.ad_units.add(child)
        loose = AdUnit(company_id, net.id, "u3", "solto", NOW)
        uow.ad_units.add(loose)
        uow.commit()
        return {
            "acai": acai.id,
            "blog": blog.id,
            "root": root.id,
            "child": child.id,
            "network": net.id,
        }


def test_sites_and_assignment(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    ids = _inventory(engine, uuid.UUID(me["active_company_id"]))
    ana = _member_client(client, mailer, "ana@acai.com")  # Financeiro: sites.view, só atribuídos
    ana_id = next(
        m["id"] for m in client.get("/api/v1/members").json()["items"] if m["user"]["name"] == "Ana"
    )

    sites = client.get("/api/v1/sites").json()["items"]
    assert sorted((s["domain"], s["ad_units"]) for s in sites) == [
        ("acai.com.br", 2),
        ("blog.com", 0),
    ]
    assert [
        s["domain"] for s in client.get("/api/v1/sites?approval_status=draft").json()["items"]
    ] == ["blog.com"]
    unlinked = client.get("/api/v1/ad-units/unlinked").json()["items"]
    assert [u["name"] for u in unlinked] == ["solto"]

    # A Ana não vê nada até ter um site atribuído, e não atribui.
    assert ana.get("/api/v1/sites").json()["items"] == []
    assert ana.get("/api/v1/sites/options").json()["items"] == []
    assert ana.get("/api/v1/ad-units/unlinked").json()["total"] == 0
    assert ana.get(f"/api/v1/sites/{ids['acai']}").status_code == 404
    put = {"site_ids": [str(ids["acai"])]}
    denied = ana.put(f"/api/v1/members/{ana_id}/sites", json=put, headers=_csrf(ana))
    assert denied.status_code == 403 and denied.json()["error"]["code"] == "permission_denied"

    r = client.put(f"/api/v1/members/{ana_id}/sites", json=put, headers=_csrf(client))
    assert r.status_code == 200, r.text
    assert [s["domain"] for s in r.json()["items"]] == ["acai.com.br"]
    assert [s["domain"] for s in client.get(f"/api/v1/members/{ana_id}/sites").json()["items"]] == [
        "acai.com.br"
    ]

    ana_options = ana.get("/api/v1/sites/options").json()["items"]
    assert [s["domain"] for s in ana_options] == ["acai.com.br"]
    detail = ana.get(f"/api/v1/sites/{ids['acai']}").json()
    assert [u["name"] for u in detail["ad_units"]] == ["acai.com.br", "topo"]
    assert detail["assigned_to"] is None
    assert client.get(f"/api/v1/sites/{ids['acai']}").json()["assigned_to"] == [ana_id]
    by_network = f"/api/v1/ad-units?network_id={ids['network']}"
    assert ana.get("/api/v1/ad-units").status_code == 422
    assert {u["name"] for u in ana.get(by_network).json()["items"]} == {
        "acai.com.br",
        "topo",
    }
    assert ana.get(f"/api/v1/sites/{ids['acai']}/members").status_code == 403
    members = client.get(f"/api/v1/sites/{ids['acai']}/members").json()["items"]
    assert {(m["user"]["name"], m["via"]) for m in members} == {
        ("Dono", "all"),
        ("Ana", "assigned"),
    }

    # Ligar a raiz a outro site leva o filho junto; a Ana deixa de ver os dois.
    url = f"/api/v1/ad-units/{ids['root']}"
    assert ana.patch(url, json={"site_id": str(ids["blog"])}, headers=_csrf(ana)).status_code == 403
    moved = client.patch(url, json={"site_id": str(ids["blog"])}, headers=_csrf(client))
    assert moved.status_code == 200, moved.text
    assert moved.json()["site_id"] == str(ids["blog"]) and moved.json()["site_manual"] is True
    assert ana.get(by_network).json()["items"] == []
    back = client.patch(url, json={"automatic": True}, headers=_csrf(client))
    assert back.json()["site_manual"] is False

    unknown = {"site_ids": [str(uuid.uuid4())]}
    r = client.put(f"/api/v1/members/{ana_id}/sites", json=unknown, headers=_csrf(client))
    assert r.status_code == 404 and r.json()["error"]["code"] == "not_found"
    r = client.put(f"/api/v1/members/{ana_id}/sites", json={"site_ids": []}, headers=_csrf(client))
    assert r.json()["items"] == [] and ana.get("/api/v1/sites").json()["items"] == []
    audit = client.get("/api/v1/audit").json()["items"]
    assert {"site.assigned", "site.unassigned", "ad_unit.linked"} <= {e["action"] for e in audit}


def test_manual_site(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    me = _onboard_owner(client, engine, mailer)
    ids = _inventory(engine, uuid.UUID(me["active_company_id"]))
    ana = _member_client(client, mailer, "ana@acai.com")  # Financeiro: sem sites.manage

    body = {"domain": "https://www.Receitas.com.br/"}
    denied = ana.post("/api/v1/sites", json=body, headers=_csrf(ana))
    assert denied.status_code == 403 and denied.json()["error"]["code"] == "permission_denied"

    r = client.post("/api/v1/sites", json=body, headers=_csrf(client))
    assert r.status_code == 201, r.text
    site = r.json()
    assert site["domain"] == "receitas.com.br" and site["awaiting_gam"] is True
    assert site["network_id"] is None and site["synced_at"] is None and site["ad_units"] == 0
    listed = {s["domain"]: s["awaiting_gam"] for s in client.get("/api/v1/sites").json()["items"]}
    assert listed == {"acai.com.br": False, "blog.com": False, "receitas.com.br": True}
    assert client.get(f"/api/v1/sites/{site['id']}").json()["ad_units"] == []

    again = client.post("/api/v1/sites", json={"domain": "acai.com.br"}, headers=_csrf(client))
    assert again.status_code == 409 and again.json()["error"]["code"] == "site_exists"
    bad = client.post("/api/v1/sites", json={"domain": "nada"}, headers=_csrf(client))
    assert bad.status_code == 422 and bad.json()["error"]["code"] == "invalid_input"

    from_gam = client.delete(f"/api/v1/sites/{ids['acai']}", headers=_csrf(client))
    assert from_gam.status_code == 409 and from_gam.json()["error"]["code"] == "site_from_gam"
    assert ana.delete(f"/api/v1/sites/{site['id']}", headers=_csrf(ana)).status_code == 403
    assert client.delete(f"/api/v1/sites/{site['id']}", headers=_csrf(client)).status_code == 204
    assert client.get(f"/api/v1/sites/{site['id']}").status_code == 404


def test_site_category_and_responsible(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    """Categoria e responsável do site, sozinho e em lote, e quem não pode mudar."""
    me = _onboard_owner(client, engine, mailer)
    ids = _inventory(engine, uuid.UUID(me["active_company_id"]))
    ana = _member_client(client, mailer, "ana@acai.com")
    members = client.get("/api/v1/members").json()["items"]
    ana_user = next(member["user"]["id"] for member in members if member["user"]["name"] == "Ana")

    response = client.patch(
        f"/api/v1/sites/{ids['acai']}",
        json={"category": "food", "responsible_user_id": ana_user},
        headers=_csrf(client),
    )
    assert response.status_code == 200
    assert (response.json()["category"], response.json()["responsible_user_id"]) == (
        "food",
        ana_user,
    )
    response = client.patch(
        "/api/v1/sites",
        json={"site_ids": [str(ids["acai"]), str(ids["blog"])], "category": "news"},
        headers=_csrf(client),
    )
    assert response.status_code == 200
    found = {site["domain"]: site for site in response.json()["items"]}
    assert found["acai.com.br"]["category"] == "news"
    assert found["acai.com.br"]["responsible_user_id"] == ana_user
    assert found["blog.com"]["responsible_user_id"] is None
    cleared = client.patch(
        f"/api/v1/sites/{ids['acai']}", json={"category": None}, headers=_csrf(client)
    )
    assert cleared.json()["category"] is None
    assert cleared.json()["responsible_user_id"] == ana_user

    assert (
        client.patch(
            f"/api/v1/sites/{ids['acai']}", json={"category": "cars"}, headers=_csrf(client)
        ).status_code
        == 422
    )
    assert (
        client.patch(
            f"/api/v1/sites/{ids['acai']}",
            json={"responsible_user_id": str(uuid.uuid4())},
            headers=_csrf(client),
        ).status_code
        == 422
    )
    assert (
        client.patch(f"/api/v1/sites/{ids['acai']}", json={}, headers=_csrf(client)).status_code
        == 422
    )
    assert (
        ana.patch(
            f"/api/v1/sites/{ids['acai']}", json={"category": "news"}, headers=_csrf(ana)
        ).status_code
        == 403
    )
    assert (
        ana.patch(
            "/api/v1/sites",
            json={"site_ids": [str(ids["acai"])], "category": "news"},
            headers=_csrf(ana),
        ).status_code
        == 403
    )

    def domains(query: str) -> list[str]:
        """Os domínios da lista de sites com o filtro da query string."""
        return sorted(
            site["domain"] for site in client.get(f"/api/v1/sites?{query}").json()["items"]
        )

    assert domains("category=news") == ["blog.com"]
    assert domains("category=none") == ["acai.com.br"]
    assert domains(f"responsible_user_id={ana_user}") == ["acai.com.br"]
    assert domains("responsible_user_id=none") == ["blog.com"]
    assert client.get("/api/v1/sites?category=cars").status_code == 422

    catalog = client.get("/api/v1/metrics/catalog").json()
    assert {"site_category", "site_responsible"} <= {item["key"] for item in catalog["dimensions"]}
    assert catalog["site_categories"][0] == {
        "key": "news",
        "label": {"pt": "Notícias", "en": "News", "es": "Noticias"},
    }

    ana_member = next(member["id"] for member in members if member["user"]["name"] == "Ana")
    assert client.delete(f"/api/v1/members/{ana_member}", headers=_csrf(client)).status_code == 204
    assert client.get(f"/api/v1/sites/{ids['acai']}").json()["responsible_user_id"] is None


def test_options_have_a_ceiling_and_a_search(
    client: TestClient, engine: Engine, mailer: CapturingMailer, monkeypatch: pytest.MonkeyPatch
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _inventory(engine, uuid.UUID(me["active_company_id"]))
    found = client.get("/api/v1/sites/options?query=BLOG").json()["items"]
    assert [site["domain"] for site in found] == ["blog.com"]
    monkeypatch.setattr(options_module, "OPTIONS_LIMIT", 1)
    assert len(client.get("/api/v1/sites/options").json()["items"]) == 1
    assert len(client.get("/api/v1/networks/options").json()["items"]) == 1
