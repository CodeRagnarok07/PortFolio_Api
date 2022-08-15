from django.urls import path, include
from .views import apiSkills, apiWorks, apiProjects

urlpatterns = [
    path('skills/', apiSkills.as_view()),
    path('works/', apiWorks.as_view()),
    path('projects/', apiProjects.as_view()),

]