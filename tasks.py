from celery import Celery, Task
from celery.utils.log import get_task_logger
from datetime import datetime, timedelta
from celery.signals import worker_init
import time

app = Celery(
    'rentnumbot',
    broker='amqp://guest:guest@localhost/celerybot'
)


@app.task(name="sleeping", bind=True)
def reply_message(self, token, chat_id, message):
    print('start')
    time.sleep(7)
    print('stop')
