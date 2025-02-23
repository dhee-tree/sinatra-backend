from rest_framework import serializers
from .models import SideQuest, UserQuest, Reward, Leaderboard

class SideQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideQuest
        fields = ['uuid', 'title', 'description', 'points', 'created_at', 'expiration_date']

class UserQuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuest
        fields = ['user', 'quest', 'completed', 'completed_at']

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ['user', 'points', 'badge', 'awarded_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['user', 'points', 'streak', 'last_completed']