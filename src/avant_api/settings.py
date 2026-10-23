"""Configuração por variáveis de ambiente. Os valores reais ficam só nas VMs."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    avant_env: Literal["local", "test", "staging", "production"] = "local"
    # Papel avant_app: sem BYPASSRLS e sem ser dono das tabelas.
    database_url: str
    db_pool_size: int = 10
    # Chave Fernet dos segredos de 2FA. Trocar a chave invalida todos os 2FA ativos.
    mfa_encryption_key: str
    app_base_url: str = "http://localhost:8080"
    session_cookie: str = "avant_session"
    csrf_cookie: str = "avant_csrf"

    @property
    def cookie_secure(self) -> bool:
        return self.avant_env in ("staging", "production")
