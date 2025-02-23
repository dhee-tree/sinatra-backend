from django.urls import path

from .views import UserListView, UserSignupView, CurrentUserView
# from skills.views import UserSkillsView, SkillListView, AsignSkillView

urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    path('me/', CurrentUserView.as_view(), name='current_user'),
    path('signup', UserSignupView.as_view(), name='signup'),
    # path('<int:user_id>/skills', UserSkillsView.as_view(), name='user-skills'),
    # path ("view/all", SkillListView.as_view(), name='user-viewallskills'),
    # path ('assign/<uuid:skill_id>', AsignSkillView.as_view(), name='assign-skill'),

]
