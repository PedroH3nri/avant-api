"""Envio de e-mail.

Com ``RESEND_API_KEY``, os e-mails saem pelo Resend (domínio avant.groone.com). Sem a
chave (local e testes), o LogMailer só registra o envio, com o link.

O envio acontece depois do commit. Se o Resend falhar, o convite continua pendente e
pode ser reenviado (e o link de nova senha pode ser pedido de novo): a falha vai para o
log e para a métrica
``avant_mail_failures_total``, e a requisição não quebra.
"""

import html
import logging
from dataclasses import dataclass

import httpx
from avant_core.company.domain import InvitationKind
from avant_core.ports import Notice
from prometheus_client import Counter

log = logging.getLogger("avant.mail")

MAIL_SENT = Counter("avant_mail_sent_total", "E-mails enviados", ["template"])
MAIL_FAILURES = Counter("avant_mail_failures_total", "E-mails que não saíram", ["template"])

RESEND_URL = "https://api.resend.com/emails"


@dataclass(frozen=True)
class Message:
    subject: str
    text: str
    html: str


# Textos do convite por idioma. {company} só aparece no convite de equipe.
_INVITE = {
    "pt": {
        "subject_team": "Convite para {company} no Groone Avant",
        "subject_owner": "Seu acesso ao Groone Avant",
        "intro_team": "Você foi convidado para a equipe de {company} no Groone Avant.",
        "intro_owner": "A Groone liberou seu acesso ao Groone Avant. Crie sua Empresa.",
        "button": "Aceitar convite",
        "expires": "O link vale por 24 horas. Se não esperava o convite, ignore este e-mail.",
    },
    "en": {
        "subject_team": "Invitation to {company} on Groone Avant",
        "subject_owner": "Your Groone Avant access",
        "intro_team": "You have been invited to join {company} on Groone Avant.",
        "intro_owner": "Groone has given you access to Groone Avant. Create your company to start.",
        "button": "Accept invitation",
        "expires": "The link is valid for 24 hours. Not expecting it? Ignore this email.",
    },
    "es": {
        "subject_team": "Invitación a {company} en Groone Avant",
        "subject_owner": "Tu acceso a Groone Avant",
        "intro_team": "Te invitaron al equipo de {company} en Groone Avant.",
        "intro_owner": "Groone habilitó tu acceso a Groone Avant. Crea tu empresa para empezar.",
        "button": "Aceptar invitación",
        "expires": "El enlace vale por 24 horas. Si no lo esperabas, ignora este correo.",
    },
}


_RESET = {
    "pt": {
        "subject": "Redefinir sua senha do Groone Avant",
        "intro": "Recebemos um pedido para redefinir a senha da sua conta no Groone Avant.",
        "button": "Redefinir senha",
        "expires": "O link vale por 1 hora e só uma vez. Se não pediu, ignore este e-mail.",
    },
    "en": {
        "subject": "Reset your Groone Avant password",
        "intro": "We received a request to reset the password of your Groone Avant account.",
        "button": "Reset password",
        "expires": "The link is valid for 1 hour, once. Didn't ask for it? Ignore this email.",
    },
    "es": {
        "subject": "Restablecer tu contraseña de Groone Avant",
        "intro": "Recibimos un pedido para restablecer la contraseña de tu cuenta de Groone Avant.",
        "button": "Restablecer contraseña",
        "expires": "El enlace vale 1 hora y una sola vez. Si no lo pediste, ignora este correo.",
    },
}

