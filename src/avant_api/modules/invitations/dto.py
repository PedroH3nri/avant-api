"""DTOs de entrada e saída do domínio invitations. Datas sempre em ISO 8601 UTC."""

import uuid

from pydantic import BaseModel, EmailStr


class InviteIn(BaseModel):
    email: EmailStr
    role_id: uuid.UUID
