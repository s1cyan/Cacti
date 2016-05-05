from django import forms
from models import User, ScheduleBlock, Day, UserHelper


class ScheduleBlockForm(forms.ModelForm):
    """
    This form is associated with the ScheduleBlock Model found in
    models.py.
    """

    class Meta:
        model = ScheduleBlock
        fields = ['start_time', 'end_time',
                  'schedule_name', 'schedule_desc']


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    password_confirmation = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password_confirmation')


class DayForm(forms.ModelForm):
    """
    This form is associated with the Day Model found in
    models.py.
    """
    class Meta:
        model = Day
        exclude = ['user']


class LoginForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('username', 'password')


class SearchForm(forms.Form):
    search_input = forms.CharField(max_length=64)


class PictureForm(forms.Form):
    pfp = forms.ImageField()

    class Meta:
        model = UserHelper
        fields = ('pfps')