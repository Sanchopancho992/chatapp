from django import forms
from .models import Room, Message, User

class SignupForm(forms.UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password']

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)

