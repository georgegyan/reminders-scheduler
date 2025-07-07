from django.urls import path
from .views import (ReminderListView, ReminderCreateView, 
                    ReminderUpdateView, ReminderDeleteView)

urlpatterns = [
    path('', ReminderListView.as_view(), name='reminder_list'),
    path('new/', ReminderCreateView.as_view(), name='add_reminder'),
    path('<int:pk>/edit/', ReminderUpdateView.as_view(), name='edit_reminder'),
    path('<int:pk>/delete/', ReminderDeleteView.as_view(), name='delete_reminder'),
]