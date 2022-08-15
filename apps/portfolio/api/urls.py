from rest_framework.routers import DefaultRouter

from .viewset import SkillsApi, WorksApi, ProjectsApi

portfolio_router = DefaultRouter()
portfolio_router.register(r'skills', SkillsApi)
portfolio_router.register(r'works', WorksApi)
portfolio_router.register(r'projects', ProjectsApi)

urlpatterns = portfolio_router.urls