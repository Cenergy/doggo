from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'
    verbose_name = u"博客"