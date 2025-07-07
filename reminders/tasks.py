from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Reminder

@shared_task
def send_reminder_emails():
    now = timezone.now()
    upcoming = Reminder.objects.filter(
        is_completed=False,
        due_date__lte=now + timezone.timedelta(minutes=30),
        due_date__gte=now
    )
    
    for reminder in upcoming:
        send_mail(
            subject=f'⏰ Reminder: {reminder.title}',
            message=f'''
            Hi {reminder.user.username},
            
            This is a reminder for:
            {reminder.title}
            
            Due: {reminder.due_date.strftime("%Y-%m-%d %H:%M")}
            
            Description:
            {reminder.description}
            ''',
            from_email='notifications@yourdomain.com',
            recipient_list=[reminder.user.email],
            fail_silently=True,
        )
        reminder.is_completed = True
        reminder.save()