# Avisos sem botão. O último parágrafo diz o que fazer se não foi a pessoa.
_NOTICES: dict[str, dict[Notice, tuple[str, str]]] = {
    "pt": {
        Notice.PASSWORD_CHANGED: (
            "Sua senha do Groone Avant foi trocada",
            "A senha da sua conta no Groone Avant acabou de ser trocada.",
        ),
        Notice.GOOGLE_LINKED: (
            "Conta Google ligada ao Groone Avant",
            "Uma conta Google foi ligada à sua conta no Groone Avant. Já dá para entrar com ela.",
        ),
        Notice.MFA_RESET: (
            "Seu 2FA do Groone Avant foi zerado",
            "A equipe Groone zerou a verificação em duas etapas da sua conta. Configure de novo "
            "no próximo login.",
        ),
    },
    "en": {
        Notice.PASSWORD_CHANGED: (
            "Your Groone Avant password was changed",
            "The password of your Groone Avant account was just changed.",
        ),
        Notice.GOOGLE_LINKED: (
            "Google account linked to Groone Avant",
            "A Google account was linked to your Groone Avant account. You can sign in with it.",
        ),
        Notice.MFA_RESET: (
            "Your Groone Avant 2FA was reset",
            "The Groone team reset the two-step verification of your account. Set it up again "
            "on your next sign-in.",
        ),
    },
    "es": {
        Notice.PASSWORD_CHANGED: (
            "Tu contraseña de Groone Avant fue cambiada",
            "La contraseña de tu cuenta de Groone Avant acaba de cambiar.",
        ),
        Notice.GOOGLE_LINKED: (
            "Cuenta de Google vinculada a Groone Avant",
            "Se vinculó una cuenta de Google a tu cuenta de Groone Avant. Ya puedes usarla.",
        ),
        Notice.MFA_RESET: (
            "Tu 2FA de Groone Avant fue restablecido",
            "El equipo de Groone restableció la verificación en dos pasos de tu cuenta. "
            "Configúrala de nuevo en el próximo inicio de sesión.",
        ),
    },
}

_NOT_YOU = {
    "pt": "Se não foi você, troque a senha e fale com o suporte da Groone.",
    "en": "If this wasn't you, change your password and contact Groone support.",
    "es": "Si no fuiste tú, cambia la contraseña y habla con el soporte de Groone.",
}


def invitation_link(base_url: str, token: str) -> str:
    return f"{base_url.rstrip('/')}/convite/{token}"


def reset_link(base_url: str, token: str) -> str:
    return f"{base_url.rstrip('/')}/redefinir-senha/{token}"


def render_invitation(
    *, link: str, kind: InvitationKind, company_name: str | None, locale: str
) -> Message:
    t = _INVITE.get(locale, _INVITE["pt"])
    which = "team" if kind is InvitationKind.TEAM else "owner"
    company = company_name or ""
    subject = t[f"subject_{which}"].format(company=company)
    intro = t[f"intro_{which}"].format(company=company)
    return _with_button(subject, intro, t["button"], link, t["expires"])


def render_password_reset(*, link: str, locale: str) -> Message:
    t = _RESET.get(locale, _RESET["pt"])
    return _with_button(t["subject"], t["intro"], t["button"], link, t["expires"])


def render_notice(*, notice: Notice, locale: str) -> Message:
    lang = locale if locale in _NOTICES else "pt"
    subject, intro = _NOTICES[lang][notice]
    footer = _NOT_YOU[lang]
    e = html.escape
    body = (
        _OPEN
        + f'<p style="font-size:15px;margin:0 0 24px">{e(intro)}</p>'
        + f'<p style="font-size:13px;color:#666666;margin:0">{e(footer)}</p></div>'
    )
    return Message(subject=subject, text=f"{intro}\n\n{footer}\n", html=body)


# Visual do DESIGN.md: Geist, quase monocromático, botão preto.
_OPEN = (
    '<div style="font-family:Geist,-apple-system,Segoe UI,Helvetica,Arial,sans-serif;'
    'color:#171717;max-width:480px;margin:0 auto;padding:32px 24px;line-height:1.5">'
    '<p style="font-weight:600;font-size:14px;margin:0 0 24px">Groone Avant</p>'
)


