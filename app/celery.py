from celery import Celery
from dotenv import load_dotenv

load_dotenv()

from monkeys.setup import setup

setup()

app = Celery(
    main='tasks',
)

app.config_from_object('celeryconfig')
