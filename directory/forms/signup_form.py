from django import forms
from directory.models import Researcher
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    names = forms.CharField(max_length=30, required=True)
    surnames = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'names', 'surnames', 'email', 'password1', 'password2', )


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = Researcher
        fields = ('profile_picture', 'names', 'surnames', 'institution', 'occupation', 'email',
            'location', 'education', 'skills', 'notes')
