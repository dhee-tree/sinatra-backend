from django.urls import path
from .views import DailyQuestListView, CompleteQuestView, LeaderboardListView, RewardListView

urlpatterns = [
    path('quests', DailyQuestListView.as_view(), name='daily-quests'),
    path('quests/<uuid:user_uuid>/complete', CompleteQuestView.as_view(), name='complete-quest'),
    path('leaderboard', LeaderboardListView.as_view(), name='leaderboard'),
    path('rewards', RewardListView.as_view(), name='user-rewards'),
]
