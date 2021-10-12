from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.conf import settings
from PIL import Image

THUMB_ROOT = "images/thumb" # 这个是最终的缩略图要保存的路径

# Create your models here.
import datetime

from utils import get_random

class SourcesCore(models.Model):
    SOURCES_TYPE = (
        (1, "视频资源"),
        (2, "专业资源"),
        (3, "软件资源"),
        (0, "其他资源"),
    )
    id=models.AutoField(primary_key=True,verbose_name="资源ID")
    sourcename=models.CharField(max_length=100,verbose_name='资源名称')
    sourceurl=models.URLField(verbose_name="资源地址",null=True,blank=True,help_text="可不填，会自动从资源描述里读取")
    code=models.CharField(max_length=20,verbose_name="提取码",null=True,blank=True,help_text="可不填，会自动从资源描述里读取")
    sourcedesc = models.CharField(max_length=200, null=True,blank=True,verbose_name='综合描述', help_text="默认是百度云的资源，如果不是，上面两个请填写")
    question_type = models.IntegerField(choices=SOURCES_TYPE, verbose_name="资源类型", help_text="资源类型", default=0)
    source_img=models.ImageField(null=True,blank=True,upload_to=get_random.timeStampRandom('sources/images/'),default="sources/images/default.png",verbose_name="资源图片")
    send_time=models.DateField(default=datetime.datetime.now,verbose_name='添加时间')

    def save(self, *args, **kwargs):
        if self.sourceurl is None:
            abc = self.sourcedesc.split()
            urllink = abc[0].split("链接:")
            urlcode = abc[-1].split("密码:")
            self.sourceurl=urllink[-1]
            self.code=urlcode[-1]
        else:
            pass
        return super(SourcesCore, self).save(*args, **kwargs)

    class Meta:
        verbose_name="资源集合"
        verbose_name_plural=verbose_name
# 因为有API有次数限制
class SourceLimit(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    num_count=models.IntegerField(default=50,verbose_name="次数")
    limit_time=models.DateField(default=datetime.date.today,verbose_name='有效时间')

    class Meta:
        verbose_name="次数管理"
        verbose_name_plural=verbose_name

import os,time
def modify_path(instance, filename):
    '''
    重定义图片保存路径
    :param instance: self
    :param filename: 文件名
    :return: 新路径
    '''
    # ext = filename.split('.').pop()
    # now_date = datetime.datetime.now().strftime('%Y%m%d')
    # now_time = int(time.time())
    # filename = '{0}{1}.{2}'.format(now_date, now_time, ext)
    return os.path.join('images', filename) # 系统路径分隔符差异，增强代码重用性
def make_thumb(path, size = 180):
    pixbuf = Image.open(path)
    width, height = pixbuf.size

    if width > size:
        delta = width / size
        height = int(height / delta)
        pixbuf.thumbnail((size, height), Image.ANTIALIAS)
    return pixbuf
import os, datetime, uuid
def generate_filename_thumb(instance, filename):
    directory_name = datetime.datetime.now().strftime('upload_img/thumb/%Y/%m')
    filename = uuid.uuid4().hex + os.path.splitext(filename)[-1]
    return os.path.join(directory_name, filename)

class PicTest(models.Model):
    id=models.AutoField(primary_key=True,verbose_name="ID")
    name=models.CharField(max_length=100,verbose_name='名称')
    pic = models.ImageField(upload_to=modify_path,unique=True)
    pic_thumb = models.ImageField(upload_to='images/thumb', null=True)
    class Meta:
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name
        ordering = ['id']
    def save(self):
        super(PicTest, self).save()  # 将上传的图片先保存一下，否则报错
        base, ext = os.path.splitext(os.path.basename(self.pic.url))
        filename=os.path.basename(self.pic.url)
        savedPath=self.pic.path
        thumb_pixbuf = make_thumb(savedPath)
        relate_thumb_path = os.path.join(THUMB_ROOT,filename)
        thumb_path = os.path.join(settings.MEDIA_ROOT, relate_thumb_path)
        thumb_abspath = os.path.join(settings.MEDIA_ROOT, THUMB_ROOT)
        if not os.path.exists(thumb_abspath):
            os.makedirs(thumb_abspath)
        thumb_pixbuf.save(os.path.abspath(thumb_path))
        self.pic_thumb = ImageFieldFile(self, self.pic_thumb, relate_thumb_path)
        super(PicTest, self).save() # 再保存一下，包括缩略图等