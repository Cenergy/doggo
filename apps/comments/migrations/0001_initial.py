# Generated by Django 3.2.1 on 2021-05-16 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='用户名')),
                ('suggest_content', models.TextField(verbose_name='建议内容')),
                ('email', models.EmailField(max_length=50, verbose_name='邮件地址')),
                ('suggest_type', models.IntegerField(choices=[(1, '已答复'), (0, '未答复')], default=0, help_text='回复类型', verbose_name='回复类型')),
                ('reply_content', models.TextField(blank=True, default='', null=True, verbose_name='回复内容')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户建议',
                'verbose_name_plural': '用户建议',
            },
        ),
    ]
