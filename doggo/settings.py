"""
Django settings for doggo project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import sys
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oa0m%=m-$gcpc9ripnwg=9+qy*^t0av1kc2_dx+f)1na_e*g^1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 跨域
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作
CORS_ORIGIN_ALLOW_ALL = True  # 设置支持所有域名访问,如果为False,需要指定域名
# CORS_ORIGIN_WHITELIST = ('*') #  白名单，"*"支持所有域名进行访问，也可写成("域名1","域名")
ALLOWED_HOSTS = ['127.0.0.1', '.aigisss.com',
                 'localhost', '47.114.59.109']     # 允许所有ip或域名

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://\w+\.aigisss\.com$",
]

# SESSION_COOKIE_DOMAIN = "aigisss.com"  #这个设置之后开发admin就登陆不上
AIGISSS_HOST='https://api.aigisss.com'

AUTH_USER_MODEL = 'users.UserProfile'

# --------------------自定义认证后端-------------------------------------
AUTHENTICATION_BACKENDS = [
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'users.views.CustomBackend',
]

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'  # 新增
SOCIAL_AUTH_GITHUB_KEY = 'cbd780d104e230cca877'
SOCIAL_AUTH_GITHUB_SECRET = '0d101317cde90ca8cb66b6aa56532af62d1ddc49'
SOCIAL_AUTH_GITHUB_USE_OPENID_AS_USERNAME = True

SOCIAL_AUTH_QQ_KEY = '101946707'
SOCIAL_AUTH_QQ_SECRET = '8b6fb506209ffd3360093484be3f7744'
SOCIAL_AUTH_QQ_USE_OPENID_AS_USERNAME = True

SOCIAL_AUTH_WEIBO_KEY = '2006316624'
SOCIAL_AUTH_WEIBO_SECRET = '0723efacc88399f1332893d2b91211a6'
SOCIAL_AUTH_WEIBO_USE_OPENID_AS_USERNAME = True


# 登陆成功后的回调路由
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000'  # 登陆成功之后的路由
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'https://aigisss.com/view/'  # 登陆成功之后的路由
SOCIAL_AUTH_SANITIZE_REDIRECTS = False
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TRAILING_SLASH = False


SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    # Verifies that the social association can be disconnected from the current
    # user (ensure that the user login mechanism is not compromised by this
    # disconnection).
    # 'social.pipeline.disconnect.allowed_to_disconnect',

    # Collects the social associations to disconnect.
    'social.pipeline.disconnect.get_entries',

    # Revoke any access_token when possible.
    'social.pipeline.disconnect.revoke_tokens',

    # Removes the social associations.
    'social.pipeline.disconnect.disconnect',
)

# Application definition

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 以上是默认的apps
    'users',
    'blogs',
    'comments',
    'explores',
    'resources',
    'wechat',
    # 以下是第三方apps
    'django_filters',
    'social_django',
    'captcha',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'import_export',
    'django_q',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'doggo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # 新增
                'social_django.context_processors.login_redirect',  # 新增
            ],
        },
    },
]

WSGI_APPLICATION = 'doggo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# 连接MySQL数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'geo_users',
#         'USER': 'root',
#         'PASSWORD':'Cenergy',
#         'HOST':'localhost',
#         'PORT':'3306',
#     }
# }
# 连接postgreSQL数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aigisss',
        'USER': 'postgres',
        'PASSWORD': 'postgres.neng',
        'HOST': '127.0.0.1',
        'PORT': '9555',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 下面是自定义的一些


# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    # "DEFAULT_VERSIONING_CLASS": 'rest_framework.versioning.URLPathVersioning',
    # "ALLOWED_VERSIONS": ['v1', "v2"],
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1000/day',
        'user': '10000/day'
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': datetime.timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': datetime.timedelta(days=1),
}

# 缓存设置

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

Q_CLUSTER = {
    'name': 'aigisss_doggo',  # 项目名称
    'workers': 4,  # worker数。默认为当前主机的CPU计数，
    'recycle': 500,  # worker在回收之前要处理的任务数。有助于定期释放内存资源。默认为500。
    'timeout': 60,   # 任务超时设置,如果是爬虫任务建议设置长一些
    'compress': True,  # 数据压缩
    'save_limit': 250,  # 限制保存到Django的成功任务的数量。0为无限，-1则不会保存
    'queue_limit': 500,  # 排队的任务数量，默认为workers**2。
    'cpu_affinity': 1,  # 设置每个工作人员可以使用的处理器数量。根据经验; cpu_affinity 1支持重复的短期运行任务，而没有亲和力则有利于长时间运行的任务。
    'label': '任务',  # 用于Django Admin页面的标签。默认为'Django Q'，之后我会根据源码做一个中文版的django-admin页面。如果有需求请私信我
    'redis': {  # 如果配置了redis缓存，可以使用django的设置，请参考官方文档。
        'host': '127.0.0.1',
        'port': 6379,
        'db': 0, }
}


# 配置session存储

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# 邮箱设置
EMAIL_HOST = "smtp.sina.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "helloaigis@sina.com"
EMAIL_HOST_PASSWORD = "Cenergy.0919"
EMAIL_USE_TLS = False
EMAIL_FROM = "helloaigis@sina.com"

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# ----------------------手机号码正则表达式-------------------------------
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
# 云片网apikey 配置
API_KEY = "09d6805265afbd0a779cfd9e16a0f4c5"

# 百度识别# 定义常量
BAIDU_APP_ID = '11800206'
BAIDU_API_KEY = 'sAy8l7GrgGMBfesVoPkYtr0m'
BAIDU_SECRET_KEY = 'Ex4Yitab1ZTq8y3FykTpa3kbGvpfUvjV'

# 百度地图
BAIDU_MAP_KEY = 'tDM947ZCUIZXzs7ohNHsz77QkU22WzDa'

# 图灵api
TURING_API_KEY = 'bf61c090a1bc4cfabc43e20e2d5b307b'
