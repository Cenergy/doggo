from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Blog,BlogType

@admin.register(BlogType)
class BlogTypeAdmin(ImportExportModelAdmin):
    list_display = ('id','type_name')
    list_per_page = 20

@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'content')
    list_per_page = 20
