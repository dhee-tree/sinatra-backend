from django.urls import path

from .views import UserListView, UserSignupView, CurrentUserView
from Skills.views import UserSkillsView, SkillListView, AsignSkillView

urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('signup', UserSignupView.as_view(), name='signup'),
    path('<uuid:user_uuid>/skills', UserSkillsView.as_view(), name='user-skills'),
    path ("view/all", SkillListView.as_view(), name='user-viewallskills'),
    path ('assign/<uuid:skill_uuid>', AsignSkillView.as_view(), name='assign-skill'),
]
