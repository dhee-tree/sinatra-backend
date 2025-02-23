from django.urls import path

from .views import UserListView, UserSignupView, UserMeView
from skills import views 

urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    # path('me/', CurrentUserView.as_view(), name='current_user'),
    path('signup', UserSignupView.as_view(), name='signup'),
    path('users/<int:user_id>/skills/', views.user_skills, name='user-skills'),
    path('me', UserMeView.as_view(), name='user-me'),

]
