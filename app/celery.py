from celery import Celery
from dotenv import load_dotenv

load_dotenv()

app = Celery(
    main='tasks',
)

app.config_from_object('celeryconfig')
