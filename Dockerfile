FROM python:3.12-slim AS base
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y
RUN apt-get install curl -y
RUN pip install poetry
RUN poetry shell

FROM base AS codebase
COPY . .

FROM codebase AS development
RUN poetry install
EXPOSE 8000
CMD "poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

FROM codebase AS production
RUN poetry install --no-dev
EXPOSE 8000
CMD "poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"