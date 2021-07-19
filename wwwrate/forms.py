from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Project

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'screenshot', 'repository_url', 'live_url']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
