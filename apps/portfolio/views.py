

# from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets


from .api.serializers import SkillsSerializers, ProjectsSerializers ,WorkSerializers
from .models import Skill, Project, Work

# skills list 
class apiSkills(APIView):  # http://127.0.0.1:8000/api/api/
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        queryset = Skill.objects.all()
        serializer = SkillsSerializers(queryset, many=True, context={'request': request})

        try:
            return Response({"success": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "error": "error 505 internal server error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
# skills View



class apiProjects(APIView):  # http://127.0.0.1:8000/api/projects/
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        queryset = Project.objects.all()
        serializer = ProjectsSerializers(queryset, many=True, context={'request': request})

        try:
            return Response({"success": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "error": "error 505 internal server error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )



class apiWorks(APIView):  # http://127.0.0.1:8000/api/projects/
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        queryset = Work.objects.all().order_by('init_date')
        serializer = WorkSerializers(queryset, many=True, context={'request': request})
        try:
            return Response({"success": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "error": "error 505 internal server error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
