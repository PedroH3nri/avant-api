"""Métricas do Prometheus com vários processos do uvicorn (modo multiprocesso)."""

import os
import subprocess
import sys
from pathlib import Path

from avant_api.modules.health.metrics import exposition

COUNT_ONE_REQUEST = (
    "from avant_api.app.middleware import REQUESTS; "
    "REQUESTS.labels('GET', '/api/v1/health', '200').inc()"
)


def test_metrics_add_up_every_process(tmp_path: Path) -> None:
    environment = {**os.environ, "PROMETHEUS_MULTIPROC_DIR": str(tmp_path)}
    for _ in range(2):
        subprocess.run([sys.executable, "-c", COUNT_ONE_REQUEST], env=environment, check=True)
    body = exposition(str(tmp_path)).decode()
    expected = 'avant_http_requests_total{method="GET",route="/api/v1/health",status="200"} 2.0'
    assert expected in body


def test_metrics_of_a_single_process() -> None:
    assert b"avant_http_requests_total" in exposition(None)
