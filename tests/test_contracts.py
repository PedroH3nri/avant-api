"""Contratos no painel interno contra o Postgres: só a equipe Groone, cada ação com a sua
permissão, e contrato à mão só em network MCM Manage Inventory."""

import uuid
from datetime import UTC, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.model import ConnectionType, Delegation, Network
from fastapi.testclient import TestClient
from sqlalchemy import Engine, text

from tests.conftest import CapturingMailer
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_mfa import _enable


def _networks(engine: Engine, company_id: uuid.UUID) -> dict[str, uuid.UUID]:
    """Uma network MCM Manage Inventory e uma Manage Account da Empresa."""
    now = datetime.now(UTC)
    inventory = Network(
        company_id, "111", ConnectionType.MCM, now, delegation=Delegation.MANAGE_INVENTORY
    )
    account = Network(
        company_id, "222", ConnectionType.MCM, now, delegation=Delegation.MANAGE_ACCOUNT
    )
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        uow.networks.add(inventory)
        uow.networks.add(account)
        uow.commit()
    return {"inventory": inventory.id, "account": account.id}


def test_contract_crud(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    owner = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(owner["active_company_id"])
    networks = _networks(engine, company_id)
    staff = _staff(client, engine)

    listed = staff.get("/api/v1/internal/contracts/networks").json()["items"]
    assert [(item["network"]["network_code"], item["manual"]) for item in listed] == [
        ("111", True),
        ("222", False),
    ]
    assert listed[0]["company"]["id"] == str(company_id) and listed[0]["active"] is None

    created = staff.post(
        "/api/v1/internal/contracts",
        json={"network_id": str(networks["inventory"]), "revshare": "30.5", "notes": "assinado"},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    contract = created.json()
    assert contract["revshare"] == "30.500" and contract["source"] == "manual"
    assert contract["status"] == "active" and contract["notes"] == "assinado"

    blocked = staff.post(
        "/api/v1/internal/contracts",
        json={"network_id": str(networks["account"]), "revshare": 10},
        headers=_csrf(staff),
    )
    assert blocked.status_code == 409
    assert blocked.json()["error"]["code"] == "contract_not_manual"
    invalid = staff.post(
        "/api/v1/internal/contracts",
        json={"network_id": str(networks["inventory"]), "revshare": 101},
        headers=_csrf(staff),
    )
    assert invalid.status_code == 422

    replaced = staff.post(
        "/api/v1/internal/contracts",
        json={"network_id": str(networks["inventory"]), "revshare": 25},
        headers=_csrf(staff),
    ).json()
    history = staff.get(
        "/api/v1/internal/contracts", params={"network_id": str(networks["inventory"])}
    ).json()["items"]
    assert [(item["id"], item["status"]) for item in history] == [
        (replaced["id"], "active"),
        (contract["id"], "ended"),
    ]
    active = staff.get("/api/v1/internal/contracts", params={"status": "active"}).json()["items"]
    assert [item["id"] for item in active] == [replaced["id"]]

    edited = staff.patch(
        f"/api/v1/internal/contracts/{replaced['id']}",
        json={"notes": "aditivo"},
        headers=_csrf(staff),
    )
    assert edited.status_code == 200 and edited.json()["notes"] == "aditivo"
    assert edited.json()["revshare"] == "25.000"
    ended = staff.post(f"/api/v1/internal/contracts/{replaced['id']}/end", headers=_csrf(staff))
    assert ended.status_code == 200 and ended.json()["status"] == "ended"
    again = staff.post(f"/api/v1/internal/contracts/{replaced['id']}/end", headers=_csrf(staff))
    assert again.status_code == 409 and again.json()["error"]["code"] == "contract_ended"

    removed = staff.delete(f"/api/v1/internal/contracts/{contract['id']}", headers=_csrf(staff))
    assert removed.status_code == 204
    missing = staff.get(f"/api/v1/internal/contracts/{contract['id']}")
    assert missing.status_code == 404

    audit = "SELECT action FROM audit_logs WHERE target_type = 'contract'"
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        actions = uow.session.execute(text(audit)).scalars().all()
    assert "contract.started" in actions and "contract.deleted" in actions


def test_contracts_need_staff_and_their_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    denied = client.get("/api/v1/internal/contracts")
    assert denied.status_code == 403 and denied.json()["error"]["code"] == "staff_only"

    staff = _staff(client, engine)
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

    assert support.get("/api/v1/internal/contracts").status_code == 200
    assert support.get("/api/v1/internal/contracts/networks").status_code == 200
    refused = support.post(
        "/api/v1/internal/contracts",
        json={"network_id": str(uuid.uuid4()), "revshare": 10},
        headers=_csrf(support),
    )
    assert refused.status_code == 403
    assert refused.json()["error"]["code"] == "permission_denied"
    removed = support.delete(f"/api/v1/internal/contracts/{uuid.uuid4()}", headers=_csrf(support))
    assert removed.status_code == 403
