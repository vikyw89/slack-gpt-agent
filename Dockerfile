FROM python:3.12-slim AS base
WORKDIR /app
RUN apt-get update && apt-get install -y \
    curl \
    wget
RUN pip install poetry==1.7.1

FROM base AS codebase
WORKDIR /app
COPY . .

FROM codebase AS development
WORKDIR /app
RUN poetry install --no-interaction --no-ansi
EXPOSE 8000
CMD "poetry run uvicorn app.main:api --host 0.0.0.0 --port 8000 --reload"

FROM codebase AS production
WORKDIR /app
RUN poetry install --no-dev --no-interaction --no-ansi
EXPOSE 8000
CMD "poetry run uvicorn app.main:api --host 0.0.0.0 --port 8000 "