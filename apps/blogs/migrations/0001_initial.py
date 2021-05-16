# Generated by Django 3.2.1 on 2021-05-16 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.renameImg


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': '文章类型',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, default='', null=True, verbose_name='文章')),
                ('source_img', models.ImageField(blank=True, default='blog/images/default.png', null=True, storage=utils.renameImg.ImageStorage(), upload_to='blog/images/', verbose_name='封面图片')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('blog_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blogs.blogtype')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
