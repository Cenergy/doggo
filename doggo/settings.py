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

ALLOWED_HOSTS = ['127.0.0.1', '.aigisss.com','localhost']
# 跨域
CORS_ORIGIN_ALLOW_ALL = True

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
# SOCIAL_AUTH_SANITIZE_REDIRECTS = True
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SOCIAL_AUTH_TRAILING_SLASH = False

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
]

MIDDLEWARE = [
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
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


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
