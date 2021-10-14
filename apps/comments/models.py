from django.db import models

# Create your models here.
import datetime


from utils.replay_email import common_reply_email


class Suggestion(models.Model):
    SUGGEST_TYPE = (
        (1, "已答复"),
        (0, "未答复"),
    )
    id = models.BigAutoField(primary_key=True)
    suggest_name = models.CharField(max_length=100, verbose_name="用户名", null=True, blank=True)
    suggest_content = models.TextField(verbose_name="建议内容", null=False, blank=False)
    email = models.EmailField(max_length=50, verbose_name="邮件地址", null=False, blank=False)
    suggest_type = models.IntegerField(choices=SUGGEST_TYPE, verbose_name="回复类型", help_text="回复类型", default=0)
    reply_content = models.TextField(verbose_name='回复内容', default="", null=True, blank=True)
    add_time = models.DateField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户建议"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if self.suggest_type == 0:
            pass
        else:
            common_reply_email(self.email, self.suggest_content, self.reply_content)
        # return super(Suggestion, self).delete(*args, **kwargs)
        return super(Suggestion, self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class FriendLinks(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="名称", null=False, blank=False)
    intro = models.CharField(max_length=200, verbose_name="简介", null=True, blank=True)
    link = models.URLField(verbose_name="链接", null=False, blank=False)
    avatar = models.URLField(verbose_name="头像",null=True, blank=True)
    email = models.EmailField(verbose_name="邮件地址", null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True,verbose_name='描述')
    add_time = models.DateField(default=datetime.datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "友情链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title