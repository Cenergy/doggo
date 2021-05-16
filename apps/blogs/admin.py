from django.contrib import admin

# Register your models here.
from .models import Blog,BlogType

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)
    list_per_page = 20

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_per_page = 20
