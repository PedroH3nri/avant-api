"""DTOs de entrada e saída do domínio reports. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Annotated, Any, Literal

from avant_core.access.enums.visibility import Visibility
from avant_core.metrics.enums import (
    FilterOperator,
    MetricFormat,
    MetricKind,
    MetricSource,
    RelativePeriod,
)
from avant_core.metrics.models import (
    CustomMetric,
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
from avant_core.reports.enums.chart_type import ChartType
from avant_core.reports.models.report_template import ReportTemplate
from avant_core.reports.models.saved_report import SavedReport
from avant_core.reports.services import ReportInput
from pydantic import BaseModel, Field

from avant_api.shared.dto import PageOut

ExportFormat = Literal["csv", "xlsx"]


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


class CustomCatalogMetricOut(BaseModel):
    # A chave para pedir a métrica numa consulta (``custom.<chave>``).
    query_key: str
    name: str
    description: str | None
    format: MetricFormat
    decimals: int
    sources: list[MetricSource]

    @classmethod
    def of(cls, metric: CustomMetric, sources: frozenset[MetricSource]) -> "CustomCatalogMetricOut":
        """Monta a métrica personalizada da Empresa para o catálogo."""
        return cls(
            query_key=f"custom.{metric.key}",
            name=metric.name,
            description=metric.description,
            format=metric.format,
            decimals=metric.decimals,
            sources=sorted(sources),
        )


class MetricCatalogOut(BaseModel):
    metrics: list[MetricOut]
    # As métricas personalizadas da Empresa ativa.
    custom_metrics: list[CustomCatalogMetricOut]
    dimensions: list[DimensionOut]
    operators: list[FilterOperator]
    periods: list[RelativePeriod]
    max_days: int
    max_limit: int


class PeriodIn(BaseModel):
    preset: RelativePeriod | None = None
    start: date | None = None
    end: date | None = None

    @classmethod
    def of(cls, period: Period) -> "PeriodIn":
        """Monta o período salvo: relativo ou fixo."""
        return cls(preset=period.preset, start=period.start, end=period.end)


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


class SavedQueryOut(BaseModel):
    # A consulta salva, no formato de ``ReportQueryIn`` sem a moeda (cada um roda na sua).
    source: MetricSource
    metrics: list[str]
    period: PeriodIn
    dimensions: list[str]
    filters: list[FilterIn]
    compare: bool
    order: list[OrderIn]
    limit: int

    @classmethod
    def of(cls, definition: QueryDefinition) -> "SavedQueryOut":
        """Monta a consulta a partir da definição do motor."""
        return cls(
            source=definition.source,
            metrics=list(definition.metrics),
            period=PeriodIn.of(definition.period),
            dimensions=list(definition.dimensions),
            filters=[
                FilterIn(field=item.field, operator=item.operator, values=list(item.values))
                for item in definition.filters
            ],
            compare=definition.compare,
            order=[
                OrderIn(field=item.field, descending=item.descending) for item in definition.order
            ],
            limit=definition.limit,
        )


class SavedReportIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    # A moeda da consulta não fica salva: cada execução usa a de quem roda.
    query: ReportQueryIn
    chart_type: ChartType
    chart_options: dict[str, Any] = Field(default_factory=dict, max_length=10)
    visibility: Visibility = Visibility.PRIVATE
    # Papéis que veem o relatório, só com a visibilidade ``roles``.
    role_ids: list[uuid.UUID] = Field(default_factory=list, max_length=50)

    def input(self) -> ReportInput:
        """O formulário no formato do caso de uso."""
        return ReportInput(
            name=self.name,
            query=self.query.definition(),
            chart_type=self.chart_type,
            chart_options=self.chart_options,
            visibility=self.visibility,
            role_ids=tuple(self.role_ids),
            description=self.description,
        )


class SavedReportOut(BaseModel):
    id: uuid.UUID
    name: str
    description: str | None
    query: SavedQueryOut
    chart_type: ChartType
    chart_options: dict[str, Any]
    visibility: Visibility
    role_ids: list[uuid.UUID]
    owner_user_id: uuid.UUID
    created_by: uuid.UUID
    created_at: datetime
    updated_at: datetime
    # A pessoa pode editar e apagar (é a dona ou tem reports.manage).
    editable: bool

    @classmethod
    def of(
        cls, report: SavedReport, definition: QueryDefinition, editable: bool
    ) -> "SavedReportOut":
        """Monta o relatório salvo com a consulta já lida."""
        return cls(
            id=report.id,
            name=report.name,
            description=report.description,
            query=SavedQueryOut.of(definition),
            chart_type=report.chart_type,
            chart_options=report.chart_options,
            visibility=report.visibility,
            role_ids=report.role_ids,
            owner_user_id=report.owner_user_id,
            created_by=report.created_by,
            created_at=report.created_at,
            updated_at=report.updated_at,
            editable=editable,
        )


class ReportTemplateOut(BaseModel):
    key: str
    name: LabelOut
    query: SavedQueryOut
    chart_type: ChartType
    chart_options: dict[str, Any]

    @classmethod
    def of(cls, template: ReportTemplate) -> "ReportTemplateOut":
        """Monta o modelo pronto com o nome nos três idiomas."""
        return cls(
            key=template.key,
            name=LabelOut(**template.name),
            query=SavedQueryOut.of(template.query),
            chart_type=template.chart_type,
            chart_options=template.chart_options,
        )


class ReportCountsOut(BaseModel):
    """Quantos relatórios cada aba tem, sem a busca."""

    all: int
    mine: int
    shared: int


class ReportPageOut(PageOut[SavedReportOut]):
    """Uma página dos relatórios salvos com as contagens das abas."""

    counts: ReportCountsOut
