from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from User.models import CustomUser
from User.serializers import UserSignupSerializer, UserSerializer


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cache_key = f'all_users_list_{request.user.organisation.uuid}'
        cached_data = cache.get(cache_key)
        if cached_data:
            queryset = cached_data
        else:
            queryset = CustomUser.objects.filter(organisation=request.user.organisation).order_by('first_name')
            cache.set(cache_key, queryset, timeout=600)

        # serializer = CustomUserSerializer(queryset, many=True)
        serializer = UserSignupSerializer(queryset, many=True)
        return Response(serializer.data)


# class UserDetailView(APIView):
#     permission_classes = [IsAuthenticated]
#     def get_object(self, uuid):
#         try:
#             return CustomUser.objects.get(uuid=uuid)
#         except CustomUser.DoesNotExist:
#             raise Http404
#
#     def get(self, request, uuid, format=None):
#         user = self.get_object(uuid)
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)z


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserSignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "detail": "User created successfully"
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserMeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

