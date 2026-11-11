"""DTOs dos floors que a tag recebe."""

from pydantic import BaseModel


class PublicPriceFloorsOut(BaseModel):
    # Vazio: a tag não leva regra de preço (a tag não manda as keys).
    control_percent: int | None = None
    # ``{bloco: valor de groone_prices}``, na moeda da network (``Content3_Mobile: "1.01"``).
    floors: dict[str, str] = {}
    # ``{bloco: [1º, 2º, 3º]}`` no país de quem pede: a escada de floors da Cascata.
    cascades: dict[str, list[str]] = {}
