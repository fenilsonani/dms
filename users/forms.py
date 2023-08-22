from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import NormalUser


class NormalUserForm(forms.ModelForm):

    class Meta:
        model = NormalUser
        fields = ['user', 'business', 'is_admin']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name','last_name']
