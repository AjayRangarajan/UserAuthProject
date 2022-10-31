from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import User
from django import forms




class AdminUserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    auth_key = forms.CharField(max_length=500)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2', 'auth_key']
        exclude = ['id']
