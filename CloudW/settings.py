"""
Django settings for CloudW project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import os.path
APP_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l(a&^$2bxb)4ohc*)n69&*!!&$=^v*=o+-2o4k@_@8jmv2rp@h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['clw.com.ua']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
   # 'registration.supplements.default',
    'supplement_registration',
    'privatebroadcast',
    'multiuploader',
    'south',
    'gunicorn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'supplement_registration.context_processors.include_login_form',
    'supplement_registration.context_processors.user',
    'multiuploader.context_processors.booleans',
)

ROOT_URLCONF = 'CloudW.urls'

WSGI_APPLICATION = 'CloudW.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(APP_ROOT, '../htdocs/')

STATIC_URL = '/htdocs/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR,  'templates'),
#)
STATICFILES_DIRS = (
    APP_ROOT + '/htdocs/static',
)
TEMPLATE_DIRS = (
    APP_ROOT + '/templates'
)

MULTIUPLOADER_FILES_FOLDER = 'htdocs/'

MULTIUPLOADER_FILE_EXPIRATION_TIME = 3600

REGISTRATION_SUPPLEMENT_CLASS = 'supplement_registration.models.MyRegistrationSupplement'

ACCOUNT_ACTIVATION_DAYS = 7

#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'witnessescloud@gmail.com'
##EMAIL_PORT = 587
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Email sender settings.
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'witnessescloud@gmail.com'
SERVER_EMAIL = 'witnessescloud@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'witnessescloud@gmail.com'
EMAIL_HOST_PASSWORD = 'witnessescloud1246'

LOGIN_REDIRECT_URL = '/'

MULTIUPLOADER_FORMS_SETTINGS = {
    'default': {
        'FILE_TYPES': ["txt", "zip", "jpg", "jpeg", "flv", "png"],
        'CONTENT_TYPES': [
                'image/jpeg',
                'image/png',
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                'application/vnd.ms-powerpoint',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                'application/vnd.oasis.opendocument.text',
                'application/vnd.oasis.opendocument.spreadsheet',
                'application/vnd.oasis.opendocument.presentation',
                'text/plain',
                'text/rtf',
                ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER': 5,
        'AUTO_UPLOAD': True,
    },

    'video': {
        'FILE_TYPES': ['flv', 'mpg', 'mpeg', 'mp4' ,'avi', 'mkv', 'ogg', 'wmv', 'mov', 'webm' ],
        'CONTENT_TYPES' : [
            'video/mpeg',
            'video/mp4',
            'video/ogg',
            'video/quicktime',
            'video/webm',
            'video/x-ms-wmv',
            'video/x-flv',
            ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER':5,
        'AUTO_UPLOAD': True,
    },
    }

try:
    from production_settings import *
except ImportError as e:
    pass