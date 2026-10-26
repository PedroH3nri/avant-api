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
    # Contadores do limite de tentativas. Sem Redis (local e testes), ficam na memória.
    redis_url: str | None = None
    # Login com Google. Sem as duas, as rotas /auth/google respondem google_unavailable.
    google_oauth_client_id: str | None = None
    google_oauth_client_secret: str | None = None
    # Fila do avant-worker. Sem ela (local e testes), as tarefas só ficam registradas.
    celery_broker_url: str | None = None
    # E-mail da conta de serviço da Groone no Ad Manager, mostrado no guia de conexão.
    # Não é segredo: a chave fica só nos workers da fila gam.
    gam_service_account_email: str = "avant@groone-ads.iam.gserviceaccount.com"
    session_cookie: str = "avant_session"
    csrf_cookie: str = "avant_csrf"

    @model_validator(mode="after")
    def _mail_in_deployed_envs(self) -> "Settings":
        """Exige Resend, Redis e o broker do Celery em staging e produção."""
        if self.avant_env in ("staging", "production") and not self.resend_api_key:
            raise ValueError("RESEND_API_KEY é obrigatória em staging e produção")
        if self.avant_env in ("staging", "production") and not self.redis_url:
            # Com várias instâncias, contador em memória não limita nada.
            raise ValueError("REDIS_URL é obrigatória em staging e produção")
        if self.avant_env in ("staging", "production") and not self.celery_broker_url:
            raise ValueError("CELERY_BROKER_URL é obrigatória em staging e produção")
        return self

    @property
    def cookie_secure(self) -> bool:
        """Diz se os cookies saem com Secure (staging e produção)."""
        return self.avant_env in ("staging", "production")
