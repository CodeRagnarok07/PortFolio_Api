from django.urls import path
from .api.view import apiSkills

urlpatterns = [
    path('skills/', apiSkills.as_view()),

]