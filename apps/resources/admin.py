from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import SourcesCore


@admin.register(SourcesCore)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'sourcename')
    list_per_page = 20


