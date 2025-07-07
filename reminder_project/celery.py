import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder_project.settings')
app = Celery('reminder_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()