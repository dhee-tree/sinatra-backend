from django.db import models


class Skill (models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.name

