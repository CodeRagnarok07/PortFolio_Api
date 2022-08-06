from .serializers import ExpSerializers, SkillsSerializers, ProjectsSerializers, UserSerializer
from .models import Exp, Skills, Projects
from rest_framework import viewsets, permissions, status

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.


class AdminLogin(APIView):
    permission_classes = (permissions.AllowAny,)  # tuple
    queryset = User.objects.none()

    def get(self, request, format=None):
        if(request.method == 'GET'):
            try:
                user = UserSerializer(request.user)
                return Response(
                    {'success': user.data},
                    status=status.HTTP_200_OK
                )
            except:
                return Response(
                    {'error': 'error 505 algo no funciona correctamente', },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {'error': 'No allow POST method ', },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ExpView(viewsets.ModelViewSet):
    serializer_class = ExpSerializers
    queryset = Exp.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.BasePermission]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializers
    queryset = Skills.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.BasePermission]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class ProjectsView(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializers
    queryset = Projects.objects.all()

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.BasePermission]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
