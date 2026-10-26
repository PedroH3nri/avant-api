"""Leitura do pedido HTTP usada por mais de um domínio."""

import ipaddress

from fastapi import Request


def client_info(request: Request) -> tuple[str | None, str | None]:
    """User-Agent e IP. Atrás do nginx, o uvicorn roda com --proxy-headers e o client já é
    o IP real. Socket unix ou cliente de teste não têm IP válido: fica vazio."""
    host = request.client.host if request.client else None
    try:
        ip = str(ipaddress.ip_address(host)) if host else None
    except ValueError:
        ip = None
    return request.headers.get("User-Agent"), ip
