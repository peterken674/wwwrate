# Generated by Django 3.0 on 2021-07-18 19:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wwwrate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='image/upload/v1626430054/default_zogkvr.png', max_length=255, verbose_name='images'),
        ),
    ]
