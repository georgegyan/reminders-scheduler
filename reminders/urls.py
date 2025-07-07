from django.urls import path
from .views import (ReminderListView, ReminderCreateView, 
                    ReminderUpdateView, ReminderDeleteView, CalendarView)
from .api_views import ReminderListCreateAPIView, ReminderRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('', ReminderListView.as_view(), name='reminder_list'),
    path('new/', ReminderCreateView.as_view(), name='add_reminder'),
    path('<int:pk>/edit/', ReminderUpdateView.as_view(), name='edit_reminder'),
    path('<int:pk>/delete/', ReminderDeleteView.as_view(), name='delete_reminder'),
    path('calendar/', CalendarView.as_view(), name='calendar_view'),
    path('api/reminders/', ReminderListCreateAPIView.as_view(), name='reminder-api-list'),
    path('api/reminders/<int:pk>/', ReminderRetrieveUpdateDestroyAPIView.as_view(), name='reminder-api-detail'),
]