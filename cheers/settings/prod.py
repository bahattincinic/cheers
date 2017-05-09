from .base import *


ALLOWED_HOSTS = ['*']

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
