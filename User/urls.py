from django.urls import path

from .views import UserListView, CurrentUserView


urlpatterns = [
    path('getOrganisationUsers', UserListView.as_view(), name='', ),
    path('me/', CurrentUserView.as_view(), name='current_user'),
]
