from celery import Celery
from mm import celeryconfig

app = Celery("my_task")
app.config_from_object("mm.celeryconfig")