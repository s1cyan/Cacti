from django import forms
from models import User


class RegistrationForm(forms.ModelForm):
    # email = forms() # wat
    email = forms.EmailField()
    username = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64)
    password_confirmation = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('email','username','password','password_confirmation')




