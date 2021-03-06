from __future__ import absolute_import, unicode_literals
from datetime import timezone

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ScheduleWFMTTaskProject.settings")

app=Celery("ScheduleWFMTTaskProject")

app.conf.enable_utc=False

app.conf.update(timezone="Asia/Kolkata")

app.config_from_object("django.conf:settings",namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f" Request :{self.request!r}")#this will consider __str__ rather than __repr__