"""
Django settings for RemoteOPD project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z_w@b_+en%7+3np++w4h4gjikd7^gh-vsbv=u&vv&tu*87vwoe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'rest_framework',
          'drf_yasg',
          'corsheaders',
          'Patient',
          'User',
          'disease',
          'villages',
          'camps',
          'medicines',
          'hbcamp',
          'eyecamp',
          'Client',
          'adcamp',
          'megacamp',

]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
          'corsheaders.middleware.CorsMiddleware',
          'django.middleware.security.SecurityMiddleware',
          'django.contrib.sessions.middleware.SessionMiddleware',
          'django.middleware.common.CommonMiddleware',
          'django.middleware.csrf.CsrfViewMiddleware',
          'django.contrib.auth.middleware.AuthenticationMiddleware',
          'django.contrib.messages.middleware.MessageMiddleware',
          'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RemoteOPD.urls'

TEMPLATES = [
          {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [],
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

WSGI_APPLICATION = 'RemoteOPD.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
          'default': {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'remoteopd',
                    'USER': 'root',
                    'PASSWORD': 'Roshni',
                    'HOST': 'localhost',
                    'PORT': '3306',
          }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
