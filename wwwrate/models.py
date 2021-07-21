from django.db import models
from django.forms.models import modelform_factory
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    profile_pic = CloudinaryField('images', default='image/upload/v1626430054/default_zogkvr.png')

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
    repository_url = models.CharField(max_length=200, blank=True)
    live_url = models.CharField(max_length=200, blank=True)
    
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')

    @property
    def get_average_design_rating(self):
        reviews = Review.objects.all().filter(project=self)
        design_ratings = []
        for review in reviews:
            design_ratings.append(review.design_rating)
        if len(design_ratings) != 0:
            average_design_rating = sum(design_ratings)/len(design_ratings)
        else:
            average_design_rating = 0.0

        return average_design_rating
    @property
    def get_average_usability_rating(self):
        reviews = Review.objects.all().filter(project=self)
        usability_ratings = []
        for review in reviews:
            usability_ratings.append(review.usability_rating)
        if len(usability_ratings) != 0:
            average_usability_rating = sum(usability_ratings)/len(usability_ratings)
        else:
            average_usability_rating = 0.0

        return average_usability_rating
    @property
    def get_average_content_rating(self):
        reviews = Review.objects.all().filter(project=self)
        content_ratings = []
        for review in reviews:
            content_ratings.append(review.content_rating)
        if len(content_ratings) != 0:
            average_content_rating = sum(content_ratings)/len(content_ratings)
        else:
            average_content_rating = 0.0

        return average_content_rating

    @property
    def get_overall_average_rating(self):
        return round((self.get_average_design_rating + self.get_average_usability_rating + self.get_average_content_rating)/3,1)

    class Meta:
        ordering = ['posted_at']


    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField(max_length=1000)
    design_rating = models.IntegerField()
    usability_rating = models.IntegerField()
    content_rating = models.IntegerField()
    review_date = models.DateTimeField(auto_now_add=True)

    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews', null=True)

    @property
    def average_rating(self):
        return round(((self.design_rating + self.usability_rating + self.content_rating)/3),1)