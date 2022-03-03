from rest_framework import serializers
from .models import Exp, Skills, Projects


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
