"""Os testes da API rodam contra um PostgreSQL real, com as migrations do avant-core.

AVANT_TEST_MIGRATIONS_URL: papel avant_owner. AVANT_TEST_DATABASE_URL: papel avant_app.
Sem as duas, os testes que precisam de banco são pulados.
"""

import os
import uuid
from collections.abc import Iterator
from dataclasses import dataclass, field

import pytest
from alembic import command
from alembic.config import Config
from avant_core.company.domain import InvitationKind
from avant_core.identity.crypto import FernetSecretBox
from avant_core.identity.passwords import Argon2PasswordHasher
from avant_core.shared.clock import SystemClock
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine, text

from avant_api.main import create_app
from avant_api.services import Services
from avant_api.settings import Settings

APP_URL = os.environ.get("AVANT_TEST_DATABASE_URL")
OWNER_URL = os.environ.get("AVANT_TEST_MIGRATIONS_URL")
FINANCE = uuid.uuid5(uuid.NAMESPACE_URL, "avant:role:finance")


@dataclass
class Sent:
    to: str
    token: str
    kind: InvitationKind


@dataclass
class CapturingMailer:
    sent: list[Sent] = field(default_factory=list)

    def send_invitation(
        self, *, to: str, token: str, kind: InvitationKind, company_name: str | None, locale: str
    ) -> None:
        self.sent.append(Sent(to, token, kind))


@pytest.fixture(scope="session")
def engine() -> Iterator[Engine]:
    if not (APP_URL and OWNER_URL):
        pytest.skip("defina AVANT_TEST_DATABASE_URL e AVANT_TEST_MIGRATIONS_URL")
    cfg = Config()
    cfg.set_main_option("script_location", "avant_core:migrations")
    os.environ["DATABASE_MIGRATIONS_URL"] = OWNER_URL
    command.downgrade(cfg, "base")
    command.upgrade(cfg, "head")
    eng = create_engine(APP_URL)
    yield eng
    eng.dispose()


@pytest.fixture
def mailer() -> CapturingMailer:
    return CapturingMailer()


@pytest.fixture
def client(engine: Engine, mailer: CapturingMailer) -> Iterator[TestClient]:
    key = Fernet.generate_key().decode()
    services = Services(
        settings=Settings(database_url=APP_URL or "", avant_env="test", mfa_encryption_key=key),
        engine=engine,
        clock=SystemClock(),
        hasher=Argon2PasswordHasher(),
        mailer=mailer,
        box=FernetSecretBox(key),
    )
    with TestClient(create_app(services)) as c:
        yield c
    owner = create_engine(OWNER_URL or "")
    with owner.begin() as conn:
        for table in (
            "sessions",
            "member_permissions",
            "memberships",
            "invitations",
            "user_credentials",
        ):
            conn.execute(text(f"DELETE FROM {table}"))
        conn.execute(text("DELETE FROM audit_logs"))
        conn.execute(text("DELETE FROM roles WHERE company_id IS NOT NULL"))
        conn.execute(text("DELETE FROM companies"))
        conn.execute(text("DELETE FROM users"))
    owner.dispose()
