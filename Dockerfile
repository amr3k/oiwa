FROM python:3.14-alpine

WORKDIR /app

ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_NO_CACHE_DIR=1

COPY pyproject.toml uv.lock /app/

RUN pip install --no-cache-dir uv && \
  uv sync --frozen --no-dev --no-install-project

COPY main.py /app/

CMD ["uv", "run", "--no-sync", "python", "main.py"]
