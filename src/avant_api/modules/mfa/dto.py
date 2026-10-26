"""DTOs de entrada e saída do domínio mfa. Datas sempre em ISO 8601 UTC."""

from pydantic import BaseModel, Field


class MfaCodeIn(BaseModel):
    """Código de 6 dígitos do app ou um código de recuperação (xxxx-xxxx)."""

    code: str = Field(min_length=6, max_length=16)


class MfaSetupOut(BaseModel):
    secret: str
    # O link otpauth://..., para o QR code.
    uri: str


class RecoveryCodesOut(BaseModel):
    # Aparecem só nesta resposta.
    recovery_codes: list[str]
