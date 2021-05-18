from django.contrib import admin
from import_export.admin import ExportMixin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserProfile,EmailVerifyRecord
@admin.register(UserProfile)
class UserProfileAdmin(ExportMixin,UserAdmin):
    list_per_page = 20
    list_display = ('username','last_login','is_superuser','is_staff','is_active','date_joined')

@admin.register(EmailVerifyRecord)
class EmailVerifyAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ('email','send_time')
    list_per_page = 20
