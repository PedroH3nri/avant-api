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
    db_max_overflow: int = 5
    # Quanto um pedido espera por uma conexão livre antes de desistir com erro.
    db_pool_timeout_seconds: int = 10
    # Toda consulta da API tem prazo; o motor de relatórios usa um prazo menor por cima.
    db_statement_timeout_ms: int = 30_000
    db_idle_in_transaction_timeout_ms: int = 60_000
    # Chave Fernet dos segredos de 2FA. Trocar a chave invalida todos os 2FA ativos.
    mfa_encryption_key: str
    app_base_url: str = "http://localhost:8080"
    # Sem chave, os e-mails só vão para o log (local e testes).
    resend_api_key: str | None = None
    mail_from: str = "Avant <nao-responda@avant.groone.com>"
    # Limites de tentativas, balde das chaves de API, eventos e caches. Obrigatória em todo
    # ambiente: um limite não pode valer só em staging e produção.
    redis_url: str
    # Login com Google. Sem as duas, as rotas /auth/google respondem google_unavailable.
    google_oauth_client_id: str | None = None
    google_oauth_client_secret: str | None = None
    # Fila do avant-worker (RabbitMQ). Obrigatória em todo ambiente: o esqueci a senha só
    # agenda o envio, e o mesmo caminho vale no local.
    celery_broker_url: str
    # E-mail da conta de serviço da Groone no Ad Manager, mostrado no guia de conexão.
    # Não é segredo: a chave fica só nos workers da fila gam.
    gam_service_account_email: str = "avant@groone-ads.iam.gserviceaccount.com"
    # Network da Groone, que entra no arquivo de instalação dos clientes Manage Inventory.
    # Não é segredo: é o mesmo valor que o Genius usa no groone.js.
    gam_groone_network_code: str = "22893970961"
    # Base GeoLite2 Country (.mmdb) para o país dos floors das regras de preço. Sem ela, a rota
    # dos floors devolve só o grupo de controle.
    geolite2_country_file: str | None = None
    # Processos do uvicorn no contêiner (a mesma variável que o uvicorn lê).
    web_concurrency: int = 1
    # Modo multiprocesso do prometheus_client: cada processo grava aqui e o /metrics soma todos.
    # Obrigatório com mais de um processo, senão cada coleta cai num processo qualquer.
    prometheus_multiproc_dir: str | None = None

    @model_validator(mode="after")
    def _required_services(self) -> "Settings":
        """Exige Redis e o broker do Celery em todo ambiente, o diretório das métricas com vários
        processos e o Resend em staging e produção."""
        if not self.redis_url.strip():
            raise ValueError("REDIS_URL é obrigatória em todo ambiente")
        if not self.celery_broker_url.strip():
            raise ValueError("CELERY_BROKER_URL é obrigatória em todo ambiente")
        if self.web_concurrency > 1 and not self.prometheus_multiproc_dir:
            raise ValueError("PROMETHEUS_MULTIPROC_DIR é obrigatória com WEB_CONCURRENCY > 1")
        if self.avant_env in ("staging", "production") and not self.resend_api_key:
            raise ValueError("RESEND_API_KEY é obrigatória em staging e produção")
        return self

    @property
    def cookie_secure(self) -> bool:
        """Diz se os cookies saem com Secure (staging e produção)."""
        return self.avant_env in ("staging", "production")

    @property
    def session_cookie(self) -> str:
        """O cookie da sessão; com Secure, com o prefixo __Host- (nenhum subdomínio o grava)."""
        return f"{self._cookie_prefix}avant_session"

    @property
    def csrf_cookie(self) -> str:
        """O cookie de CSRF, legível pelo painel, com o mesmo prefixo do de sessão."""
        return f"{self._cookie_prefix}avant_csrf"

    @property
    def _cookie_prefix(self) -> str:
        """``__Host-`` quando os cookies saem com Secure; sem HTTPS o navegador recusaria."""
        return "__Host-" if self.cookie_secure else ""
