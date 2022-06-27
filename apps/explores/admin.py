from django.contrib import admin
from .models import WebSiteConfig
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(WebSiteConfig)
class WebBlogConfigAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'save_path', 'description')
    list_per_page = 20
    verbose_name = '配置'
