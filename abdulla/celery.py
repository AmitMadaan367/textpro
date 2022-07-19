from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abdulla.settings')

app = Celery('abdulla')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

# app.config_from_object(settings, namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

# Celery Beat Settings
app.conf.beat_schedule = {
    'run-fun-every-day-at time': {
        'task': 'ab.tasks.test_func',
        'schedule': crontab(hour='*', minute='*/1'),
        #'args': (2,)
    }
    
}



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')