from django.urls import path

<<<<<<< Updated upstream
from .views import UserListView, UserSignupView, UserMeView
from skills import views 
=======
from .views import UserListView, UserSignupView 
from skills.views import UserSkillsView, SkillListView, AsignSkillView
>>>>>>> Stashed changes

urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    # path('me/', CurrentUserView.as_view(), name='current_user'),
    path('signup', UserSignupView.as_view(), name='signup'),
<<<<<<< Updated upstream
    path('users/<int:user_id>/skills/', views.user_skills, name='user-skills'),
    path('me', UserMeView.as_view(), name='user-me'),
=======
    path('<int:user_id>/skills', UserSkillsView.as_view(), name='user-skills'),
    path ("view/all", SkillListView.as_view(), name='user-viewallskills'),
    path ('assign/<uuid:skill_id>', AsignSkillView.as_view(), name='assign-skill'),
>>>>>>> Stashed changes

]
