from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
app = Celery('conf')

app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('\nRequest: {0!r}'.format(self.request))
    print('\nhello world')


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'test',
        'schedule': 5.0,
    },
    'add-every-minute-contrab': {
        'task': 'get_all_data',
        'schedule': crontab(minute=1),
    },
}
