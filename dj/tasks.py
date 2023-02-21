from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.contrib.auth.models import User


@shared_task(name='test')
def test():
    print('\n\n\n Hello world')
    return 'test'


@shared_task(name="get_all_data")
def all_data():
    print("\n\n\nall_data")
    return {'user': 'None'}
