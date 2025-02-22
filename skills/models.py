from django.db import models
from User.models import CustomUser


class Skill (models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)  # Optional: Skill category
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

CustomUser.add_to_class('skills', models.ManyToManyField(Skill, related_name='users'))
