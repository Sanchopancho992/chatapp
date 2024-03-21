from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Message, User

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1']

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = ['name', 'description', 'host']