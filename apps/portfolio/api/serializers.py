from rest_framework import serializers
from portfolio.models import Skill, Project, Work
# from django.contrib.auth.models import User


class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class WorkSerializers(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'
    skills = SkillsSerializers(many=True)


class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    skills = SkillsSerializers(many=True)

    def get_image_url(self, obj):
        return obj.img.url
