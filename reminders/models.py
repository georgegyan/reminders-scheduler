from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Reminder(models.Model):
    PRIORITY_CHOICES = [
        ('L', '🔵 Low'),
        ('M', '🟡 Medium'),
        ('H', '🔴 High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']