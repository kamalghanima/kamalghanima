from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  email = forms.CharField(max_length=255,required=1,widget=forms.EmailInput())

  class Meta :
    model = User
    fields = ['username','email','password1','password2']