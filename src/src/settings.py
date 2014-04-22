"""
Django settings for src project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8gm_lgq-5%0bxb(c*j_rr-sx1(_7l_d64l$%lkopx_j#r8qql4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'housing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'src.urls'

WSGI_APPLICATION = 'src.wsgi.application'

ADMINS = (
    ('nobu42', 'achard@eurecom.fr'),
    ('rem92', 'decouzon@eurecom.fr'),
    ('gd', 'dudragne@eurecom.fr'),
    ('gp5', 'piatte@eurecom.fr'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'housing',
        'USER' : 'wtfo',
        'PASSWORD' : 'company',
        'HOST' : '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates")    
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

APPEND_SLASH = True  # Ajoute un slash en fin d'URL

# File storage related

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

STATIC_DOC_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/login/'

# Images resize and thumbnails

#IMG_WIDTH = 639
#IMG_HEIGHT = 426 previous size
IMG_WIDTH = 678
IMG_HEIGHT = 452
THUMBNAIL_HEIGHT = 47
THUMBNAIL_WIDTH = 70
