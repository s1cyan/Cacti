from django import forms
from models import User


class RegistrationForm(forms.ModelForm):
    email = forms() # wat
    class Meta:
        model = User
        field = ('email',)