import os
import json

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


def jsonDefault():
    return {}


def save_json(save_path, data):
    assert save_path.split('.')[-1] == 'json'
    with open(save_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False)


class WebSiteConfig(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    title = models.CharField(
        max_length=50, verbose_name="名称", null=False, blank=False)
    is_on = models.BooleanField(
        verbose_name='是否开启', default=True, null=False, blank=False)
    save_path = models.CharField(max_length=300, null=True, blank=True,
                                 verbose_name='保存地址')
    save_name = models.SlugField(
        max_length=50, verbose_name="保存名称", default="config", null=False, blank=False)
    data = models.JSONField(verbose_name="配置数据",
                            null=True, default=jsonDefault)
    description = models.CharField(max_length=200, null=True, blank=True,
                                   verbose_name='描述')

    def clean_fields(self, exclude = None):
            super(WebSiteConfig, self).clean_fields(exclude)

            filePathExist = os.path.exists(self.save_path)
            if not filePathExist:
                raise ValidationError(_('【保存地址】不存在...'))
                
    def save(self):
        super(WebSiteConfig, self).save()  # 先保存一下，否则报错

        filePath = self.save_path
        filePathExist = os.path.exists(filePath)
        if not filePathExist:
            return
        saveName = self.save_name+".json"
        fileName = os.path.join(filePath, saveName)
        # jsonData = json.dumps(self.toDict(), ensure_ascii=False)
        save_json(fileName, self.toDict())

        print(fileName, "==============")
        super(WebSiteConfig, self).save()  # 再保存一下

    def toDict(self):
        return {'on': self.is_on, 'config': self.data}

    class Meta:
        verbose_name = "配置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
