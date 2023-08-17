FROM python:alpine

RUN mkdir /app

COPY . /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install -U pip setuptools

RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-dev

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "port", "8000"]
