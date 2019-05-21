from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    names = forms.CharField(max_length=100, required=True)
    surnames = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250)

    class Meta:
        model = User
        fields = {'username', 'names', 'surnames', 'email', 'password1', 'password2'}

