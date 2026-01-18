FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.9.2 /uv /bin/

RUN adduser --disabled-password --gecos "" celery_user

WORKDIR /app

RUN chown -R celery_user:celery_user /app

COPY ./app/ ./app/
COPY ./monkeys/ ./monkeys/
COPY celeryconfig.py .
COPY dandy_settings.py .
COPY pyproject.toml .
COPY README.md .
COPY .env .

RUN uv pip install -r pyproject.toml --system

USER celery_user

CMD ["celery", "worker", "--loglevel=info"]