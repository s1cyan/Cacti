from django import forms
from models import User, ScheduleBlock, Day


class ScheduleBlockForm(forms.ModelForm):
    """
    This form is associated with the ScheduleBlock Model found in
    models.py.
    """
    class Meta:
        model = ScheduleBlock
        fields = ['start_time', 'end_time',
                  'schedule_name', 'schedule_desc']


class DayForm(forms.ModelForm):
    """
    This form is associated with the Day Model found in
    models.py.
    """
    class Meta:
        model = Day
        fields = ['date']
