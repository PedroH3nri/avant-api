"""DTOs de entrada e saída do domínio api_keys. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.access.api_keys import MAX_DAYS, ApiKeyView
from pydantic import BaseModel, Field

from avant_api.shared.dto import UserOut


class ApiKeyOut(BaseModel):
    id: uuid.UUID
    name: str
    # Para reconhecer: avk_{prefix}...
    prefix: str
    permissions: list[str]
    owner: UserOut
    created_at: datetime
    expires_at: datetime
    last_used_at: datetime | None
    revoked_at: datetime | None

    @classmethod
    def of(cls, view: ApiKeyView) -> "ApiKeyOut":
        """Monta a chave de API com o dono, sem o token."""
        key, owner = view.key, view.owner
        return cls(
            id=key.id,
            name=key.name,
            prefix=key.prefix,
            permissions=list(key.permissions),
            owner=UserOut(id=owner.id, email=owner.email, name=owner.name, locale=owner.locale),
            created_at=key.created_at,
            expires_at=key.expires_at,
            last_used_at=key.last_used_at,
            revoked_at=key.revoked_at,
        )


class ApiKeyCreatedOut(ApiKeyOut):
    # Aparece só nesta resposta.
    token: str


class ApiKeyIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    permissions: list[str] = Field(min_length=1, max_length=50)
    expires_in_days: int = Field(default=MAX_DAYS, ge=1, le=MAX_DAYS)
