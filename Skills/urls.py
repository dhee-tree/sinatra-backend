from django.urls import path
from .views import UserSkillsView, SkillListView, DeleteUserSkillView  

urlpatterns = [
    path('', SkillListView.as_view(), name='skill_list'),  
    path('users/<int:user_id>/', UserSkillsView.as_view(), name='user_skills'), 
    path('users/<int:user_id>/skills/<int:skill_id>/delete/', DeleteUserSkillView.as_view(), name='delete-user-skill'),
    
]