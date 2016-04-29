from .base import *

# DEBUG = False
# ALLOWED_HOSTS = ['.web.prioenergy.com', '.webapp.prio.pt', 'prio']
# BASE_URL = 'http://web.prioenergy.com'
#
# # Database
# # https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'prio_db',
#         'USER': 'postgres',
#         'PASSWORD': os.environ.get('PRIO_DB_PASS', 'admin'),
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
#
# COMPRESS_ENABLED = True
#
# RAVEN_CONFIG = {
#     'dsn': 'http://372aff5def824f109c78d3ba019898a9:0b7b5e96220a435eb19489525f1f6cb1@sentry.ubiwhere.com/56',
# }
#
# # Add raven to the list of installed apps
# INSTALLED_APPS = INSTALLED_APPS + (
#     'raven.contrib.django.raven_compat',
# )

BASE_URL = 'http://localhost:80'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'dorothy_postgis',
        'PORT': '5432',
    }
}
