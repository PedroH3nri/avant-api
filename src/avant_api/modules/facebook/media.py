"""Corpo do envio de imagem ou vídeo de anúncio: o arquivo cru, lido em pedaços até 100 MB."""

from fastapi import Request

from avant_api.app.errors import FacebookMediaTooLarge

MEGABYTE = 1024 * 1024
MAX_MEDIA_BYTES = 100 * MEGABYTE


async def media_upload(request: Request) -> bytes:
    """O arquivo do corpo do POST; para de ler ao passar do limite dos vídeos (o core confere
    o limite de cada tipo)."""
    message = f"o arquivo passa de {MAX_MEDIA_BYTES // MEGABYTE} MB"
    declared = request.headers.get("Content-Length", "")
    if declared.isdigit() and int(declared) > MAX_MEDIA_BYTES:
        raise FacebookMediaTooLarge(message)
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > MAX_MEDIA_BYTES:
            raise FacebookMediaTooLarge(message)
    return bytes(body)
