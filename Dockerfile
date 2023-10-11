FROM python:alpine

RUN mkdir /app

COPY main.py pyproject.toml poetry.lock /app/

WORKDIR /app/

RUN pip install -U pip setuptools

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev

CMD ["python", "main.py"]
