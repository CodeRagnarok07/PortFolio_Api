from django.shortcuts import render, get_object_or_404
from .models import Projects, Skills, Formation, Exp
# Create your views here.

def home(request):
    projects = Projects.objects.all()
    skills = Skills.objects.all()
    formation = Formation.objects.all()
    exp = Exp.objects.all()

    ctx = {
        "projects":projects,
        "exp":exp,
        "formation":formation,
        "skills":skills,
    }

    return render(request, 'core/home.html', ctx)

def project_view(request, project_slug):
    project = get_object_or_404(Projects, slug=project_slug)
    used_skill = Skills.objects.filter(projects=project)

    ctx = {
        "project":project,
        "used_skill": used_skill,
    }

    return render(request, 'core/project_view.html', ctx)

def skill_view(request, skill_slug):
    skill = get_object_or_404(Skills, slug=skill_slug)
    projects = Projects.objects.filter(skills=skill)

    ctx = {
        "skill":skill,
        "projects":projects,
    }
    return render(request, 'core/skill_view.html', ctx)
