from django.urls import path
from .views import (
    ListingCreateView,
    ListingListView,
    ListingDetailView,
    ListingUpdateView,
    ListingDeleteView,
    SubscribeToListingView
)

urlpatterns = [
    path('', ListingListView.as_view(), name='listings-list'),
    path('add', ListingCreateView.as_view(), name='listings-create'),
    path('<uuid:uuid>', ListingDetailView.as_view(), name='listings-detail'),
    path('<uuid:uuid>/edit', ListingUpdateView.as_view(), name='listings-update'),
    path('<uuid:uuid>/delete', ListingDeleteView.as_view(), name='listings-delete'),
    path('<uuid:uuid>/subscribe', SubscribeToListingView.as_view(), name='listings-subscribe'),
]
