from django.urls import path
from .views import OrganisationListCreateView, OrganisationDetailView, OrganisationGetUserOrganisationsView

urlpatterns = [
    path('', OrganisationListCreateView.as_view(), name='organisation-list-create'),
    path('<uuid:uuid>', OrganisationDetailView.as_view(), name='organisation-detail'),
    path('my', OrganisationGetUserOrganisationsView.as_view(), name='user-organisations'),

]
