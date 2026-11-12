"""Quantas conexões do pool um pedido usa, e que as respostas em streaming (SSE e download)
devolvem a conexão antes de mandar o corpo."""

import json
import uuid
from collections.abc import AsyncIterator, Callable
from dataclasses import dataclass, field
from typing import Any

from fastapi.testclient import TestClient
from sqlalchemy import Engine, event
from sqlalchemy.pool import Pool, QueuePool

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


def _checked_out(engine: Engine) -> int:
    """Quantas conexões do pool estão emprestadas agora."""
    pool = engine.pool
    assert isinstance(pool, QueuePool)
    return pool.checkedout()


@dataclass
class PoolWatchingEvents:
    """Fonte de eventos que anota quantas conexões estão fora do pool enquanto o SSE corre."""

    engine: Engine
    checked_out: list[int] = field(default_factory=list)

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Entrega dois eventos e anota o pool antes de cada um."""
        for network_id in ("n1", "n2"):
            self.checked_out.append(_checked_out(self.engine))
            yield json.dumps({"type": "network.updated", "data": {"network_id": network_id}})


def test_event_stream_holds_no_connection(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    source = PoolWatchingEvents(engine)
    client.app.state.services.events = source  # type: ignore[attr-defined]
    with client.stream("GET", "/api/v1/events") as response:
        assert response.status_code == 200
        body = "".join(response.iter_text())
    assert body.count("event: network.updated") == 2
    assert source.checked_out == [0, 0]
    assert _checked_out(engine) == 0


def test_downloads_give_the_connection_back(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    _metrics(engine, uuid.UUID(me["active_company_id"]))
    report = client.post("/api/v1/reports", json=_report(), headers=_csrf(client)).json()
    downloads = [
        lambda: client.post(
            "/api/v1/reports/query/export", json=_day(["site"]), headers=_csrf(client)
        ),
        lambda: client.get(f"/api/v1/reports/{report['id']}/export"),
        lambda: client.get(f"/api/v1/reports/{report['id']}/export", params={"format": "xlsx"}),
    ]
    for download in downloads:
        assert _checkouts(download) > 0
        assert _checked_out(engine) == 0
