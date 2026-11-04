"""Conversão da imagem da Empresa com o Pillow (adaptador do port ``ImageProcessor``).

Um PNG de 2 MB pode declarar dezenas de megapixels: o teto é 8 MP. O JPEG comum vai até 24 MP e
é lido já reduzido, então foto de celular passa; o progressivo fica nos 8 MP. A imagem é
reduzida pelo lado menor antes de virar RGBA e no máximo duas conversões rodam ao mesmo tempo
em cada processo.
"""

import threading
from io import BytesIO

from avant_core.shared.errors import InvalidImage
from PIL import Image, ImageOps, UnidentifiedImageError

ACCEPTED_FORMATS = frozenset({"PNG", "JPEG", "WEBP"})
MAX_PIXELS = 8_000_000
# Foto de celular (até 24 MP) é lida já reduzida; o JPEG progressivo guarda a imagem inteira na
# memória mesmo assim, por isso fica com o teto comum.
MAX_JPEG_PIXELS = 24_000_000
WEBP_QUALITY = 90
# O lado menor é reduzido até este múltiplo do lado final antes do corte, para não converter tudo.
SHRINK_FACTOR = 4

_converting = threading.BoundedSemaphore(2)


class PillowImageProcessor:
    """Corta a imagem no quadrado do centro e grava em WebP."""

    def square_webp(self, content: bytes, side: int) -> bytes:
        """Abre PNG, JPEG ou WebP, respeita a rotação do EXIF e devolve WebP side x side."""
        with _converting:
            return self._square_webp(content, side)

    def _square_webp(self, content: bytes, side: int) -> bytes:
        """Reduz a imagem pelo lado menor até perto do lado final, corta no quadrado do centro
        e grava; o JPEG já é lido reduzido (``draft``), por isso aceita foto de celular."""
        target = side * SHRINK_FACTOR
        try:
            with Image.open(BytesIO(content)) as source:
                if source.format not in ACCEPTED_FORMATS:
                    raise InvalidImage(f"formato {source.format} não aceito")
                if source.format == "JPEG":
                    _check_jpeg_size(source)
                    source.draft("RGB", (target, target))
                width, height = source.size
                if width * height > MAX_PIXELS:
                    raise InvalidImage("a imagem tem pixels demais")
                image = source.convert("RGBA") if source.mode in ("P", "1") else source
                upright = ImageOps.exif_transpose(image)
                scale = target / min(upright.size)
                if scale < 1:
                    reduced = (round(upright.width * scale), round(upright.height * scale))
                    upright = upright.resize(reduced, Image.Resampling.LANCZOS)
                upright = upright.convert("RGBA")
        except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as error:
            raise InvalidImage("não foi possível abrir a imagem") from error
        square = ImageOps.fit(upright, (side, side), method=Image.Resampling.LANCZOS)
        output = BytesIO()
        square.save(output, format="WEBP", quality=WEBP_QUALITY)
        return output.getvalue()


def _check_jpeg_size(source: Image.Image) -> None:
    """Recusa o JPEG grande demais antes de ler: 24 MP no comum, 8 MP no progressivo."""
    progressive = bool(source.info.get("progressive") or source.info.get("progression"))
    limit = MAX_PIXELS if progressive else MAX_JPEG_PIXELS
    if source.width * source.height > limit:
        raise InvalidImage("a imagem tem pixels demais")
