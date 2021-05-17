from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# Register your models here.
from .models import SourcesCore


@admin.register(SourcesCore)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'sourcename')
    list_per_page = 20


