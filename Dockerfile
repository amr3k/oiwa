FROM python:3.12-alpine

RUN mkdir /app

COPY main.py pyproject.toml poetry.lock /app/

WORKDIR /app/

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV PATH="/root/.cargo/bin:${PATH}"

RUN apk add --no-cache curl gcc libressl-dev musl-dev libffi-dev

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --profile=minimal

RUN pip install --no-cache-dir poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

RUN apk del curl gcc libressl-dev musl-dev libffi-dev

CMD ["python", "main.py"]
