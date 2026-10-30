"""Enfileirar tarefas do avant-worker pelo nome, sem importar o pacote dele.

A rota chama depois que o caso de uso confirmou a transação: a tarefa sempre encontra
no banco o que a rota acabou de gravar.
"""

import logging
from dataclasses import dataclass, field
from typing import Any, Protocol

from celery import Celery

log = logging.getLogger("avant.api.tasks")

SYNC_NETWORK = "avant.gam.sync_network"
REFRESH_REPORT_PREVIEW = "avant.default.refresh_report_preview"


class TaskQueue(Protocol):
    def send(self, name: str, *args: Any) -> None:
        """Agenda uma tarefa no worker pelo nome."""
        ...


class CeleryQueue:
    """Só publica no RabbitMQ; o resultado fica com o worker."""

    def __init__(self, broker_url: str) -> None:
        self._app = Celery("avant-api", broker=broker_url)
        self._app.conf.update(task_serializer="json", broker_connection_retry_on_startup=True)

    def send(self, name: str, *args: Any) -> None:
        """Sem RabbitMQ, a rota não falha: o pedido já está gravado e o agendador do worker
        passa pela network no próximo ciclo. Fica o erro no log (e o alerta)."""
        queue = name.split(".")[1]
        try:
            self._app.send_task(
                name,
                args=list(args),
                queue=queue,
                ignore_result=True,
                retry=True,
                retry_policy={"max_retries": 2, "interval_start": 0, "interval_step": 0.5},
            )
        except Exception:
            log.exception("não foi possível enfileirar a tarefa", extra={"task": name})
            return
        log.info("tarefa enfileirada", extra={"task": name})


@dataclass
class RecordingQueue:
    """Local e testes: guarda o que seria enfileirado."""

    sent: list[tuple[str, tuple[Any, ...]]] = field(default_factory=list)

    def send(self, name: str, *args: Any) -> None:
        """Guarda a tarefa em memória, para os testes conferirem."""
        self.sent.append((name, args))
