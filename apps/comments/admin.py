from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from .models import Suggestion

@admin.register(Suggestion)
class BlogAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ('id', 'suggest_content')
    list_per_page = 20
