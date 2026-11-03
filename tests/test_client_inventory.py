"""Networks e sites dos clientes com o status de faturamento, contra o Postgres."""

import uuid
from datetime import UTC, datetime, timedelta

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import Site
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from avant_core.metrics.models import GamCounts, GamDailyMetric
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _onboard_owner
from tests.test_internal import _staff

NOW = datetime.now(UTC)
YESTERDAY = NOW.date() - timedelta(days=1)


def _scaling_client(engine: Engine, company_id: uuid.UUID) -> None:
    """Uma network com um site: US$ 900 nos últimos 30 dias e US$ 600 nos 30 anteriores."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "4242", ConnectionType.MCM, NOW, "Rede Açaí")
        uow.networks.add(network)
        site = Site(company_id, "acai.com", network_id=network.id, gam_site_id="9", synced_at=NOW)
        uow.sites.add(site)
        uow.gam_metrics.upsert_daily(
            [
                GamDailyMetric(
                    company_id=company_id,
                    network_id=network.id,
                    date=day,
                    ad_unit_path="topo",
                    country_code="BR",
                    device="desktop",
                    revenue_micros=micros,
                    counts=GamCounts(impressions=1000),
                    synced_at=NOW,
                    site_id=site.id,
                )
                for day, micros in (
                    (YESTERDAY, 900_000_000),
                    (YESTERDAY - timedelta(days=30), 600_000_000),
                )
            ]
        )
        uow.commit()


def test_staff_sees_client_networks_sites_and_revenue_status(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["companies"][0]["id"])
    _scaling_client(engine, company_id)
    staff = _staff(client, engine)
    expected = {
        "trend": "scaling",
        "per_day": "30",
        "change_percent": 50,
        "recent": "900",
        "previous": "600",
    }

    clients = staff.get("/api/v1/internal/clients")
    assert clients.status_code == 200, clients.text
    (row,) = clients.json()["items"]
    assert row["revenue_status"] == expected

    networks = staff.get("/api/v1/internal/networks", params={"q": "açaí"})
    assert networks.status_code == 200, networks.text
    (network,) = networks.json()["items"]
    assert network["client"]["id"] == str(company_id) and network["sites"] == 1
    assert network["revenue_status"] == expected

    sites = staff.get("/api/v1/internal/sites", params={"q": "acai"})
    assert sites.status_code == 200, sites.text
    (site,) = sites.json()["items"]
    assert site["network_name"] == "Rede Açaí" and site["revenue_status"] == expected
    assert staff.get("/api/v1/internal/sites", params={"q": "outro"}).json()["items"] == []


def test_client_owner_cannot_list_client_networks_or_sites(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    for path in ("/api/v1/internal/networks", "/api/v1/internal/sites"):
        r = client.get(path)
        assert r.status_code == 403 and r.json()["error"]["code"] == "staff_only"
