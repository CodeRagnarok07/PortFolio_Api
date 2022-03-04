from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExpSerializers, SkillsSerializers, ProjectsSerializers
from .models import Exp, Skills, Projects
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser

# Create your views here.


class ExpView(viewsets.ModelViewSet):
    serializer_class = ExpSerializers
    queryset = Exp.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [BasePermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializers
    queryset = Skills.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [BasePermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [BasePermission]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
