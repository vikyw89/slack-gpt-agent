FROM python:3.12-slim AS base
RUN apt-get update -y
RUN apt-get install -y
RUN apt-get install curl -y
RUN pip install poetry

FROM base AS codebase
WORKDIR /app
COPY . .

FROM codebase AS development
WORKDIR /app
RUN poetry install
EXPOSE 8000
CMD "poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

FROM codebase AS production
WORKDIR /app
RUN poetry install --no-dev
EXPOSE 8000
CMD "poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 "