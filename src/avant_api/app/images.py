"""Conversão da imagem da Empresa com o Pillow (adaptador do port ``ImageProcessor``).

Um PNG de 2 MB pode declarar dezenas de megapixels: o teto é 8 MP, a imagem é reduzida antes de
converter para RGBA e no máximo duas conversões rodam ao mesmo tempo em cada processo.
"""

import threading
from io import BytesIO

from avant_core.shared.errors import InvalidImage
from PIL import Image, ImageOps, UnidentifiedImageError

ACCEPTED_FORMATS = frozenset({"PNG", "JPEG", "WEBP"})
MAX_PIXELS = 8_000_000
WEBP_QUALITY = 90
# A imagem é reduzida até este múltiplo do lado final antes do corte, para não converter tudo.
SHRINK_FACTOR = 4

_converting = threading.BoundedSemaphore(2)


class PillowImageProcessor:
    """Corta a imagem no quadrado do centro e grava em WebP."""

    def square_webp(self, content: bytes, side: int) -> bytes:
        """Abre PNG, JPEG ou WebP, respeita a rotação do EXIF e devolve WebP side x side."""
        with _converting:
            return self._square_webp(content, side)

    def _square_webp(self, content: bytes, side: int) -> bytes:
        """Reduz a imagem para perto do lado final, corta no quadrado do centro e grava."""
        try:
            with Image.open(BytesIO(content)) as source:
                if source.format not in ACCEPTED_FORMATS:
                    raise InvalidImage(f"formato {source.format} não aceito")
                width, height = source.size
                if width * height > MAX_PIXELS:
                    raise InvalidImage("a imagem tem pixels demais")
                source.draft("RGB", (side * SHRINK_FACTOR, side * SHRINK_FACTOR))
                source.thumbnail((side * SHRINK_FACTOR, side * SHRINK_FACTOR))
                upright = ImageOps.exif_transpose(source).convert("RGBA")
        except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as error:
            raise InvalidImage("não foi possível abrir a imagem") from error
        square = ImageOps.fit(upright, (side, side), method=Image.Resampling.LANCZOS)
        output = BytesIO()
        square.save(output, format="WEBP", quality=WEBP_QUALITY)
        return output.getvalue()
