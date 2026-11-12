# syntax=docker/dockerfile:1.7
# O avant-core é privado: o build recebe um token de leitura do GitHub como secret,
# que não fica em nenhuma camada da imagem.
#   docker build --secret id=github_token,env=GITHUB_TOKEN -t ghcr.io/pedroh3nri/avant-api .
FROM ghcr.io/astral-sh/uv:0.11@sha256:77280f2f771df71f90786c314fe1bbc1e023feac652969bbf139c280babf2eb7 AS uv

FROM python:3.12-slim@sha256:e695ab189fa2d082b1c61c69a6b888a5adeca61ceeccad107b1ed2a125721a9e AS build
COPY --from=uv /uv /usr/local/bin/uv
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN --mount=type=secret,id=github_token \
    git config --global url."https://x-access-token:$(cat /run/secrets/github_token)@github.com/".insteadOf "https://github.com/" \
    && uv sync --frozen --no-dev \
    && git config --global --unset-all url."https://x-access-token:$(cat /run/secrets/github_token)@github.com/".insteadOf

FROM python:3.12-slim@sha256:e695ab189fa2d082b1c61c69a6b888a5adeca61ceeccad107b1ed2a125721a9e
RUN useradd --system --uid 10001 avant
WORKDIR /app
COPY --from=build /app /app
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1
USER avant
EXPOSE 8000
HEALTHCHECK --interval=10s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/api/v1/health')"
# Processos do uvicorn por contêiner (o uvicorn lê WEB_CONCURRENCY); cada um tem o próprio pool.
# Com mais de um, as métricas do Prometheus vão para PROMETHEUS_MULTIPROC_DIR e o /metrics soma
# todos os processos; o diretório é limpo a cada subida, para não somar processos antigos.
ENV WEB_CONCURRENCY=2 PROMETHEUS_MULTIPROC_DIR=/tmp/avant-metrics
# O X-Forwarded-For só vale vindo do proxy: o uvicorn lê FORWARDED_ALLOW_IPS (endereços ou redes
# do nginx do compose), que a imagem não define. Sem ela, ou com "*", as Settings recusam a subida.
CMD ["sh", "-c", "rm -rf \"$PROMETHEUS_MULTIPROC_DIR\" && mkdir -p \"$PROMETHEUS_MULTIPROC_DIR\" && exec uvicorn avant_api.main:create_app --factory --host 0.0.0.0 --port 8000 --proxy-headers"]
