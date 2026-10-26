"""DTOs de entrada e saída do domínio internal/staff. Datas sempre em ISO 8601 UTC."""

import uuid

from pydantic import BaseModel, EmailStr


class StaffInviteIn(BaseModel):
    email: EmailStr
    role_id: uuid.UUID
