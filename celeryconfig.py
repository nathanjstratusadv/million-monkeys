import os

from dotenv import load_dotenv

load_dotenv()

broker_url = f'pyamqp://{os.getenv("RABBITMQ_USER")}:{os.getenv("RABBITMQ_PASS")}@{os.getenv("RABBITMQ_HOST")}'

# List of modules to import when the Celery worker starts.
imports = (
    'app.tasks',
)

result_backend = 'rpc://'
## Using the database to store task state and results.

result_backend = 'db+sqlite:///results.db'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}