"""DTOs de entrada e saída do domínio account. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class ForgotPasswordIn(BaseModel):
    email: EmailStr


class ResetPasswordIn(BaseModel):
    token: str = Field(min_length=10, max_length=200)
    password: str = Field(min_length=1, max_length=1024)
    # Só quando a pessoa tem 2FA ligado.
    mfa_code: str | None = Field(default=None, min_length=6, max_length=16)


class ChangePasswordIn(BaseModel):
    current_password: str = Field(min_length=1, max_length=1024)
    new_password: str = Field(min_length=1, max_length=1024)


class SessionOut(BaseModel):
    id: uuid.UUID
    created_at: datetime
    last_seen_at: datetime
    expires_at: datetime
    user_agent: str | None
    ip: str | None
    current: bool


class RevokedOut(BaseModel):
    revoked: int


class GoogleStatusOut(BaseModel):
    # A Groone configurou o cliente OAuth.
    available: bool
    linked: bool
