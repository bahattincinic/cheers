from .base import *
import dj_database_url
from decouple import config


ALLOWED_HOSTS = ['*']

DEBUG = False

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
] + INSTALLED_APPS


DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
