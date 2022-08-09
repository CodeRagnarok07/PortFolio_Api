from django.contrib import admin

# Register your models here.

from django_summernote.admin import SummernoteModelAdmin
from .models import Skills

# Apply summernote to all TextField in model.


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'description'


admin.site.register(Skills, SomeModelAdmin)
