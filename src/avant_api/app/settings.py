"""Configuração por variáveis de ambiente. Os valores reais ficam só nas VMs. A mesma regra vale
em todo ambiente: nenhuma configuração muda de comportamento pelo nome do ambiente."""

import ipaddress
import logging
from typing import Literal

from pydantic import Field, ValidationError, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

log = logging.getLogger("avant.api")


class InvalidVariables(ValueError):
    """Variáveis que faltam ou estão inválidas; leva só os nomes, nunca os valores."""

    def __init__(self, names: list[str]) -> None:
        super().__init__(f"variáveis faltando ou inválidas: {', '.join(names)}")
        self.names = names


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    # Papel avant_app: sem BYPASSRLS e sem ser dono das tabelas.
    database_url: str
    # Pool e prazos do engine (avant_core.db.engine.EngineSettings): os mesmos em todo ambiente,
    # e a subida recusa zero e o que passa dos tetos do core.
    db_pool_size: int = 10
    db_max_overflow: int = 5
    # Quanto um pedido espera por uma conexão livre antes de desistir com erro.
    db_pool_timeout_seconds: float = 10
    # Abaixo de qualquer timeout de rede ou proxy entre a API e o Postgres.
    db_pool_recycle_seconds: int = 1800
    # Toda consulta da API tem prazo; o motor de relatórios usa um prazo menor por cima.
    db_statement_timeout_ms: int = 30_000
    db_idle_in_transaction_timeout_ms: int = 60_000
    db_lock_timeout_ms: int = 10_000
    # Chave Fernet dos segredos de 2FA. Trocar a chave invalida todos os 2FA ativos.
    mfa_encryption_key: str
    app_base_url: str = "http://localhost:8080"
    # Transporte dos e-mails, sem padrão: ``resend`` (VMs) ou ``smtp`` (o Mailpit no local).
    # Nenhum e-mail nem link com token vai para o log.
    mail_transport: Literal["resend", "smtp"]
    # Obrigatória com MAIL_TRANSPORT=resend.
    resend_api_key: str | None = None
    # Obrigatória com MAIL_TRANSPORT=smtp: ``smtps://`` com TLS, ``smtp://`` só na mesma rede.
    smtp_url: str | None = None
    mail_from: str = "Avant <nao-responda@avant.groone.com>"
    # Limites de tentativas, balde das chaves de API, eventos e caches. Obrigatória em todo
    # ambiente: um limite não pode valer só em staging e produção.
    redis_url: str = Field(min_length=1)
    # Login com Google. Sem as duas, as rotas /auth/google respondem google_unavailable.
    google_oauth_client_id: str | None = None
    google_oauth_client_secret: str | None = None
    # Fila do avant-worker (RabbitMQ). Obrigatória em todo ambiente: o esqueci a senha só
    # agenda o envio, e o mesmo caminho vale no local.
    celery_broker_url: str = Field(min_length=1)
    # E-mail da conta de serviço da Groone no Ad Manager, mostrado no guia de conexão.
    # Não é segredo: a chave fica só nos workers da fila gam.
    gam_service_account_email: str = "avant@groone-ads.iam.gserviceaccount.com"
    # Network da Groone, que entra no arquivo de instalação dos clientes Manage Inventory.
    # Não é segredo: é o mesmo valor que o Genius usa no groone.js.
    gam_groone_network_code: str = "22893970961"
    # Base GeoLite2 Country (.mmdb) para o país dos floors das regras de preço. Sem ela, a rota
    # dos floors devolve só o grupo de controle.
    geolite2_country_file: str | None = None
    # Endereços ou redes do proxy (o nginx do compose) de quem o uvicorn aceita o X-Forwarded-For;
    # o uvicorn lê a mesma variável. Obrigatória em todo ambiente e sem "*": o IP do cliente
    # sustenta os limites de tentativas.
    forwarded_allow_ips: str = Field(min_length=1)
    # Processos do uvicorn no contêiner (a mesma variável que o uvicorn lê).
    web_concurrency: int = 1
    # Modo multiprocesso do prometheus_client: cada processo grava aqui e o /metrics soma todos.
    # Obrigatório com mais de um processo, senão cada coleta cai num processo qualquer.
    prometheus_multiproc_dir: str | None = None

    @model_validator(mode="after")
    def _required_services(self) -> "Settings":
        """Exige Redis, o broker do Celery, a configuração do transporte de e-mail e o proxy em
        todo ambiente, e o diretório das métricas com vários processos."""
        required = {
            "REDIS_URL": self.redis_url,
            "CELERY_BROKER_URL": self.celery_broker_url,
            "RESEND_API_KEY": self.resend_api_key if self.mail_transport == "resend" else "-",
            "SMTP_URL": self.smtp_url if self.mail_transport == "smtp" else "-",
        }
        invalid = [name for name, value in required.items() if not (value or "").strip()]
        if self.web_concurrency > 1 and not self.prometheus_multiproc_dir:
            invalid.append("PROMETHEUS_MULTIPROC_DIR")
        if not _are_proxy_addresses(self.forwarded_allow_ips):
            invalid.append("FORWARDED_ALLOW_IPS")
        if invalid:
            raise InvalidVariables(invalid)
        return self


def _are_proxy_addresses(addresses: str) -> bool:
    """Diz se são só endereços ou redes IP separados por vírgula; "*" e nome de host não."""
    try:
        for entry in addresses.split(","):
            ipaddress.ip_network(entry.strip(), strict=False)
    except ValueError:
        return False
    return True


def invalid_variable_names(error: ValidationError) -> list[str]:
    """Os nomes das variáveis do erro de validação, sem os valores que o pydantic traz junto."""
    names: set[str] = set()
    for detail in error.errors():
        if detail["loc"]:
            names.add(str(detail["loc"][0]).upper())
        cause = detail.get("ctx", {}).get("error")
        if isinstance(cause, InvalidVariables):
            names.update(cause.names)
    return sorted(names)


def load_settings() -> Settings:
    """Lê as Settings do ambiente; se falta ou está errada alguma variável, encerra a subida com
    os nomes, sem os valores (o erro do pydantic traz as outras variáveis, com segredos)."""
    try:
        return Settings()
    except ValidationError as error:
        names = ", ".join(invalid_variable_names(error))
        log.critical("configuração da API incompleta", extra={"variables": names})
        raise SystemExit(f"configuração da API incompleta: {names}") from None
