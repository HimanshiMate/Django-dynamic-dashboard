from django import forms
from .models import StudentModel

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields=('stu_email','stu_password')       