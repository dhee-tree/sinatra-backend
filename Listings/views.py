from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Listing, Subscription
from .serializer import ListingSerializer, SubscriptionSerializer


class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]


class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'


class ListingUpdateView(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def perform_update(self, serializer):
        if self.request.user == self.get_object().owner:
            serializer.save()
        else:
            return Response({"error": "You are not the owner of this listing."}, status=status.HTTP_403_FORBIDDEN)


class ListingDeleteView(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'

    def perform_destroy(self, instance):
        if self.request.user == instance.owner:
            instance.delete()
        else:
            return Response({"error": "You are not the owner of this listing."}, status=status.HTTP_403_FORBIDDEN)


class SubscribeToListingView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, uuid, *args, **kwargs):
        listing = Listing.objects.get(uuid=uuid)
        subscription, created = Subscription.objects.get_or_create(user=request.user, listing=listing)
        if created:
            return Response({"message": "Successfully subscribed to the listing."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Already subscribed to this listing."}, status=status.HTTP_200_OK)