def _with_button(subject: str, intro: str, button: str, link: str, footer: str) -> Message:
    text = f"{intro}\n\n{button}: {link}\n\n{footer}\n"
    e = html.escape
    body = (
        _OPEN
        + f'<p style="font-size:15px;margin:0 0 24px">{e(intro)}</p>'
        + f'<p style="margin:0 0 24px"><a href="{e(link)}" style="display:inline-block;'
        + "background:#171717;color:#ffffff;text-decoration:none;padding:10px 16px;"
        + f'border-radius:6px;font-size:14px;font-weight:500">{e(button)}</a></p>'
        + f'<p style="font-size:13px;color:#666666;margin:0 0 8px">{e(footer)}</p>'
        + f'<p style="font-size:12px;color:#666666;margin:0;word-break:break-all">{e(link)}</p>'
        + "</div>"
    )
    return Message(subject=subject, text=text, html=body)


class LogMailer:
    def __init__(self, *, base_url: str, show_links: bool) -> None:
        self._base_url = base_url
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
            extra["link"] = invitation_link(self._base_url, token)
        log.info("convite enviado", extra=extra)

    def send_password_reset(self, *, to: str, token: str, locale: str) -> None:
        extra: dict[str, str] = {"to": to, "locale": locale}
        if self._show_links:
            extra["link"] = reset_link(self._base_url, token)
        log.info("link de nova senha enviado", extra=extra)

    def send_notice(self, *, to: str, notice: Notice, locale: str) -> None:
        log.info("aviso enviado", extra={"to": to, "notice": notice.value, "locale": locale})


class ResendMailer:
    """Cliente mínimo da API do Resend (POST /emails)."""

    def __init__(
        self,
        *,
        api_key: str,
        sender: str,
        base_url: str,
        client: httpx.Client | None = None,
    ) -> None:
        self._sender = sender
        self._base_url = base_url
        self._client = client or httpx.Client(timeout=10.0)
        self._headers = {"Authorization": f"Bearer {api_key}"}

    def send_invitation(
        self,
        *,
        to: str,
        token: str,
        kind: InvitationKind,
        company_name: str | None,
        locale: str,
    ) -> None:
        msg = render_invitation(
            link=invitation_link(self._base_url, token),
            kind=kind,
            company_name=company_name,
            locale=locale,
        )
        self._send(to=to, msg=msg, template="invitation", extra={"kind": kind.value})

    def send_password_reset(self, *, to: str, token: str, locale: str) -> None:
        msg = render_password_reset(link=reset_link(self._base_url, token), locale=locale)
        self._send(to=to, msg=msg, template="password_reset", extra={})

    def send_notice(self, *, to: str, notice: Notice, locale: str) -> None:
        msg = render_notice(notice=notice, locale=locale)
        self._send(to=to, msg=msg, template=f"notice_{notice.value}", extra={})

    def _send(self, *, to: str, msg: Message, template: str, extra: dict[str, str]) -> None:
        payload = {
            "from": self._sender,
            "to": [to],
            "subject": msg.subject,
            "text": msg.text,
            "html": msg.html,
        }
        # Uma nova tentativa em erro de rede, 429 ou 5xx; erro 4xx é configuração.
        for attempt in (1, 2):
            try:
                r = self._client.post(RESEND_URL, json=payload, headers=self._headers)
            except httpx.HTTPError as exc:
                if attempt == 2:
                    self._failed(to, template, extra, str(exc))
                    return
                continue
            if r.status_code < 300:
                MAIL_SENT.labels(template).inc()
                log.info(
                    "e-mail enviado",
                    extra={"to": to, "template": template, "id": r.json().get("id"), **extra},
                )
                return
            if attempt == 2 or not (r.status_code == 429 or r.status_code >= 500):
                self._failed(to, template, extra, f"HTTP {r.status_code}: {r.text[:300]}")
                return

    def _failed(self, to: str, template: str, extra: dict[str, str], reason: str) -> None:
        MAIL_FAILURES.labels(template).inc()
        log.error(
            "e-mail não saiu", extra={"to": to, "template": template, "reason": reason, **extra}
        )
