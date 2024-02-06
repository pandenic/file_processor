FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY ../poetry.lock pyproject.toml ./

COPY ../file_processing .

RUN poetry install --without dev

CMD ["poetry", "run", "celery", "-A", "file_processing", "worker", "--loglevel=INFO"]
