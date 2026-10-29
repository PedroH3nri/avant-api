"""Paginação de 10 itens: a equipe paginada no banco e a lista leve de papéis."""

import uuid
from datetime import UTC, datetime, timedelta

from avant_core.company.models import Membership
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity.models import User
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import FINANCE, CapturingMailer
from tests.test_api import _onboard_owner


def test_members_come_in_pages_of_ten(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    start = datetime(2026, 1, 1, tzinfo=UTC)
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        for index in range(11):
            user = User(f"p{index}@acai.com", f"Pessoa {index:02d}")
            uow.users.add(user)
            uow.memberships.add(
                Membership(company_id, user.id, FINANCE, start + timedelta(minutes=index))
            )
        uow.commit()
    first = client.get("/api/v1/members").json()
    assert (first["total"], first["pages"], first["page"], first["page_size"]) == (12, 2, 1, 10)
    assert len(first["items"]) == 10 and first["items"][0]["user"]["name"] == "Dono"
    second = client.get("/api/v1/members?page=2").json()
    assert [item["user"]["name"] for item in second["items"]] == ["Pessoa 01", "Pessoa 00"]
    found = client.get("/api/v1/members?q=pessoa 1").json()
    assert [item["user"]["name"] for item in found["items"]] == ["Pessoa 10"]
    assert client.get("/api/v1/members?page=0").status_code == 422
    assert client.get("/api/v1/members?page=9").json()["items"] == []


def test_role_options_are_light(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    options = client.get("/api/v1/roles/options")
    assert options.status_code == 200, options.text
    items = options.json()["items"]
    assert items and set(items[0]) == {"id", "name", "is_system", "site_scope"}
    assert any(item["id"] == str(FINANCE) for item in items)


def test_member_options_bring_the_whole_team(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        for index in range(11):
            user = User(f"q{index}@acai.com", f"Quem {index:02d}")
            uow.users.add(user)
            uow.memberships.add(Membership(company_id, user.id, FINANCE, datetime.now(UTC)))
        uow.commit()
    options = client.get("/api/v1/members/options")
    assert options.status_code == 200, options.text
    assert len(options.json()["items"]) == 12


def test_team_lists_come_in_pages(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from avant_core.audit.enums import ActorKind
    from avant_core.audit.models import AuditEntry
    from avant_core.company.enums import InvitationKind
    from avant_core.company.models import Invitation

    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    owner_id = uuid.UUID(me["user"]["id"])
    now = datetime.now(UTC)
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        for index in range(11):
            uow.invitations.add(
                Invitation(
                    InvitationKind.TEAM,
                    f"c{index}@acai.com",
                    f"hash-{index}",
                    now + timedelta(days=1, minutes=index),
                    owner_id,
                    company_id,
                    FINANCE,
                )
            )
            uow.audit.add(
                AuditEntry(
                    company_id,
                    "test.paged",
                    ActorKind.MEMBER,
                    now + timedelta(minutes=index),
                    actor_user_id=owner_id,
                )
            )
        uow.commit()
    invitations = client.get("/api/v1/invitations").json()
    assert (invitations["total"], invitations["pages"]) == (11, 2)
    assert invitations["items"][0]["email"] == "c10@acai.com"
    audit = client.get("/api/v1/audit?action=test.paged&page=2").json()
    assert (audit["total"], len(audit["items"]), audit["page"]) == (11, 1, 2)
    roles = client.get("/api/v1/roles").json()
    assert roles["page"] == 1 and roles["total"] >= len(roles["items"])
    groups = client.get("/api/v1/groups").json()
    assert groups["total"] == 0 and groups["pages"] == 0
    assert client.get("/api/v1/groups/options").status_code == 200
    keys = client.get("/api/v1/api-keys").json()
    assert keys["total"] == 0


def test_inventory_lists_come_in_pages(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    from avant_core.gam.inventory.models import AdUnit, Site
    from avant_core.gam.networks.enums import ConnectionType
    from avant_core.gam.networks.models import Network
    from avant_core.gam.sync.enums import SyncKind
    from avant_core.gam.sync.models import NetworkSyncRun

    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["active_company_id"])
    start = datetime(2026, 1, 1, tzinfo=UTC)
    network = Network(company_id, "555", ConnectionType.MCM, start)
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        uow.networks.add(network)
        for index in range(11):
            uow.sync_runs.add(
                NetworkSyncRun(
                    company_id, network.id, SyncKind.SITES, start + timedelta(minutes=index)
                )
            )
            uow.ad_units.add(AdUnit(company_id, network.id, f"u{index}", f"solto{index}", start))
        uow.commit()
    for index in range(11):
        with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
            uow.sites.add(Site(company_id, f"s{index:02d}.com", network.id, f"g{index}", start))
            uow.commit()
    networks = client.get("/api/v1/networks").json()
    assert (networks["total"], networks["items"][0]["network_code"]) == (1, "555")
    options = client.get("/api/v1/networks/options").json()["items"]
    assert [item["network_code"] for item in options] == ["555"]
    runs = client.get(f"/api/v1/networks/{network.id}/sync-runs?page=2").json()
    assert (runs["total"], len(runs["items"])) == (11, 1)
    sites = client.get("/api/v1/sites").json()
    assert (sites["total"], sites["pages"], sites["items"][0]["domain"]) == (11, 2, "s10.com")
    assert [item["domain"] for item in client.get("/api/v1/sites?q=s1").json()["items"]] == [
        "s10.com"
    ]
    assert len(client.get("/api/v1/sites/options").json()["items"]) == 11
    unlinked = client.get("/api/v1/ad-units/unlinked?page=2").json()
    assert (unlinked["total"], len(unlinked["items"])) == (11, 1)
