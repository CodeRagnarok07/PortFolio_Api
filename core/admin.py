from ast import For
from django.contrib import admin
from .models import Projects, Skills, Formation, Exp

# Register your models here.

admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Formation)
admin.site.register(Exp)