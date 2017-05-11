from .base import *

import os
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = False

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
] + INSTALLED_APPS


DATABASES = {
    'default': dj_database_url.config()
}


EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
