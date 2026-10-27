"""Conversão da imagem da Empresa com o Pillow (adaptador do port ``ImageProcessor``)."""

from io import BytesIO

from avant_core.shared.errors import InvalidImage
from PIL import Image, ImageOps, UnidentifiedImageError

ACCEPTED_FORMATS = frozenset({"PNG", "JPEG", "WEBP"})
MAX_PIXELS = 40_000_000
WEBP_QUALITY = 90


class PillowImageProcessor:
    """Corta a imagem no quadrado do centro e grava em WebP."""

    def square_webp(self, content: bytes, side: int) -> bytes:
        """Abre PNG, JPEG ou WebP, respeita a rotação do EXIF e devolve WebP side x side."""
        try:
            with Image.open(BytesIO(content)) as source:
                if source.format not in ACCEPTED_FORMATS:
                    raise InvalidImage(f"formato {source.format} não aceito")
                width, height = source.size
                if width * height > MAX_PIXELS:
                    raise InvalidImage("a imagem tem pixels demais")
                upright = ImageOps.exif_transpose(source).convert("RGBA")
        except (UnidentifiedImageError, OSError, Image.DecompressionBombError) as error:
            raise InvalidImage("não foi possível abrir a imagem") from error
        square = ImageOps.fit(upright, (side, side), method=Image.Resampling.LANCZOS)
        output = BytesIO()
        square.save(output, format="WEBP", quality=WEBP_QUALITY)
        return output.getvalue()
