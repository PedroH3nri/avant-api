"""DTOs de entrada e saída do domínio reports. Datas sempre em ISO 8601 UTC."""

from datetime import date
from decimal import Decimal
from typing import Annotated

from avant_core.metrics.enums import (
    FilterOperator,
    MetricFormat,
    MetricKind,
    MetricSource,
    RelativePeriod,
)
from avant_core.metrics.models import (
    DateRange,
    Dimension,
    DimensionValue,
    Filter,
    Label,
    Metric,
    Order,
    Period,
    QueryDefinition,
    QueryResult,
)
from avant_core.metrics.services.query_rules import (
    MAX_FILTER_VALUES,
    MAX_LIMIT,
    UNFILTERABLE_DIMENSIONS,
)
from avant_core.money.catalog import BASE_CURRENCY
from pydantic import BaseModel, Field


class LabelOut(BaseModel):
    pt: str
    en: str
    es: str

    @classmethod
    def of(cls, label: Label) -> "LabelOut":
        """Monta o texto nos três idiomas."""
        return cls(pt=label.pt, en=label.en, es=label.es)


class MetricOut(BaseModel):
    key: str
    label: LabelOut
    kind: MetricKind
    format: MetricFormat
    # Fontes onde a métrica existe: as visitas (page_views) têm a sua.
    sources: list[MetricSource]

    @classmethod
    def of(cls, metric: Metric) -> "MetricOut":
        """Monta a métrica do catálogo."""
        return cls(
            key=metric.key,
            label=LabelOut.of(metric.label),
            kind=metric.kind,
            format=metric.format,
            sources=sorted(metric.sources),
        )


class DimensionOut(BaseModel):
    key: str
    label: LabelOut
    sources: list[MetricSource]
    # Data, semana, mês e hora agrupam, mas não filtram: o período já faz isso.
    filterable: bool

    @classmethod
    def of(cls, dimension: Dimension) -> "DimensionOut":
        """Monta a dimensão do catálogo."""
        return cls(
            key=dimension.key,
            label=LabelOut.of(dimension.label),
            sources=sorted(dimension.sources),
            filterable=dimension.key not in UNFILTERABLE_DIMENSIONS,
        )


class MetricCatalogOut(BaseModel):
    metrics: list[MetricOut]
    dimensions: list[DimensionOut]
    operators: list[FilterOperator]
    periods: list[RelativePeriod]
    max_days: int
    max_limit: int


class PeriodIn(BaseModel):
    preset: RelativePeriod | None = None
    start: date | None = None
    end: date | None = None


class FilterIn(BaseModel):
    field: str = Field(min_length=1, max_length=60)
    operator: FilterOperator
    values: list[Annotated[str, Field(max_length=300)]] = Field(
        min_length=1, max_length=MAX_FILTER_VALUES
    )


class OrderIn(BaseModel):
    field: str = Field(min_length=1, max_length=60)
    descending: bool = True


class ReportQueryIn(BaseModel):
    source: MetricSource = MetricSource.GAM
    metrics: list[str] = Field(min_length=1, max_length=30)
    period: PeriodIn
    dimensions: list[str] = Field(default_factory=list, max_length=6)
    filters: list[FilterIn] = Field(default_factory=list, max_length=20)
    # Soma também o período de mesmo tamanho logo antes.
    compare: bool = False
    order: list[OrderIn] = Field(default_factory=list, max_length=5)
    limit: int = Field(default=1000, ge=1, le=MAX_LIMIT)
    # Moeda do dinheiro na resposta; o painel manda a moeda de visualização da pessoa.
    currency: str = Field(default=BASE_CURRENCY, min_length=3, max_length=3)

    def definition(self) -> QueryDefinition:
        """A definição do motor de consulta do avant-core."""
        return QueryDefinition(
            source=self.source,
            metrics=tuple(self.metrics),
            period=Period(self.period.preset, self.period.start, self.period.end),
            dimensions=tuple(self.dimensions),
            filters=tuple(
                Filter(item.field, item.operator, tuple(item.values)) for item in self.filters
            ),
            compare=self.compare,
            order=tuple(Order(item.field, item.descending) for item in self.order),
            limit=self.limit,
            currency=self.currency.upper(),
        )


class ReportRowOut(BaseModel):
    # Datas em ISO, sites e networks pelo id (o nome vem em ``labels``).
    dimensions: dict[str, str | None]
    # Valores decimais como texto, para não perder centavos no caminho.
    metrics: dict[str, Decimal | None]
    previous: dict[str, Decimal | None] | None


class ReportRangeOut(BaseModel):
    start: date
    end: date

    @classmethod
    def of(cls, date_range: DateRange) -> "ReportRangeOut":
        """Monta o período."""
        return cls(start=date_range.start, end=date_range.end)


class ReportResultOut(BaseModel):
    period: ReportRangeOut
    rows: list[ReportRowOut]
    totals: dict[str, Decimal | None]
    previous_period: ReportRangeOut | None
    previous_totals: dict[str, Decimal | None] | None
    # Havia mais linhas que o limite.
    truncated: bool
    labels: dict[str, dict[str, str]]
    currency: str

    @classmethod
    def of(cls, result: QueryResult) -> "ReportResultOut":
        """Monta o resultado do motor de consulta."""
        return cls(
            period=ReportRangeOut.of(result.date_range),
            rows=[
                ReportRowOut(
                    dimensions={
                        key: dimension_text(value) for key, value in row.dimensions.items()
                    },
                    metrics=row.metrics,
                    previous=row.previous,
                )
                for row in result.rows
            ],
            totals=result.totals,
            previous_period=ReportRangeOut.of(result.previous_range)
            if result.previous_range is not None
            else None,
            previous_totals=result.previous_totals,
            truncated=result.truncated,
            labels=result.labels,
            currency=result.currency,
        )


def dimension_text(value: DimensionValue) -> str | None:
    """Valor de uma dimensão como texto: data em ISO, id como texto."""
    if value is None:
        return None
    if isinstance(value, date):
        return value.isoformat()
    return str(value)
