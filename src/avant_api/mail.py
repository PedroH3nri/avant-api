"""Envio de e-mail.

O adaptador do Resend (domínio avant.groone.com) entra no próximo passo. Por
enquanto o LogMailer registra o envio; em local e nos testes, com o link.
"""

import logging

from avant_core.company.domain import InvitationKind

log = logging.getLogger("avant.mail")


class LogMailer:
    def __init__(self, *, base_url: str, show_links: bool) -> None:
        self._base_url = base_url.rstrip("/")
        self._show_links = show_links

    def send_invitation(
        self,
        *,
        to: str,
        token: str,
        kind: InvitationKind,
        company_name: str | None,
        locale: str,
    ) -> None:
        extra: dict[str, str | None] = {
            "to": to,
            "kind": kind.value,
            "company": company_name,
            "locale": locale,
        }
        if self._show_links:
            extra["link"] = f"{self._base_url}/convite/{token}"
        log.info("convite enviado", extra=extra)
