import shutil
import os,requests

from django.contrib import admin
from django.db.models.signals import post_delete, pre_save,post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.safestring import mark_safe  # imageField
from import_export.admin import ImportExportModelAdmin

from .models import Gallery, Photos
from .models import SourcesCore, ImageSource, ImageMatch
from .serializers import GallerySerializers
from .utils import genGalleryCache

# Register your models here.

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


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    try:
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    except:
        pass


def delete_dir(dir):
    if not dir:
        return
    fname = str(settings.MEDIA_ROOT)+dir
    del_file(fname)


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
            img = mark_safe('<img src="%s" height="20" />' %
                            os.path.join(settings.MEDIA_URL, str(obj.pic_thumb)))
        except Exception as e:
            img = ''
        return img
    logo.short_description = '缩略图'
    list_display = ('id', 'pic', 'logo', 'pic_webp')
    list_per_page = 20
    readonly_fields = ('pic_thumb', 'pic_webp')


# 删除文件同时删除资源图片文件
@receiver(post_delete, sender=Photos)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'image')
    thumb = getattr(instance, 'image_thumb')
    webp = getattr(instance, 'image_webp')
    delete_image(files)
    delete_image(thumb)
    delete_image(webp)

# @receiver(post_save, sender= Photos)
# def delete_old_image(sender, instance, **kwargs):
#     if hasattr(instance, '_current_image_file'):
#         if instance._current_imagen_file != instance.image.path:
#             instance._current_imagen_file.delete(save=False)

# Gallery变更保存后的操作
@receiver(post_save, sender=Gallery)
@receiver(post_delete, sender=Gallery)
def post_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    genGalleryCache()

@receiver(pre_save, sender=Photos)
@receiver(pre_save, sender=Gallery)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_img = instance.image.path
        except:
            new_img = None
        if new_img != old_img:
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
# 更新image_thumb的操作
@receiver(pre_save, sender=Photos)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image_thumb file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image_thumb.path
        try:
            new_img = instance.image_thumb.path
        except:
            new_img = None
        if new_img != old_img:
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass
    
# 更新image_webp的操作
@receiver(pre_save, sender=Photos)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image_webp file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image_webp.path
        try:
            new_img = instance.image_webp.path
        except:
            new_img = None
        if new_img != old_img:
            if os.path.exists(old_img):
                os.remove(old_img)
    except:
        pass


@receiver(post_delete, sender=Gallery)
def delete_upload_files(sender, instance, **kwargs):
    files = getattr(instance, 'name')
    fileId = getattr(instance, 'id')
    delete_dir('/images/gallery/'+str(fileId))
    delete_dir('/images/gallery/cover/'+str(files))


@admin.register(ImageMatch)
class ImageMatchAdmin(ImportExportModelAdmin):
    list_display = ('id', 'img_id', 'type', 'description')
    list_per_page = 20


class PhotosInline(admin.StackedInline):
    model = Photos
    verbose_name = '相册'
    fields = ['image', 'description', 'adress', 'location']
    readonly_fields = ('size', 'image_thumb', 'image_webp')
    # def has_add_permission(self, request, obj=None):
    #     return False


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotosInline
    ]
    list_display = ('name', 'type', 'description')
