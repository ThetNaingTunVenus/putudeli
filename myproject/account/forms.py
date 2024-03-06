from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class ULoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password1', 'password2', 'is_admin', 'is_emp', 'is_cus']