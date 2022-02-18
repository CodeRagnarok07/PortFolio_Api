from django.shortcuts import render
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