# Generated by Django 3.0 on 2021-07-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wwwrate', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='wwwrate.Project'),
        ),
    ]
