from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organisation
from .serializers import OrganisationSerializer
from rest_framework.permissions import IsAuthenticated

class OrganisationListCreateView(generics.ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class OrganisationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'uuid'


class OrganisationGetUserOrganisationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        organisations = Organisation.objects.filter(created_by=request.user)
        serializer = OrganisationSerializer(organisations, many=True)
        return Response(serializer.data)