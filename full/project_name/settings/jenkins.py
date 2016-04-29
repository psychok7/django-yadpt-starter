from .base import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dorothy-jenkins',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'django4.dev.ubiwhere.lan',
        'PORT': '',
    }
}

COMPRESSOR_ENABLED = False
