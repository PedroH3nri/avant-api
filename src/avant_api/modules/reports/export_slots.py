"""Vagas de exportação por processo: CSV e XLSX grandes pesam na CPU e na memória."""

import threading
from collections.abc import Iterator
from contextlib import contextmanager

from avant_api.app.errors import ExportsBusy

EXPORT_SLOTS = 2
RETRY_AFTER = 10

_exporting = threading.BoundedSemaphore(EXPORT_SLOTS)


@contextmanager
def export_slot() -> Iterator[None]:
    """Ocupa uma vaga enquanto exporta; sem vaga livre, levanta ExportsBusy (503) na hora, sem
    prender a thread do pedido."""
    if not _exporting.acquire(blocking=False):
        raise ExportsBusy(retry_after=RETRY_AFTER)
    try:
        yield
    finally:
        _exporting.release()
