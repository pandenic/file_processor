FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY poetry.lock pyproject.toml file_processing/run_app.sh ./

RUN poetry install

COPY file_processing .

RUN chmod +x run_app.sh
ENTRYPOINT ["/app/run_app.sh"]
