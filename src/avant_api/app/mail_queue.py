"""Adaptador do port ``MailQueue`` do avant-core: os e-mails da conta saem pelo worker."""

from avant_api.app.errors import QueueUnavailable
from avant_api.app.tasks import REQUEST_PASSWORD_RESET, TaskQueue

MAIL_QUEUE_RETRY_AFTER = 30


class TaskMailQueue:
    """Agenda os e-mails na fila ``mail`` do worker; só o e-mail da pessoa vai na fila."""

    def __init__(self, tasks: TaskQueue) -> None:
        self._tasks = tasks

    def request_password_reset(self, *, email: str) -> None:
        """Agenda no worker o pedido de nova senha; com a fila fora do ar, responde 503 (a mesma
        resposta exista ou não a conta)."""
        if not self._tasks.send(REQUEST_PASSWORD_RESET, email):
            raise QueueUnavailable(retry_after=MAIL_QUEUE_RETRY_AFTER)
