from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'is_completed']
        read_only_fields = ['id', 'user']