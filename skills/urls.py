from django.urls import path
from . import views  

urlpatterns = [
    path('', views.skill_list, name='skill_list'),  
    path('users/<int:user_id>/', views.user_skills, name='user_skills'), 
]