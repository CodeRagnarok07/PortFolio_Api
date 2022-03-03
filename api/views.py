from django.shortcuts import render
from rest_framework import viewsets    
from .serializers import ExpSerializers, SkillsSerializers, ProjectsSerializers
from .models import Exp, Skills, Projects

# Create your views here.

class ExpView(viewsets.ModelViewSet):
    serializer_class = ExpSerializers      
    queryset = Exp.objects.all()            


class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializers      
    queryset = Skills.objects.all()            

class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializers      
    queryset = Projects.objects.all()            