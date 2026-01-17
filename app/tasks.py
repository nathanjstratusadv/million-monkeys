import os

from celery import Celery
from dotenv import load_dotenv


load_dotenv()

app = Celery(
    main='tasks',
    backend='rpc://',
    broker=f'pyamqp://{os.getenv("RABBITMQ_USER")}:{os.getenv("RABBITMQ_PASS")}@{os.getenv("RABBITMQ_HOST")}'
)

@app.task
def add(x, y):
    return x + y