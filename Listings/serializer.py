from rest_framework import serializers
from .models import Listing, Subscription


class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['uuid', 'title', 'description', 'created_at', 'updated_at', 'owner']


class SubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    listing = serializers.ReadOnlyField(source='listing.title')

    class Meta:
        model = Subscription
        fields = ['uuid', 'user', 'listing', 'subscribed_at']
