# BASE
FROM python:3.11-slim AS base
RUN apt-get update && apt-get install -y curl && apt-get install -y wget
RUN pip install poetry==1.7.1

# CODEBASE
FROM base AS codebase
WORKDIR /app
COPY . .

# DEVELOPMENT TARGET
FROM codebase AS development
RUN poetry install --no-directory
EXPOSE 8000
CMD poetry run dev


# PRODUCTION TARGET
FROM codebase AS production
RUN poetry install --no-directory --without dev
EXPOSE 8000
CMD poetry run prod