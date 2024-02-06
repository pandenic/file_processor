FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY ../poetry.lock pyproject.toml infra/run_app.sh ./

COPY ../file_processing .

RUN poetry install --without dev

RUN chmod +x run_app.sh
ENTRYPOINT ["/app/run_app.sh"]
