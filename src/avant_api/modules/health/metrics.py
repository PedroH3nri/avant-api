"""Exposição das métricas do Prometheus, num processo só ou somando todos os do uvicorn."""

from prometheus_client import CollectorRegistry, generate_latest
from prometheus_client.multiprocess import MultiProcessCollector


def exposition(multiproc_dir: str | None) -> bytes:
    """As métricas no formato do Prometheus; com o diretório do modo multiprocesso, soma os
    arquivos de todos os processos, para a coleta não cair num processo qualquer."""
    if multiproc_dir is None:
        return generate_latest()
    registry = CollectorRegistry()
    MultiProcessCollector(registry, path=multiproc_dir)  # type: ignore[no-untyped-call]
    return generate_latest(registry)
