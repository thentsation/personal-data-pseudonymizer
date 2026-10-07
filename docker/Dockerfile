FROM python:3.14-slim AS builder

WORKDIR /app

COPY config/requirements.lock ./config/

RUN pip install --no-cache-dir --prefix=/install -r ./config/requirements.lock

FROM python:3.14-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

COPY --from=builder /install /usr/local

RUN python -m spacy download en_core_web_sm

RUN useradd --create-home appuser
USER appuser

COPY src ./src

ENTRYPOINT ["python", "src/main.py"]
CMD ["--sample"]
