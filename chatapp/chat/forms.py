from django import forms
from .models import Room, Message, User

class LoginForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password']
