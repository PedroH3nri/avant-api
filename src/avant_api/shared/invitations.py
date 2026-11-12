"""Apoio dos convites de equipe e de dono: o e-mail que não sai vira 503."""

from collections.abc import Iterator
from contextlib import contextmanager

from avant_core.ports import MailNotSent

from avant_api.app.errors import InvitationMailNotSent


@contextmanager
def invitation_mail() -> Iterator[None]:
    """Troca o ``MailNotSent`` do envio do convite pelo 503 com a mensagem fixa da API."""
    try:
        yield
    except MailNotSent as error:
        raise InvitationMailNotSent() from error
