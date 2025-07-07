from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from .models import Reminder
import json

@receiver(post_save, sender=Reminder)
def schedule_reminder(sender, instance, created, **kwargs):
    if created:
        schedule, _ = CrontabSchedule.objects.get_or_create(
            minute='*/5',  # Every 5 minutes
            hour='*',
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Reminder-{instance.id}',
            task='reminders.tasks.send_reminder_emails',
            args=json.dumps([instance.id]),
            one_off=True,
            start_time=instance.due_date,
        )