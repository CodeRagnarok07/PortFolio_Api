from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from .serializers import SkillsSerializers, ProjectsSerializers ,WorkSerializers
from portfolio.models import Skill, Project, Work

class SkillsApi(viewsets.ViewSet):
    lookup_field = 'pk'
    queryset = Skill.objects.all()
    serializer = SkillsSerializers(queryset, many=True)

    def list(self, request):
        serializer = self.serializer
        return Response(serializer.data)

    def retrieve(self, request, pk=None):    
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = SkillsSerializers(obj)
        return Response(serializer.data)

class ProjectsApi(viewsets.ViewSet):
    lookup_field = 'pk'
    queryset = Project.objects.all()
    serializer = ProjectsSerializers(queryset, many=True)

    def list(self, request):
        serializer = self.serializer
        return Response(serializer.data)

    def retrieve(self, request, pk=None):    
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = ProjectsSerializers(obj)
        return Response(serializer.data)

class WorksApi(viewsets.ViewSet):
    lookup_field = 'pk'
    queryset = Work.objects.all()
    serializer = WorkSerializers(queryset, many=True)

    def list(self, request):
        serializer = self.serializer
        return Response(serializer.data)

    def retrieve(self, request, pk=None):    
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = WorkSerializers(obj)
        return Response(serializer.data)


