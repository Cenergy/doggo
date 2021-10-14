from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from .models import Suggestion, FriendLinks


@admin.register(Suggestion)
class BlogAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'suggest_content')
    list_per_page = 20


@admin.register(FriendLinks)
class FriendLinksAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'link')
    list_per_page = 20
