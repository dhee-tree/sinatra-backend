from django.contrib import admin
from .models import (SideQuest, UserQuest, Reward, Leaderboard)

admin.site.register(SideQuest)
admin.site.register(UserQuest)
admin.site.register(Leaderboard)
admin.site.register(Reward)