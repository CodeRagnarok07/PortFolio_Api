from rest_framework import serializers
from portfolio.models import Skills
# from django.contrib.auth.models import User



class SkillsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class ExpSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Exp
#         fields = '__all__'

# class ProjectsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Projects
#         fields = '__all__'
#     skills = SkillsSerializers(many=True)
