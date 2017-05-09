from .base import *
import dj_database_url


ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware'
] + MIDDLEWARE

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
] + INSTALLED_APPS

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
