"""Comissão da equipe Groone contra o Postgres: regras no papel, data de início, consultas,
desconto, criação da invoice e permissões."""

import uuid
from datetime import UTC, date, datetime, timedelta
from decimal import Decimal

from avant_core.access.models import Role
from avant_core.commissions.enums import CommissionEvent, CommissionStatus
from avant_core.commissions.models import CommissionWindow, DailyCommission
from avant_core.commissions.services import calculate_day, close_month
from avant_core.company.models import Company
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_mfa import _enable


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


class NextMonthClock:
    """Relógio no começo do mês seguinte, para fechar o mês de hoje no teste."""

    def __init__(self, today: date) -> None:
        self.today = today

    def now(self) -> datetime:
        start = self.today.replace(day=28) + timedelta(days=4)
        return datetime(start.year, start.month, 2, tzinfo=UTC)


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
    early = staff.post("/api/v1/internal/invoices", json={"month": month}, headers=_csrf(staff))
    assert early.status_code == 409
    assert early.json()["error"]["code"] == "commission_not_validated"
    discount = staff.post(
        f"/api/v1/internal/commissions/people/{user_id}/adjustments",
        json={"month": month, "amount": "12.50", "reason": "Network banida"},
        headers=_csrf(staff),
    )
    assert discount.status_code == 201, discount.text
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        close_month(uow, month=today.replace(day=1), clock=NextMonthClock(today))
        uow.commit()
    invoice = staff.post("/api/v1/internal/invoices", json={"month": month}, headers=_csrf(staff))
    assert invoice.status_code == 201, invoice.text
    assert invoice.json()["items"][0]["kind"] == "commission"
    team = staff.get(f"/api/v1/internal/commissions?month={month}").json()["items"]
    assert team[0]["month"]["status"] == "issued" and team[0]["month"]["adjustments"] == "-12.50"
    late = staff.post(
        f"/api/v1/internal/commissions/people/{user_id}/adjustments",
        json={"month": month, "amount": "1.00", "reason": "Depois de emitido"},
        headers=_csrf(staff),
    )
    assert late.status_code == 422

    owner = TestClient(client.app)
    _onboard_owner(owner, engine, mailer)
    assert owner.get("/api/v1/internal/commissions").status_code == 403
    assert owner.get("/api/v1/internal/commissions/me").status_code == 403


