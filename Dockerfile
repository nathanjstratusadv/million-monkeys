FROM python:3.12-slim

COPY . .

RUN pip install .

CMD ["celery", "worker", "--loglevel=info"]