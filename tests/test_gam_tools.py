"""Ferramentas do GAM no painel interno, contra o Postgres."""

import io
import uuid
import zipfile
from datetime import UTC, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import AdUnit, Site
from avant_core.gam.networks.enums import ConnectionType, Delegation
from avant_core.gam.networks.models import Network
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.tasks import RUN_GAM_TOOL, RecordingQueue
from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_mfa import _enable
from tests.test_support_tasks import _agent

BASE = "/api/v1/internal/gam-tools"
NOW = datetime.now(UTC)


def _network(engine: Engine, company_id: uuid.UUID) -> str:
    """Uma network M.I. com o seller ID e dois sites, um deles com blocos Tag Light."""
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        network = Network(
            company_id,
            "4242",
            ConnectionType.MCM,
            NOW,
            "Rede Açaí",
            delegation=Delegation.MANAGE_INVENTORY,
            seller_id="pub-55",
        )
        uow.networks.add(network)
        for domain in ("acai.com", "sucos.com"):
            uow.sites.add(
                Site(company_id, domain, network_id=network.id, gam_site_id=domain, synced_at=NOW)
            )
        parent = AdUnit(company_id, network.id, "1", "acai.com", NOW)
        uow.ad_units.add(parent)
        uow.ad_units.add(
            AdUnit(company_id, network.id, "2", "Acai_Content1_20261101", NOW, parent_id=parent.id)
        )
        uow.commit()
        return str(network.id)


def test_staff_lists_runs_and_downloads(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    network_id = _network(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)

    page = staff.get(f"{BASE}/networks", params={"q": "4242"})
    assert page.status_code == 200, page.text
    (row,) = page.json()["items"]
    assert row["id"] == network_id and row["seller_id"] == "pub-55"
    detail = staff.get(f"{BASE}/networks/{network_id}").json()
    acai = next(site for site in detail["sites"] if site["domain"] == "acai.com")
    assert (acai["blocks"], acai["format"], acai["blocks_date"]) == (1, "light", "2026-11-01")

    started = staff.post(
        f"{BASE}/runs",
        json={
            "network_id": network_id,
            "kind": "setup",
            "domains": ["acai.com"],
            "format": "light",
        },
        headers=_csrf(staff),
    )
    assert started.status_code == 202, started.text
    run = started.json()
    assert run["state"] == "running" and run["steps"][0] == {
        "key": "info",
        "state": "pending",
        "site": None,
        "count": None,
        "gam_id": None,
        "error": None,
    }
    queue = client.app.state.services.tasks  # type: ignore[attr-defined]
    assert isinstance(queue, RecordingQueue)
    assert queue.sent[-1] == (RUN_GAM_TOOL, (run["id"],))
    again = staff.post(
        f"{BASE}/runs", json={"network_id": network_id, "kind": "sync"}, headers=_csrf(staff)
    )
    assert again.status_code == 409 and again.json()["error"]["code"] == "gam_tool_running"
    runs = staff.get(f"{BASE}/runs", params={"network": network_id}).json()
    assert [item["id"] for item in runs["items"]] == [run["id"]]
    everything = staff.get(f"{BASE}/runs").json()["items"]
    assert [item["id"] for item in everything] == [run["id"]]
    assert everything[0]["network"] == {
        "id": network_id,
        "network_code": "4242",
        "display_name": "Rede Açaí",
        "client_name": me["companies"][0]["name"],
    }
    shown = staff.get(f"{BASE}/runs/{run['id']}").json()
    assert shown["kind"] == "setup" and shown["requested_by"]["name"] == "Admin"

    lines = staff.get(f"{BASE}/ads-txt", params={"network": network_id}).json()["lines"]
    assert lines[-1] == "groone.com, pub-55, DIRECT" and len(lines) == 3
    single = staff.get(
        f"{BASE}/install", params={"network": network_id, "sites": ["acai.com"], "label": "en"}
    )
    assert single.status_code == 200, single.text
    assert 'filename="acai.com_2_Format.txt"' in single.headers["content-disposition"]
    assert 'data-network="22893970961,4242"' in single.text and "Sponsored Links:" in single.text
    missing = staff.get(
        f"{BASE}/install", params={"network": network_id, "sites": ["acai.com", "sucos.com"]}
    )
    assert missing.status_code == 409 and missing.json()["error"]["code"] == "no_blocks_yet"


def test_install_zip_for_several_sites(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["companies"][0]["id"])
    network_id = _network(engine, company_id)
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        sucos = next(
            site
            for site in uow.sites.list_for_network(uuid.UUID(network_id))
            if site.domain == "sucos.com"
        )
        parent = AdUnit(company_id, uuid.UUID(network_id), "3", "sucos.com", NOW, site_id=sucos.id)
        uow.ad_units.add(parent)
        uow.ad_units.add(
            AdUnit(
                company_id,
                uuid.UUID(network_id),
                "4",
                "Sucos_Content1_20261102",
                NOW,
                parent_id=parent.id,
            )
        )
        uow.commit()
    staff = _staff(client, engine)
    zipped = staff.get(
        f"{BASE}/install", params={"network": network_id, "sites": ["acai.com", "sucos.com"]}
    )
    assert zipped.status_code == 200, zipped.text
    assert zipped.headers["content-type"] == "application/zip"
    names = zipfile.ZipFile(io.BytesIO(zipped.content)).namelist()
    assert names == ["acai.com_2_Format.txt", "sucos.com_2_Format.txt"]


def _network_of(engine: Engine, company_id: uuid.UUID) -> str:
    """Uma network da própria Empresa (a Company Groone, aqui)."""
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        network = Network(company_id, "9999", ConnectionType.MCM, NOW, "Rede da Groone")
        uow.networks.add(network)
        uow.commit()
        return str(network.id)


def test_gam_tools_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    network_id = _network(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)
    agent = _agent(client, staff, mailer)
    assert agent.get(f"{BASE}/networks").status_code == 403
    assert agent.get(f"{BASE}/ads-txt", params={"network": network_id}).status_code == 403
    blocked = agent.post(
        f"{BASE}/runs", json={"network_id": network_id, "kind": "sync"}, headers=_csrf(agent)
    )
    assert blocked.status_code == 403
    assert client.get(f"{BASE}/networks").status_code in (401, 403)


def _gam_viewer(client: TestClient, staff: TestClient, mailer: CapturingMailer) -> TestClient:
    """Uma pessoa da equipe Groone que só vê as ferramentas do GAM, com 2FA."""
    role = staff.post(
        "/api/v1/roles",
        json={
            "name": "Leitura GAM",
            "permissions": ["internal.gam_tools.view"],
            "site_scope": "all",
        },
        headers=_csrf(staff),
    )
    assert role.status_code == 201, role.text
    invited = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "leitura@groone.com", "role_id": role.json()["id"]},
        headers=_csrf(staff),
    )
    assert invited.status_code == 201, invited.text
    viewer = TestClient(client.app)
    accepted = viewer.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Leitura", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    _enable(viewer)
    return viewer


