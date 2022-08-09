from rest_framework import serializers
from .models import Exp, Skills, Projects
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ExpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exp
        fields = '__all__'


class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class ProjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
    skills = SkillsSerializers(many=True)
