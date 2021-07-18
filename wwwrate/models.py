from django.db import models
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('images', default='image/upload/v1626430054/default_zogkvr.png')
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=1000, blank=True)