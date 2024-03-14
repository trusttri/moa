from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

# class Meta:
# 	model = User
# 	#fields = ["username", "email", "password1", "password2"]
# 	username = forms.CharField()
# 	email = forms.EmailField()
# 	password1 = forms.CharField()
# 	password2 = forms.CharField()