import os
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.utils.safestring import mark_safe  # imageField

# Register your models here.

# Register your models here.
from .models import SourcesCore, ImageSource,ImageMatch


@admin.register(SourcesCore)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'sourcename')
    list_per_page = 20

def delete_image(files):
    if not files:
        return
    fname = os.path.join(settings.MEDIA_ROOT, str(files))
    if os.path.isfile(fname):
        os.remove(fname) 

# 删除文件同时删除资源图片文件
@receiver(post_delete, sender=ImageSource)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'pic')
    thumb = getattr(instance, 'pic_thumb')
    webp = getattr(instance, 'pic_webp')
    delete_image(files)
    delete_image(thumb)
    delete_image(webp)
@admin.register(ImageSource)
class ImageSourceAdmin(ImportExportModelAdmin):
    
    def logo(self, obj):  # imageField显示方法设置,图片路径设为显示图片
        try:
            img = mark_safe('<img src="%s" height="20" />' % os.path.join(settings.MEDIA_URL, str(obj.pic_thumb)))
        except Exception as e:
            img = ''
        return img
    logo.short_description = '缩略图'
    list_display = ('id', 'pic','logo','pic_webp')
    list_per_page = 20
    readonly_fields = ('pic_thumb','pic_webp')
@admin.register(ImageMatch)
class ImageMatchAdmin(ImportExportModelAdmin):
    list_display = ('id', 'img_id','type','description')
    list_per_page = 20
