"""
Django settings for Hostallica project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



#cloudinary settings
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2xf^-gt=+aa!v@(b^f9)=pyoi9hc@=w!tcw9fa((lircj_d%19'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['hostallica-71b670ea65e3.herokuapp.com' ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend',
    #'chat',


    #third party apps
    'cloudinary',
    'cloudinary_storage',
]



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hjjborpoh',
    'API_KEY': '249263126821139',
    'API_SECRET': 'wNBz4HfRe8CQudub8P63DOyRWlY'
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hostallica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Hostallica.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/











STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"staticfiles", "static_root")
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# settings.py
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


#static with cloudinary
#STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'


MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "staticfiles", "media_root")
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'backend.Student'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'

#stripe settings
STRIPE_PUBLISHABLE_KEY = 'pk_test_51NW6YmKDJaSwPv3RtYY0LrOdWMhWB2scJeS9MJ2blIiO2q7LlTcaVoypcxYIdDsP5AtIzRd4Xgc92Y5JvhCfBDIo009MZe9Bab'
STRIPE_SECRET_KEY = 'sk_test_51NW6YmKDJaSwPv3RaQI8iq16Jb8LWlqxzRChCazsw8puOg8NolgXdpIvzOc20kM7pP5hSQwP2pY8mFWPdL0RCgcC00DcGYU1o5'





handler404 = 'backend.views.handler404'
handler500 = 'backend.views.handler500'