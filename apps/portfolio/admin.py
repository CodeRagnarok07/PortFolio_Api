from django.contrib import admin

# Register your models here.

from django_summernote.admin import SummernoteModelAdmin
from .models import Skill, Work, Project

# Apply summernote to all TextField in model.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'description'


admin.site.register(Skill, SomeModelAdmin)
admin.site.register(Work, SomeModelAdmin)
admin.site.register(Project, SomeModelAdmin)
