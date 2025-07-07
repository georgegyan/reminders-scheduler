from django import forms
from .models import Reminder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12 mb-3'),
            ),
            Row(
                Column('description', css_class='form-group col-md-12 mb-3'),
            ),
            Row(
                Column('due_date', css_class='form-group col-md-6 mb-3'),
                Column('priority', css_class='form-group col-md-6 mb-3'),
            ),
            Submit('submit', 'Save Reminder', css_class='btn btn-primary w-100')
        )