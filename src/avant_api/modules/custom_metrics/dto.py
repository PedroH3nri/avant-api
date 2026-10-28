"""DTOs de entrada e saída das métricas personalizadas. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime
from decimal import Decimal

from avant_core.metrics.enums import MetricFormat, MetricSource
from avant_core.metrics.models import CustomMetric
from avant_core.metrics.services import CustomMetricInput
from pydantic import BaseModel, Field


class CustomMetricIn(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    # Conta sobre as métricas do catálogo e ``custom.<chave>`` de outras personalizadas.
    formula: str = Field(min_length=1, max_length=300)
    format: MetricFormat
    decimals: int = Field(default=2, ge=0, le=6)
    description: str | None = Field(default=None, max_length=280)

    def input(self) -> CustomMetricInput:
        """O formulário no formato do caso de uso."""
        return CustomMetricInput(
            name=self.name,
            formula=self.formula,
            format=self.format,
            decimals=self.decimals,
            description=self.description,
        )


class CustomMetricCheckIn(CustomMetricIn):
    # Na edição, a métrica que está sendo editada (a chave dela não muda).
    metric_id: uuid.UUID | None = None
    # Valores de exemplo das métricas do catálogo (``revenue``); as personalizadas são calculadas.
    sample: dict[str, Decimal] | None = Field(default=None, max_length=40)


class CustomMetricCheckOut(BaseModel):
    valid: bool
    # Código do erro (invalid_formula, invalid_input, custom_metric_in_use), para traduzir.
    code: str | None = None
    # Onde a fórmula quebrou, em português.
    error: str | None = None
    variables: list[str] = Field(default_factory=list)
    # A fórmula calculada sobre a amostra; vazio sem amostra ou sem denominador.
    value: Decimal | None = None


class CustomMetricOut(BaseModel):
    id: uuid.UUID
    key: str
    # A chave para pedir a métrica numa consulta.
    query_key: str
    name: str
    description: str | None
    formula: str
    format: MetricFormat
    decimals: int
    # Fontes em que a métrica pode ser pedida (com visitas, só a do GAM).
    sources: list[MetricSource]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, metric: CustomMetric, sources: frozenset[MetricSource]) -> "CustomMetricOut":
        """Monta a métrica personalizada com as fontes em que ela pode ser pedida."""
        return cls(
            id=metric.id,
            key=metric.key,
            query_key=f"custom.{metric.key}",
            name=metric.name,
            description=metric.description,
            formula=metric.formula,
            format=metric.format,
            decimals=metric.decimals,
            sources=sorted(sources),
            created_at=metric.created_at,
            updated_at=metric.updated_at,
        )
