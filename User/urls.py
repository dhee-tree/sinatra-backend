from django.urls import path

from .views import UserListView, UserSignupView

urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    # path('me/', CurrentUserView.as_view(), name='current_user'),
    path('signup', UserSignupView.as_view(), name='signup'),
]
