

# from django.contrib.auth.models import User

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status, viewsets


from .serializers import SkillsSerializers
from portfolio.models import Skills


class apiSkills(APIView):  # http://127.0.0.1:8000/api/words/
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, format=None):
        queryset = Skills.objects.all()
        serializer = SkillsSerializers(queryset, many=True)

        try:
            return Response({"success": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {
                    "error": "error 505 internal server error",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )