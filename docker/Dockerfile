FROM python:3.14-slim AS builder

WORKDIR /app

COPY config/requirements.lock ./config/

RUN pip install --no-cache-dir --prefix=/install -r ./config/requirements.lock

# CI (o Jenkins roda docker build --target test): ruff, mypy e pytest com cobertura
# mínima de 90% em Python 3.11 e 3.12, nas versões fixadas em config/requirements-dev.txt
# (atualizadas pelo Renovate). pip-audit e Trivy rodam no pipeline da plataforma, fora do
# cache de build, porque o resultado muda com as bases de vulnerabilidades.
FROM python:3.12-slim AS lint

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(ruff|mypy)==' ./config/requirements-dev.txt)

COPY . .

RUN ruff check . && ruff format --check . && mypy && touch /ok

FROM python:3.11-slim AS pytest-py311

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(pytest|pytest-cov)==' ./config/requirements-dev.txt) \
    && python -m spacy download en_core_web_sm

COPY . .

RUN pytest --cov=src --cov-report=term-missing --cov-fail-under=90 && touch /ok

FROM python:3.12-slim AS pytest-py312

WORKDIR /app

COPY config/requirements.txt config/requirements-dev.txt ./config/

RUN pip install --no-cache-dir -r ./config/requirements.txt \
    $(grep -E '^(pytest|pytest-cov)==' ./config/requirements-dev.txt) \
    && python -m spacy download en_core_web_sm

COPY . .

RUN pytest --cov=src --cov-report=term-missing --cov-fail-under=90 && touch /ok

FROM scratch AS test

COPY --from=lint /ok /lint.ok
COPY --from=pytest-py311 /ok /pytest-py311.ok
COPY --from=pytest-py312 /ok /pytest-py312.ok

FROM python:3.14-slim AS runtime

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

RUN python -m spacy download en_core_web_sm

RUN useradd --create-home appuser
USER appuser

ARG APP_VERSION=dev
ENV APP_VERSION=$APP_VERSION

COPY src ./src

ENTRYPOINT ["python", "src/main.py"]
CMD ["--sample"]
