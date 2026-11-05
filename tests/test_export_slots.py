import threading
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.errors import ExportsBusy
from avant_api.modules.reports import export_slots
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_reports import _metrics
from tests.test_saved_reports import _report


def test_export_slots_refuse_a_third_export_while_two_run(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(export_slots, "_exporting", threading.BoundedSemaphore(2))
    with (
        export_slots.export_slot(),
        export_slots.export_slot(),
        pytest.raises(ExportsBusy) as refused,
        export_slots.export_slot(wait=0.01),
    ):
        pass
    assert refused.value.retry_after == export_slots.RETRY_AFTER
    with export_slots.export_slot(wait=0.01):
        pass


def test_busy_export_answers_503_with_retry_after(
    client: TestClient,
    engine: Engine,
    mailer: CapturingMailer,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    report = client.post("/api/v1/reports", json=_report(), headers=_csrf(client)).json()
    monkeypatch.setattr(export_slots, "_exporting", threading.BoundedSemaphore(1))
    monkeypatch.setattr(export_slots, "WAIT_SECONDS", 0.01)
    with export_slots.export_slot():
        busy = client.get(f"/api/v1/reports/{report['id']}/export")
    assert busy.status_code == 503, busy.text
    assert busy.json()["error"]["code"] == "exports_busy"
    assert busy.headers["Retry-After"] == str(export_slots.RETRY_AFTER)
