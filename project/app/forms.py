from django import forms
from .models import StudentModel,StudentQuery

class RegistrationForm(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields='__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model= StudentModel
        fields=('stu_email','stu_password')   

class QueryForm(forms.ModelForm):
    class Meta:
        model= StudentQuery
        fields=('stu_name','stu_email','stu_query')            