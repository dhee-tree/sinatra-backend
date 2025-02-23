# Generated by Django 5.1.6 on 2025-02-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('skills', '0002_skill_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='users', to='skills.skill'),
        ),
    ]
