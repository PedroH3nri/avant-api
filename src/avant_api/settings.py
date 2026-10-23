"""Configuração por variáveis de ambiente. Os valores reais ficam só nas VMs."""

from typing import Literal

from pydantic import model_validator
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
    # Sem chave, os e-mails só vão para o log (local e testes).
    resend_api_key: str | None = None
    mail_from: str = "Avant <nao-responda@avant.groone.com>"
    session_cookie: str = "avant_session"
    csrf_cookie: str = "avant_csrf"

    @model_validator(mode="after")
    def _mail_in_deployed_envs(self) -> "Settings":
        if self.avant_env in ("staging", "production") and not self.resend_api_key:
            raise ValueError("RESEND_API_KEY é obrigatória em staging e produção")
        return self

    @property
    def cookie_secure(self) -> bool:
        return self.avant_env in ("staging", "production")
