"""Service da saúde do processo: confere as dependências que a API usa."""

from sqlalchemy import Engine, text


class HealthService:
    """Responde se o banco atende."""

    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    def checks(self) -> dict[str, str]:
        """O estado de cada dependência: ``ok`` ou o nome do erro."""
        checks: dict[str, str] = {}
        try:
            with self._engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            checks["database"] = "ok"
        except Exception as exc:
            checks["database"] = type(exc).__name__
        return checks
