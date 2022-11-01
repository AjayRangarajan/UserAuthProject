from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django import forms



class UserRegistrationForm(UserCreationForm):
    auth_key = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username','password1','password2', 'auth_key']
        exclude = ['id']

class NormalUserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        exclude = ['id']