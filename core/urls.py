from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('<str:project_slug>/', project_view, name="project_view"),
    path('skill/<str:skill_slug>/', skill_view, name="skill_view")
]
