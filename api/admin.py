from django.contrib import admin

# Register your models here.

from .models import Exp, Skills, Projects

admin.site.register(Exp)
admin.site.register(Skills)
admin.site.register(Projects)
