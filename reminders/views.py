from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.safestring import mark_safe
import json
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Reminder
from .forms import ReminderForm

@login_required
def profile(request):
    return render(request, 'profile.html')
class ReminderListView(LoginRequiredMixin, ListView):
    model = Reminder
    template_name = 'reminders/reminder_list.html'
    context_object_name = 'reminders'

    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user).order_by('due_date')

class ReminderCreateView(LoginRequiredMixin, CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminders/reminder_form.html'
    success_url = reverse_lazy('reminder_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminders/reminder_form.html'
    success_url = reverse_lazy('reminder_list')

class ReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = Reminder
    template_name = 'reminders/reminder_confirm_delete.html'
    success_url = reverse_lazy('reminder_list')

class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'reminders/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reminders = Reminder.objects.filter(user=self.request.user)
        events = []
        for reminder in reminders:
            events.append({
                'title': reminder.title,
                'start': reminder.due_date.isoformat(),
                'end': (reminder.due_date + timezone.timedelta(hours=1)).isoformat(),
                'color': '#dc3545' if reminder.priority == 'H' else 
                        '#ffc107' if reminder.priority == 'M' else '#0d6efd',
            })
        context['events'] = mark_safe(json.dumps(events))
        return context