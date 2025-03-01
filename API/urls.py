from django.urls import path, include

urlpatterns = [
    path("user/", include("User.urls")),
    path("auth/", include("Auth.urls")),
    path ("skills/", include("skills.urls")),
    path ("sidequests/", include("SideQuests.urls")),
    path ("organisations/", include("Organisation.urls")),
]
