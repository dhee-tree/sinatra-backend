import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

class SideQuest(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField()

    def __str__(self):
        return self.title

class UserQuest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quest = models.ForeignKey(SideQuest, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def complete(self):
        self.completed = True
        self.completed_at = timezone.now()
        self.save()

class Reward(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    badge = models.CharField(max_length=100, null=True, blank=True)
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.points} points"

class Leaderboard(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)

    def update_leaderboard(self, points):
        self.points += points
        self.save()
