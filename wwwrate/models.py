from django.db import models
from django.forms.models import modelform_factory
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=1000, blank=True)