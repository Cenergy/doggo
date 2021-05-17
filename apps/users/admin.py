from django.contrib import admin
from import_export.admin import ExportMixin

# Register your models here.
from .models import UserProfile,EmailVerifyRecord

@admin.register(UserProfile)
class UserProfileAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ('username','email')
    list_per_page = 20
@admin.register(EmailVerifyRecord)
class EmailVerifyAdmin(ExportMixin,admin.ModelAdmin):
    list_display = ('email','send_time')
    list_per_page = 20
