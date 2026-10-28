"""DTOs de entrada e saída do domínio internal/people. Datas sempre em ISO 8601 UTC."""

from datetime import datetime

from avant_core.identity.enums import UserStatus
from pydantic import BaseModel

from avant_api.shared.dto import CompanyRefOut, UserOut


class PersonOut(BaseModel):
    user: UserOut
    status: UserStatus
    mfa_enabled: bool
    last_login_at: datetime | None
    companies: list[CompanyRefOut]
