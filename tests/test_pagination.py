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
    assert items and set(items[0]) == {"id", "name"}
    assert any(item["id"] == str(FINANCE) for item in items)
