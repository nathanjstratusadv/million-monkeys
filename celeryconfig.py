import os

from dotenv import load_dotenv

load_dotenv()

broker_url = f'pyamqp://{os.getenv("RABBITMQ_USER")}:{os.getenv("RABBITMQ_PASS")}@{os.getenv("RABBITMQ_HOST")}'

imports = (
    'app.tasks',
)

result_backend = f'db+mysql+mysqlconnector://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASS")}@{os.getenv("MYSQL_HOST")}/million_monkeys'

task_serializer = 'json'
accept_content = [
    'json'
]
result_serializer = 'json'
