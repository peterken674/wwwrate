# Generated by Django 3.0 on 2021-07-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wwwrate', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=1000)),
                ('design_rating', models.IntegerField()),
                ('usability_rating', models.IntegerField()),
                ('content_rating', models.IntegerField()),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wwwrate.Project')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='wwwrate.Profile')),
            ],
        ),
    ]