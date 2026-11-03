"""Documentos do cliente Manage Inventory e observações da equipe Groone, contra o Postgres."""

import uuid
from datetime import UTC, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.networks.enums import ConnectionType, Delegation
from avant_core.gam.networks.models import Network
from avant_core.ports import Notice
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_commissions import _support
from tests.test_internal import _staff

PDF = b"%PDF-1.7\n" + b"0" * 200
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 200


def _manage_inventory(engine: Engine, company_id: uuid.UUID) -> None:
    """Uma network Manage Inventory, que faz a Empresa precisar enviar documentos."""
    with SqlAlchemyUnitOfWork(engine, company_id=company_id) as uow:
        network = Network(company_id, "7070", ConnectionType.MCM, datetime.now(UTC), "Rede MI")
        network.delegation = Delegation.MANAGE_INVENTORY
        uow.networks.add(network)
        uow.commit()


def _send(client: TestClient, kind: str, name: str, content: bytes) -> dict:  # type: ignore[type-arg]
    """Envia o arquivo cru no corpo do PUT e devolve a resposta em JSON."""
    response = client.put(
        f"/api/v1/company/documents/{kind}",
        params={"name": name},
        content=content,
        headers={**_csrf(client), "Content-Type": "application/octet-stream"},
    )
    return {"http": response.status_code, **response.json()}


def test_client_sends_documents_and_staff_reviews(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = uuid.UUID(me["companies"][0]["id"])
    assert client.get("/api/v1/company/documents").json() == {"required": False, "documents": []}
    refused = _send(client, "identity", "rg.pdf", PDF)
    assert refused["http"] == 409 and refused["error"]["code"] == "documents_not_required"

    _manage_inventory(engine, company_id)
    invalid = _send(client, "identity", "rg.gif", b"GIF89a" + b"0" * 50)
    assert invalid["http"] == 422 and invalid["error"]["code"] == "invalid_document"
    too_large = _send(client, "identity", "rg.pdf", PDF + b"0" * (5 * 1024 * 1024))
    assert too_large["http"] == 413 and too_large["error"]["code"] == "document_too_large"
    sent = _send(client, "identity", "Identidade Ação.pdf", PDF)
    assert sent["http"] == 200
    assert (sent["kind"], sent["content_type"]) == ("identity", "application/pdf")
    assert _send(client, "address", "conta.png", PNG)["http"] == 200
    overview = client.get("/api/v1/company/documents").json()
    assert overview["required"] is True
    assert {item["kind"]: item["status"] for item in overview["documents"]} == {
        "identity": "pending",
        "address": "pending",
    }
    mine = client.get("/api/v1/company/documents/identity/file")
    assert mine.status_code == 200 and mine.content == PDF
    assert mine.headers["cache-control"] == "private, no-store"
    assert "Identidade%20A%C3%A7%C3%A3o.pdf" in mine.headers["content-disposition"]

    staff = _staff(client, engine)
    base = f"/api/v1/internal/clients/{company_id}/documents"
    listed = staff.get(base)
    assert listed.status_code == 200, listed.text
    assert len(listed.json()["documents"]) == 2
    assert staff.get(f"{base}/address/file").content == PNG
    approved = staff.post(f"{base}/identity/approve", headers=_csrf(staff))
    assert approved.status_code == 200 and approved.json()["status"] == "approved"
    assert approved.json()["reviewed_by"] is not None
    again = staff.post(f"{base}/identity/approve", headers=_csrf(staff))
    assert again.status_code == 409 and again.json()["error"]["code"] == "document_not_reviewable"
    rejected = staff.post(
        f"{base}/address/reject",
        json={"reason": "A conta está no nome de outra pessoa."},
        headers=_csrf(staff),
    )
    assert rejected.status_code == 200 and rejected.json()["status"] == "rejected"
    assert [notice for _, notice in mailer.notices[-2:]] == [
        Notice.DOCUMENT_APPROVED,
        Notice.DOCUMENT_REJECTED,
    ]
    locked = _send(client, "identity", "rg.pdf", PDF)
    assert locked["http"] == 409 and locked["error"]["code"] == "document_already_approved"
    resent = _send(client, "address", "conta.pdf", PDF)
    assert resent["http"] == 200 and resent["status"] == "pending"
    assert resent["rejection_reason"] is None

    support = _support(client, staff, mailer)
    assert support.get(base).status_code == 403
    assert client.get(base).status_code == 403


def test_staff_writes_notes_and_only_author_or_manager_changes(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = me["companies"][0]["id"]
    staff = _staff(client, engine)
    base = f"/api/v1/internal/clients/{company_id}/notes"
    short = staff.post(base, json={"message": "oi"}, headers=_csrf(staff))
    assert short.status_code == 422
    written = staff.post(
        base, json={"message": "Ligação de boas-vindas feita."}, headers=_csrf(staff)
    )
    assert written.status_code == 204, written.text
    (note,) = staff.get(base).json()["items"]
    assert note["author"]["name"] == "Admin" and note["editable"] is True
    assert note["editor"] is None and note["edited_at"] is None

    edited = staff.patch(
        f"{base}/{note['id']}",
        json={"message": "Ligação feita; volta em dezembro."},
        headers=_csrf(staff),
    )
    assert edited.status_code == 204, edited.text
    (note,) = staff.get(base).json()["items"]
    assert note["message"] == "Ligação feita; volta em dezembro."
    assert note["editor"]["name"] == "Admin" and note["edited_at"] is not None

    support = _support(client, staff, mailer)
    assert support.get(base).status_code == 403
    assert client.get(base).status_code == 403
    deleted = staff.delete(f"{base}/{note['id']}", headers=_csrf(staff))
    assert deleted.status_code == 204
    assert staff.get(base).json()["items"] == []
    missing = staff.delete(f"{base}/{uuid.uuid4()}", headers=_csrf(staff))
    assert missing.status_code == 404
