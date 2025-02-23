from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from User.models import CustomUser
from .models import Skill
from .serializers import SkillSerializer
from rest_framework import status
from rest_framework.response import Response


class UserSkillsView(generics.ListAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_uuid = self.kwargs['user_uuid']
        user = get_object_or_404(CustomUser, uuid=user_uuid)
        return Skill.objects.filter(users=user)

class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

class AsignSkillView(generics. GenericAPIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        skill_uuid = self.kwargs['skill_uuid']

        skill = get_object_or_404(Skill, uuid=skill_uuid)
        user= request.user

        # Assign the skill to the user
        user.skills.add(skill)

        # Return a success response
        return Response(
            {"message": f"Skill '{skill.name}' successfully assigned to user ."},
            status=status.HTTP_200_OK
        )

class DeleteUserSkillView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_uuid = self.kwargs['user_id']
        skill_id = self.kwargs['skill_id']
        user = get_object_or_404(CustomUser, uuid=user_uuid)
        skill = get_object_or_404(Skill, uuid=skill_id)
        if skill not in user.skills.all():
            raise Http404("Skill not found for this user")
        return skill

    def destroy(self, request, *args, **kwargs):
        skill = self.get_object()
        user_uuid = self.kwargs['user_uuid']
        user = get_object_or_404(CustomUser, uuid=user_uuid)
        user.skills.remove(skill)
        return Response({"message": "Skill deleted successfully."}, status=status.HTTP_204_NO_CONTENT)