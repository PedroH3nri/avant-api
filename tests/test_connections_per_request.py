"""Quantas conexões do pool um pedido de relatório usa: cada uma é uma transação a mais."""

import uuid
from collections.abc import Callable
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine, event
from sqlalchemy.pool import Pool

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_reports import _day, _metrics
from tests.test_saved_reports import _report


def _checkouts(call: Callable[[], Any]) -> int:
    """Faz o pedido e conta as conexões tiradas do pool."""
    taken: list[int] = []

    def count(*args: object) -> None:
        """Conta uma conexão tirada do pool."""
        taken.append(1)

    event.listen(Pool, "checkout", count)
    try:
        response = call()
    finally:
        event.remove(Pool, "checkout", count)
    assert response.status_code == 200, response.text
    return len(taken)


def test_report_requests_use_few_connections(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    report = client.post("/api/v1/reports", json=_report(), headers=_csrf(client)).json()

    def query() -> Any:
        """Uma consulta avulsa por site."""
        return client.post("/api/v1/reports/query", json=_day(["site"]), headers=_csrf(client))

    def export() -> Any:
        """A exportação do relatório salvo."""
        return client.get(f"/api/v1/reports/{report['id']}/export")

    assert _checkouts(query) <= 2
    assert _checkouts(export) <= 5
