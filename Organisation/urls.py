from django.urls import path
from .views import OrganisationListCreateView, OrganisationDetailView

urlpatterns = [
    path('', OrganisationListCreateView.as_view(), name='organisation-list-create'),
    path('<uuid:uuid>', OrganisationDetailView.as_view(), name='organisation-detail'),
]
