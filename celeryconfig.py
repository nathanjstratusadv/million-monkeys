import os

from dotenv import load_dotenv

load_dotenv()

broker_url = f'pyamqp://{os.getenv("RABBITMQ_USER")}:{os.getenv("RABBITMQ_PASS")}@{os.getenv("RABBITMQ_HOST")}'

imports = (
    'app.tasks',
)

result_backend = 'rpc://'
# result_backend = 'db+sqlite:///results.db'

task_serializer = 'json'
accept_content = [
    'json'
]
result_serializer = 'json'


task_annotations = {
    'tasks.add': {
        'rate_limit': '10/s'
    }
}