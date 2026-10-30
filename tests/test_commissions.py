"""Comissão da equipe Groone contra o Postgres: regras no papel, data de início, consultas,
desconto, emissão e permissões."""

import uuid
from datetime import UTC, datetime

from avant_core.commissions.services import calculate_day, close_month
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff


def _admin_role(staff: TestClient) -> dict:  # type: ignore[type-arg]
    """O papel de administrador da Company Groone."""
    roles = staff.get("/api/v1/roles").json()["items"]
    return next(item for item in roles if item["key"] == "groone_admin")


def test_rules_on_the_role(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    role = _admin_role(staff)
    url = f"/api/v1/internal/roles/{role['id']}/commission-rules"
    body = {
        "event": "client_created",
        "percentage": "5",
        "start_offset_days": 7,
        "duration_days": 30,
    }
    created = staff.post(url, json=body, headers=_csrf(staff))
    assert created.status_code == 201, created.text
    rule = created.json()
    assert (rule["event"], rule["percentage"], rule["duration_days"]) == (
        "client_created",
        "5.00",
        30,
    )
    taken = staff.post(url, json=body, headers=_csrf(staff))
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "commission_rule_taken"
    edited = staff.put(
        f"{url}/{rule['id']}",
        json={**body, "percentage": "10.5", "duration_days": None},
        headers=_csrf(staff),
    )
    assert edited.status_code == 200 and edited.json()["percentage"] == "10.50"
    bad = staff.post(
        url, json={**body, "event": "site_created", "percentage": "0"}, headers=_csrf(staff)
    )
    assert bad.status_code == 422
    assert [item["event"] for item in staff.get(url).json()["items"]] == ["client_created"]
    deleted = staff.delete(f"/api/v1/internal/commission-rules/{rule['id']}", headers=_csrf(staff))
    assert deleted.status_code == 204
    assert staff.get(url).json()["items"] == []


def test_start_my_commission_team_discount_and_issue(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    me = staff.get("/api/v1/auth/me").json()
    role = _admin_role(staff)
    staff.post(
        f"/api/v1/internal/roles/{role['id']}/commission-rules",
        json={
            "event": "client_created",
            "percentage": "5",
            "start_offset_days": 0,
            "duration_days": 30,
        },
        headers=_csrf(staff),
    )
    today = datetime.now(UTC).date()
    month = today.strftime("%Y-%m")
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        groone = uow.companies.internal()
        assert groone is not None
        membership = uow.memberships.get_for(groone.id, uuid.UUID(me["user"]["id"]))
        assert membership is not None
        # O dono da Groone não tem papel; comissão é de quem tem um papel com regra.
        membership.role_id = uuid.UUID(role["id"])
        uow.commit()
    start = staff.put(
        "/api/v1/internal/commissions/settings",
        json={"starts_on": today.replace(day=1).isoformat()},
        headers=_csrf(staff),
    )
    assert start.status_code == 200, start.text
    assert (
        staff.get("/api/v1/internal/commissions/settings").json()["starts_on"]
        == today.replace(day=1).isoformat()
    )
    profile = {
        "first_name": "Dono",
        "last_name": "Alfa",
        "email": "dono@alfa.com",
        "account_manager_id": me["user"]["id"],
    }
    created = staff.post(
        "/api/v1/internal/clients",
        json={"name": "Alfa", "seat_limit": 2, "profile": profile},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        calculate_day(uow, day=today, clock=SystemClock())
        uow.commit()
    mine = staff.get(f"/api/v1/internal/commissions/me?month={month}").json()
    assert [item["target_name"] for item in mine["windows"]] == ["Alfa"]
    assert mine["month"]["status"] == "draft" and mine["month"]["total"] == "0.00"
    team = staff.get(f"/api/v1/internal/commissions?month={month}").json()["items"]
    assert [person["user"]["id"] for person in team] == [me["user"]["id"]]
    user_id = me["user"]["id"]
    detail = staff.get(f"/api/v1/internal/commissions/people/{user_id}?month={month}").json()[
        "items"
    ]
    assert detail[0]["target_name"] == "Alfa"
    early = staff.post(
        f"/api/v1/internal/commissions/people/{user_id}/issue",
        json={"month": month},
        headers=_csrf(staff),
    )
    assert early.status_code == 422
    discount = staff.post(
        f"/api/v1/internal/commissions/people/{user_id}/adjustments",
        json={"month": month, "amount": "12.50", "reason": "Network banida"},
        headers=_csrf(staff),
    )
    assert discount.status_code == 201, discount.text
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        close_month(uow, month=today.replace(day=1), clock=SystemClock())
        uow.commit()
    issued = staff.post(
        f"/api/v1/internal/commissions/people/{user_id}/issue",
        json={"month": month},
        headers=_csrf(staff),
    )
    assert issued.status_code == 200 and issued.json()["days"] == 1
    team = staff.get(f"/api/v1/internal/commissions?month={month}").json()["items"]
    assert team[0]["month"]["status"] == "issued" and team[0]["month"]["adjustments"] == "-12.50"

    owner = TestClient(client.app)
    _onboard_owner(owner, engine, mailer)
    assert owner.get("/api/v1/internal/commissions").status_code == 403
    assert owner.get("/api/v1/internal/commissions/me").status_code == 403
