"""O painel interno usa os mesmos formatos do painel do cliente, que já trazem a Empresa."""

from avant_api.modules.facebook.dto import (
    FacebookAccountOut,
    FacebookAlertOut,
    FacebookChangeOut,
    FacebookObjectDetailOut,
    FacebookObjectOut,
)

__all__ = [
    "FacebookAccountOut",
    "FacebookAlertOut",
    "FacebookChangeOut",
    "FacebookObjectDetailOut",
    "FacebookObjectOut",
]
