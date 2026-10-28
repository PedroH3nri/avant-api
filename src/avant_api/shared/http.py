"""Leitura do pedido HTTP usada por mais de um domínio."""

import ipaddress

from avant_core.company.models import CompanyImage
from avant_core.identity.models import UserImage
from avant_core.shared.errors import ImageTooLarge
from avant_core.shared.images import IMAGE_MAX_BYTES
from fastapi import Request, Response, status

# A URL da imagem muda a cada imagem nova (?v=), então o navegador pode guardar por um ano.
IMAGE_CACHE = "private, max-age=31536000, immutable"


def client_info(request: Request) -> tuple[str | None, str | None]:
    """User-Agent e IP. Atrás do nginx, o uvicorn roda com --proxy-headers e o client já é
    o IP real. Socket unix ou cliente de teste não têm IP válido: fica vazio."""
    host = request.client.host if request.client else None
    try:
        ip = str(ipaddress.ip_address(host)) if host else None
    except ValueError:
        ip = None
    return request.headers.get("User-Agent"), ip


def image_response(request: Request, image: CompanyImage | UserImage) -> Response:
    """Devolve a imagem com ETag; 304 quando o navegador já tem a mesma."""
    etag = f'"{image.sha256}"'
    headers = {"ETag": etag, "Cache-Control": IMAGE_CACHE}
    if request.headers.get("If-None-Match") == etag:
        return Response(status_code=status.HTTP_304_NOT_MODIFIED, headers=headers)
    return Response(image.content, media_type=image.content_type, headers=headers)


async def image_upload(request: Request) -> bytes:
    """Corpo do PUT da imagem (o arquivo cru); para de ler ao passar do limite."""
    declared = request.headers.get("Content-Length", "")
    if declared.isdigit() and int(declared) > IMAGE_MAX_BYTES:
        raise ImageTooLarge(f"a imagem passa de {IMAGE_MAX_BYTES} bytes")
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > IMAGE_MAX_BYTES:
            raise ImageTooLarge(f"a imagem passa de {IMAGE_MAX_BYTES} bytes")
    return bytes(body)