def test_groone_role_with_internal_permissions(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    keys = {item["key"] for item in staff.get("/api/v1/permissions").json()["items"]}
    assert {"internal.clients.view", "internal.commissions.manage"} <= keys
    created = staff.post(
        "/api/v1/roles",
        json={
            "name": "Comercial",
            "permissions": ["internal.clients.view", "internal.commissions.view"],
            "site_scope": "all",
        },
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    assert set(created.json()["permissions"]) == {
        "internal.clients.view",
        "internal.commissions.view",
    }


def test_groone_role_with_the_whole_catalog(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    keys = sorted(item["key"] for item in staff.get("/api/v1/permissions").json()["items"])
    assert len(keys) > 32
    created = staff.post(
        "/api/v1/roles",
        json={"name": "Tudo", "permissions": keys, "site_scope": "all"},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    assert sorted(created.json()["permissions"]) == keys
    updated = staff.patch(
        f"/api/v1/roles/{created.json()['id']}",
        json={"permissions": keys[:-1]},
        headers=_csrf(staff),
    )
    assert updated.status_code == 200, updated.text
    too_many = staff.post(
        "/api/v1/roles",
        json={"name": "Demais", "permissions": [*keys, "extra.permission"]},
        headers=_csrf(staff),
    )
    assert too_many.status_code == 422


def _support(client: TestClient, staff: TestClient, mailer: CapturingMailer) -> TestClient:
    """Uma pessoa da equipe Groone com o papel de suporte (sem as permissões da comissão)."""
    roles = staff.get("/api/v1/roles").json()["items"]
    support_role = next(role for role in roles if role["key"] == "groone_support")
    invited = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "suporte@groone.com", "role_id": support_role["id"]},
        headers=_csrf(staff),
    )
    assert invited.status_code == 201, invited.text
    support = TestClient(client.app)
    accepted = support.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Suporte", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    _enable(support)
    return support


def test_who_sees_and_changes_commissions(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    support = _support(client, staff, mailer)
    me = support.get("/api/v1/auth/me").json()["user"]["id"]
    admin = staff.get("/api/v1/auth/me").json()["user"]["id"]
    month = datetime.now(UTC).strftime("%Y-%m")
    assert support.get(f"/api/v1/internal/commissions?month={month}").status_code == 403
    other = support.get(f"/api/v1/internal/commissions/people/{admin}?month={month}")
    assert other.status_code == 403
    own = support.get(f"/api/v1/internal/commissions/people/{me}?month={month}")
    assert own.status_code == 200
    assert support.get(f"/api/v1/internal/commissions/me?month={month}").status_code == 200
    people = support.get("/api/v1/internal/staff/options").json()["items"]
    assert {person["user"]["id"] for person in people} == {me, admin}
    assert all(set(person) >= {"id", "user", "role", "status"} for person in people)
    refused = support.put(
        "/api/v1/internal/commissions/settings",
        json={"starts_on": "2026-11-01"},
        headers=_csrf(support),
    )
    assert refused.status_code == 403
    no_csrf = staff.put("/api/v1/internal/commissions/settings", json={"starts_on": "2026-11-01"})
    assert no_csrf.status_code == 403 and no_csrf.json()["error"]["code"] == "csrf_failed"


def test_client_owner_cannot_touch_commissions(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    user_id = client.get("/api/v1/auth/me").json()["user"]["id"]
    for method, url, body in (
        ("put", "/api/v1/internal/commissions/settings", {"starts_on": "2026-11-01"}),
        ("post", "/api/v1/internal/invoices", {"month": "2026-10"}),
        (
            "post",
            f"/api/v1/internal/commissions/people/{user_id}/adjustments",
            {"month": "2026-10", "amount": "1.00", "reason": "x"},
        ),
        ("get", "/api/v1/internal/staff/options", None),
    ):
        found = (
            getattr(client, method)(url, json=body, headers=_csrf(client))
            if body
            else (client.get(url))
        )
        assert found.status_code == 403, (url, found.text)


def test_commission_input_is_checked(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    user_id = staff.get("/api/v1/auth/me").json()["user"]["id"]
    role = _admin_role(staff)
    rules = f"/api/v1/internal/roles/{role['id']}/commission-rules"
    base = {"event": "client_created", "percentage": "5", "start_offset_days": 0}
    for wrong in ({"percentage": "100.01"}, {"percentage": "1.234"}, {"percentage": "0"}):
        found = staff.post(rules, json={**base, **wrong}, headers=_csrf(staff))
        assert found.status_code == 422, wrong
    adjustments = f"/api/v1/internal/commissions/people/{user_id}/adjustments"
    for amount in ("0", "-5", "1.234"):
        found = staff.post(
            adjustments,
            json={"month": "2026-10", "amount": amount, "reason": "x"},
            headers=_csrf(staff),
        )
        assert found.status_code == 422, amount
    assert staff.get("/api/v1/internal/commissions?month=0000-01").status_code == 422


def test_start_date_is_locked_after_the_first_closing(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    url = "/api/v1/internal/commissions/settings"
    person = uuid.UUID(staff.get("/api/v1/auth/me").json()["user"]["id"])
    assert staff.put(url, json={"starts_on": "2026-10-01"}, headers=_csrf(staff)).status_code == 200
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        groone = uow.companies.internal()
        assert groone is not None
        role = Role(key="vendas", name={"pt": "Vendas"}, company_id=groone.id)
        uow.roles.add(role)
        client_company = Company(name="Alfa", owner_user_id=None, seat_limit=2, slug="alfa-trava")
        uow.companies.add(client_company)
        window = CommissionWindow(
            CommissionEvent.CLIENT_CREATED,
            client_company.id,
            date(2026, 10, 1),
            datetime.now(UTC),
            role_id=role.id,
            user_id=person,
            starts_on=date(2026, 10, 1),
        )
        uow.commission_windows.add(window)
        uow.daily_commissions.add(
            DailyCommission(
                window.id,
                date(2026, 10, 2),
                person,
                Decimal("5"),
                0,
                0,
                CommissionStatus.VALIDATED,
                datetime.now(UTC),
            )
        )
        uow.commit()
    locked = staff.put(url, json={"starts_on": "2026-11-01"}, headers=_csrf(staff))
    assert locked.status_code == 409
    assert locked.json()["error"]["code"] == "commission_start_locked"


def test_client_edit_without_the_manager_keeps_it(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    me = staff.get("/api/v1/auth/me").json()["user"]["id"]
    profile = {"first_name": "Dono", "last_name": "Beta", "email": "dono@beta.com"}
    created = staff.post(
        "/api/v1/internal/clients",
        json={"name": "Beta", "seat_limit": 2, "profile": {**profile, "account_manager_id": me}},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    company_id = created.json()["id"]
    edited = staff.patch(
        f"/api/v1/internal/clients/{company_id}",
        json={"profile": {**profile, "notes": "Sem mudar o responsável"}},
        headers=_csrf(staff),
    )
    assert edited.status_code == 200, edited.text
    detail = staff.get(f"/api/v1/internal/clients/{company_id}").json()
    assert detail["profile"]["account_manager_id"] == me
    cleared = staff.patch(
        f"/api/v1/internal/clients/{company_id}",
        json={"profile": {**profile, "account_manager_id": None}},
        headers=_csrf(staff),
    )
    assert cleared.status_code == 200, cleared.text
    assert (
        staff.get(f"/api/v1/internal/clients/{company_id}").json()["profile"]["account_manager_id"]
        is None
    )


def test_manager_change_preview(client: TestClient, engine: Engine) -> None:
    staff = _staff(client, engine)
    me = staff.get("/api/v1/auth/me").json()["user"]["id"]
    role = _admin_role(staff)
    staff.post(
        f"/api/v1/internal/roles/{role['id']}/commission-rules",
        json={"event": "client_created", "percentage": "5", "start_offset_days": 0},
        headers=_csrf(staff),
    )
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        groone = uow.companies.internal()
        assert groone is not None
        membership = uow.memberships.get_for(groone.id, uuid.UUID(me))
        assert membership is not None
        membership.role_id = uuid.UUID(role["id"])
        uow.commit()
    profile = {
        "first_name": "Dono",
        "last_name": "Gama",
        "email": "dono@gama.com",
        "account_manager_id": me,
    }
    created = staff.post(
        "/api/v1/internal/clients",
        json={"name": "Gama", "seat_limit": 2, "profile": profile},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    company_id = created.json()["id"]
    same = staff.get(f"/api/v1/internal/clients/{company_id}/manager-change?user_id={me}")
    assert same.status_code == 200, same.text
    assert same.json() == {"continues": 1, "stops": 0, "arrives": 0}
    removed = staff.get(f"/api/v1/internal/clients/{company_id}/manager-change")
    assert removed.json() == {"continues": 0, "stops": 1, "arrives": 0}


def test_staff_without_the_permissions_and_sessions_without_2fa_are_refused(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    role = staff.post(
        "/api/v1/roles",
        json={"name": "Sem acesso", "permissions": [], "site_scope": "all"},
        headers=_csrf(staff),
    )
    assert role.status_code == 201, role.text
    invited = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "sem@groone.com", "role_id": role.json()["id"]},
        headers=_csrf(staff),
    )
    assert invited.status_code == 201, invited.text
    plain = TestClient(client.app)
    accepted = plain.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Sem", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    no_2fa = plain.get("/api/v1/internal/commissions/me?month=2026-10")
    assert no_2fa.status_code == 403 and no_2fa.json()["error"]["code"] == "mfa_required"
    _enable(plain)
    assert plain.get("/api/v1/internal/staff/options").status_code == 403
    me = staff.get("/api/v1/auth/me").json()["user"]["id"]
    created = staff.post(
        "/api/v1/internal/clients",
        json={
            "name": "Delta",
            "seat_limit": 2,
            "profile": {"first_name": "Dono", "last_name": "Delta", "email": "dono@delta.com"},
        },
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    company_id = created.json()["id"]
    preview = f"/api/v1/internal/clients/{company_id}/manager-change?user_id={me}"
    assert plain.get(preview).status_code == 403
    assert staff.get(preview).status_code == 200
    unknown = staff.get(f"/api/v1/internal/clients/{uuid.uuid4()}/manager-change?user_id={me}")
    assert unknown.status_code == 404
    outsider = staff.get(
        f"/api/v1/internal/clients/{company_id}/manager-change?user_id={uuid.uuid4()}"
    )
    assert outsider.status_code == 404
