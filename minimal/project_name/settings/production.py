from .base import *

DEBUG = False

BASE_URL = 'http://localhost:80'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '{{ project_name }}_postgis',
        'PORT': '5432',
    }
}

# TLS/SSL settings

# https://docs.djangoproject.com/en/1.8/topics/security/#ssl-https
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# For performance reasons, let's set this to False and Nginx will take care of
# it. https://docs.djangoproject.com/en/1.8/ref/middleware/#ssl-redirect
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
