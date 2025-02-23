from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Skill
from django.contrib.auth.models import User

def user_skills(request, user_id):
    user = get_object_or_404(User, id=user_id)
    skills = Skill.objects.filter(user=user)
    return render(request, 'skills/user_skills.html', {'user': user, 'skills': skills})

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/skill_list.html', {'skills': skills})

def delete_user_skill(request, user_id, skill_id):
    user = get_object_or_404(User, id=user_id)
    skill = get_object_or_404(Skill, id=skill_id)
    if skill not in user.skills.all():
        raise Http404("Skill not found for this user")

    if request.method == 'POST':
        user.skills.remove(skill) 
        return redirect('skills:user_skills', user_id=user.id)  
    return render(request, 'skills/delete_skill.html', {'skill': skill, 'user': user})