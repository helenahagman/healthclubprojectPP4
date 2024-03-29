"""
Django settings for healthclub project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path
import cloudinary
from env import *

if os.path.isfile("env.py"):
    import env

    

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*.ws-eu106.gitpod.io',
    '8000-helenahagma-healthclubp-xd16582m4yh.ws-eu107.gitpod.io',
    '8000-helenahagma-healthclubp-xd16582m4yh.ws-eu108.gitpod.io',
    'health-club-project-pp4.herokuapp.com',
    'health-club-project-pp4-aec30baa0c93.herokuapp.com',
    'localhost'
]


X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    'ptproject',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'healthclub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'healthclub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    
# DATABASES = {
#    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
# }

# Ensure DATABASE_URL is decoded if it's bytes
database_url = os.environ.get("DATABASE_URL")
print("DATABASE_URL Type:", type(database_url))
if isinstance(database_url, bytes):
   database_url = database_url.decode('utf-8')

# Configure the database settings
DATABASES = {'default': dj_database_url.parse(database_url)}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
 
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


CSRF_TRUSTED_ORIGINS = [
    'https://*.gitpod.io',
    'https://health-club-project-pp4.herokuapp.com',
    'https://health-club-project-pp4-aec30baa0c93.herokuapp.com',
    'http://localhost',
    'https://8000-helenahagma-healthclubp-xd16582m4yh.ws-eu107.gitpod.io',
    'https://8000-helenahagma-healthclubp-xd16582m4yh.ws-eu108.gitpod.io',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

cloudinary.config(
        cloud_name=os.environ['CLOUD_NAME'],
        api_key=os.environ['API_KEY'],
        api_secret=os.environ['API_SECRET']
)

CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ['CLOUD_NAME'],
        'API_KEY': os.environ['API_KEY'],
        'API_SECRET': os.environ['API_SECRET'],
}

# Default file storage for media files
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

LOGIN_REDIRECT_URL = 'profile_view'
ACCOUNT_LOGOUT_REDIRECT_URL = 'home_view'
ACCOUNT_SESSION_REMEMBER = TrueACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
