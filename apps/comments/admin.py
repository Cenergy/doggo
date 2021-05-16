from django.contrib import admin

# Register your models here.
from .models import Suggestion

@admin.register(Suggestion)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'suggest_content')
    list_per_page = 20
