from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# Set default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

app = Celery('financeiro')

# Using a string here means the worker doesn't need to pickle the object
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')