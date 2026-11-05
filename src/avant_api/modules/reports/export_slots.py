"""Vagas de exportação por processo: CSV e XLSX grandes pesam na CPU e na memória."""

import threading
from collections.abc import Iterator
from contextlib import contextmanager

from avant_api.app.errors import ExportsBusy

EXPORT_SLOTS = 2
WAIT_SECONDS = 10.0
RETRY_AFTER = 10

_exporting = threading.BoundedSemaphore(EXPORT_SLOTS)


@contextmanager
def export_slot(wait: float | None = None) -> Iterator[None]:
    """Ocupa uma vaga enquanto exporta; sem vaga depois da espera, levanta ExportsBusy (503)."""
    if not _exporting.acquire(timeout=WAIT_SECONDS if wait is None else wait):
        raise ExportsBusy(retry_after=RETRY_AFTER)
    try:
        yield
    finally:
        _exporting.release()
