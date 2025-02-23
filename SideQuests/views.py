from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import SideQuest, UserQuest, Reward, Leaderboard
from .serializers import SideQuestSerializer, UserQuestSerializer, RewardSerializer, LeaderboardSerializer

class DailyQuestListView(generics.ListAPIView):
    queryset = SideQuest.objects.all()
    serializer_class = SideQuestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SideQuest.objects.filter(expiration_date__gte=timezone.now().date())

class CompleteQuestView(generics.UpdateAPIView):
    queryset = UserQuest.objects.all()
    serializer_class = UserQuestSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.completed:
            instance.complete()
            self.update_leaderboard(instance.user, instance.quest.points)
            return Response({"message": "Quest completed!"}, status=status.HTTP_200_OK)
        return Response({"message": "Quest already completed."}, status=status.HTTP_400_BAD_REQUEST)

    def update_leaderboard(self, user, points):
        leaderboard, created = Leaderboard.objects.get_or_create(user=user)
        leaderboard.points += points
        leaderboard.streak += 1
        leaderboard.last_completed = timezone.now().date()
        leaderboard.save()

class LeaderboardListView(generics.ListAPIView):
    queryset = Leaderboard.objects.order_by('-points')
    serializer_class = LeaderboardSerializer
    permission_classes = [IsAuthenticated]

class RewardListView(generics.ListAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reward.objects.filter(user=self.request.user)
