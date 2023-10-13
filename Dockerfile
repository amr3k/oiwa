FROM python:3.12-alpine

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_NO_CACHE_DIR=1 \
  POETRY_VERSION=1.3.1

COPY main.py pyproject.toml poetry.lock /app/

RUN apk add --no-cache curl gcc libressl-dev musl-dev libffi-dev && \
  pip install --no-cache-dir poetry && \
  poetry config virtualenvs.create false && \
  poetry install --no-dev --no-interaction --no-ansi && \
  apk del curl gcc libressl-dev musl-dev libffi-dev

CMD ["python", "main.py"]