def test_gam_tool_runs_refuse_what_they_should(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    network_id = _network(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)
    groone_id = uuid.UUID(staff.get("/api/v1/auth/me").json()["active_company_id"])
    groone_network = _network_of(engine, groone_id)
    runs = f"{BASE}/runs"
    setup = {"network_id": network_id, "kind": "setup", "domains": ["acai.com"], "format": "light"}

    viewer = _gam_viewer(client, staff, mailer)
    refused = viewer.post(runs, json=setup, headers=_csrf(viewer))
    assert refused.status_code == 403, refused.text
    assert viewer.get(f"{BASE}/networks/{network_id}").status_code == 200

    own = {"network_id": groone_network, "kind": "sync"}
    assert staff.post(runs, json=own, headers=_csrf(staff)).status_code == 404
    assert staff.post(runs, json=setup).status_code == 403

    no_format = {**setup, "format": None}
    assert staff.post(runs, json=no_format, headers=_csrf(staff)).status_code == 422
    elsewhere = {**setup, "domains": ["outro.com"]}
    assert staff.post(runs, json=elsewhere, headers=_csrf(staff)).status_code == 422
    too_long = {**setup, "domains": ["a" * 254]}
    assert staff.post(runs, json=too_long, headers=_csrf(staff)).status_code == 422
    install = {"network": network_id, "sites": ["a" * 254]}
    assert staff.get(f"{BASE}/install", params=install).status_code == 422

    unverified = TestClient(client.app)
    login = {"email": "admin@groone.com", "password": PASSWORD}
    pending = unverified.post("/api/v1/auth/login", json=login)
    assert pending.status_code == 200 and pending.json()["mfa_required"] is True
    blocked = unverified.post(runs, json=setup, headers={"X-CSRF-Token": "x"})
    assert blocked.status_code == 401, blocked.text


def test_a_run_the_queue_did_not_take_frees_the_network(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    network_id = _network(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)
    queue = client.app.state.services.tasks  # type: ignore[attr-defined]
    assert isinstance(queue, RecordingQueue)
    queue.offline = True
    sync = {"network_id": network_id, "kind": "sync"}
    down = staff.post(f"{BASE}/runs", json=sync, headers=_csrf(staff))
    assert down.status_code == 503 and down.json()["error"]["code"] == "queue_unavailable"
    assert down.headers["Retry-After"] == "30"
    (failed,) = staff.get(f"{BASE}/runs", params={"network": network_id}).json()["items"]
    assert failed["state"] == "failed"
    queue.offline = False
    again = staff.post(f"{BASE}/runs", json=sync, headers=_csrf(staff))
    assert again.status_code == 202, again.text
