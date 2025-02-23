# Generated by Django 5.1.6 on 2025-02-23 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='users', to='Skills.skill'),
        ),
    ]
