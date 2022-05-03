from django.urls import path
from .views import AdminLogin, ExpView, ProjectsView, SkillsView

urlpatterns = [
    path('', AdminLogin.as_view()), # login
    # path('exp/', ExpView.as_view()), # 
    # path('projects/', ProjectsView.as_view()), # 
    # path('skills/', SkillsView.as_view()), # 
 
]