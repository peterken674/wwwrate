from django.db import models
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('images', default='image/upload/v1626430054/default_zogkvr.png')
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=1000, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    screenshot = CloudinaryField('images')
    posted_at = models.DateTimeField(auto_now_add=True)
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField(max_length=1000)
    design_rating = models.IntegerField()
    usability_rating = models.IntegerField()
    content_rating = models.IntegerField()
    review_date = models.DateTimeField(auto_now_add=True)

    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)