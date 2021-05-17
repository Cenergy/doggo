from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Blog,BlogType

@admin.register(BlogType)
class BlogTypeAdmin(ImportExportModelAdmin):
    list_display = ('type_name',)
    list_per_page = 20

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'content')
    list_per_page = 20
