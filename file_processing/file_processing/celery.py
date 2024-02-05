import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_processing.settings')
app = Celery('file_processing')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')