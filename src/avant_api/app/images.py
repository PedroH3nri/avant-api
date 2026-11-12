"""Conversão da imagem da Empresa com o Pillow (adaptador do port ``ImageProcessor``).

Um PNG de 2 MB pode declarar dezenas de megapixels: o teto é 8 MP. O JPEG comum vai até 24 MP e
é lido já reduzido, então foto de celular passa; o progressivo fica nos 8 MP, e o comum com mais
de uma varredura (``jpegtran -scans``) conta como progressivo, porque também fica todo na
memória. JPEG irregular (byte solto entre segmentos, truncado) também fica nos 8 MP. A imagem
é reduzida pelo lado menor antes de virar RGBA e no máximo duas conversões rodam ao mesmo tempo
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

# Marcadores do JPEG: prefixo, zero de enchimento, começo da varredura, fim da imagem e os que
# não têm tamanho; o tamanho de um segmento conta os próprios 2 bytes.
MARKER_PREFIX = 0xFF
STUFFED_ZERO = 0x00
SEGMENT_LENGTH_SIZE = 2
START_OF_SCAN = 0xDA
END_OF_IMAGE = 0xD9
STANDALONE_MARKERS = frozenset({0x01, *range(0xD0, 0xD8)})

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
                    _check_jpeg_size(source, content)
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


def _check_jpeg_size(source: Image.Image, content: bytes) -> None:
    """Recusa o JPEG grande demais antes de ler: 24 MP no comum, 8 MP no progressivo ou no
    comum com várias varreduras."""
    progressive = bool(source.info.get("progressive") or source.info.get("progression"))
    limit = MAX_PIXELS if progressive or _has_many_scans(content) else MAX_JPEG_PIXELS
    if source.width * source.height > limit:
        raise InvalidImage("a imagem tem pixels demais")


def _has_many_scans(content: bytes) -> bool:
    """Diz se há mais de um SOS antes do EOI no fluxo principal (a miniatura do EXIF fica no APP1
    e é pulada); falha fechada: byte fora de lugar, tamanho inválido ou sem EOI contam como mais."""
    scans = 0
    position = 2
    while position + 1 < len(content):
        if content[position] != MARKER_PREFIX:
            return True
        marker = content[position + 1]
        if marker == MARKER_PREFIX:
            position += 1
            continue
        position += 2
        if marker == END_OF_IMAGE:
            return False
        if marker in STANDALONE_MARKERS:
            continue
        if marker == STUFFED_ZERO or position + 2 > len(content):
            return True
        length = int.from_bytes(content[position : position + 2], "big")
        if length < SEGMENT_LENGTH_SIZE:
            return True
        position += length
        if marker == START_OF_SCAN:
            scans += 1
            if scans > 1:
                return True
            position = _end_of_scan_data(content, position)
    return True


def _end_of_scan_data(content: bytes, position: int) -> int:
    """Pula os dados comprimidos da varredura até o próximo marcador (nem FF00 nem RST)."""
    while True:
        position = content.find(b"\xff", position)
        if position < 0 or position + 1 >= len(content):
            return len(content)
        following = content[position + 1]
        if following == 0x00 or following == 0xFF or 0xD0 <= following <= 0xD7:
            position += 1 if following == 0xFF else 2
            continue
        return position
