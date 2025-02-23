from django.contrib import admin

from Listings.models import Subscription, Listing

# Register your models here.
admin.site.register(Subscription)
admin.site.register(Listing)