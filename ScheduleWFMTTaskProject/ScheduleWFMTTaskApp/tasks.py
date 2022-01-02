from __future__ import absolute_import, unicode_literals
from django.core.management import call_command
from celery import shared_task

@shared_task
def add(x,y):
    return x+y

@shared_task
def backup_db():
    with open("db.json","w") as f:
        call_command("dumpdata",stdout=f)
        
    