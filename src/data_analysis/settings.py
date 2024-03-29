"""
Django settings for data_analysis project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import logging.config
import os
# from django.utils.log import DEFAULT_LOGGING
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", 'False').lower() in 'true'

# Allowed Hosts
if ENV_ALLOWED_HOST := os.environ.get("ENV_ALLOWED_HOST", None):
    ALLOWED_HOSTS = [ENV_ALLOWED_HOST]

# Trusted Origins
if ENV_CSRF_TRUSTED_ORIGINS := os.environ.get("ENV_CSRF_TRUSTED_ORIGINS", None):
    CSRF_TRUSTED_ORIGINS = [ENV_CSRF_TRUSTED_ORIGINS]

# # CSRF
# CSRF_COOKIE_SECURE = os.environ.get("ENV_CSRF_COOKIE_SECURE", 'False').lower() in 'true'
# SESSION_COOKIE_SECURE = os.environ.get("ENV_SESSION_COOKIE_SECURE", 'False').lower() in 'true'
#
# # XSS
# SECURE_BROWSER_XSS_FILTER = os.environ.get("ENV_SECURE_BROWSER_XSS_FILTER", 'False').lower() in 'true'
# SECURE_CONTENT_TYPE_NOSNIFF = os.environ.get("ENV_SECURE_CONTENT_TYPE_NOSNIFF", 'False').lower() in 'true'
#
# # SSL Redirect
# SECURE_SSL_REDIRECT = os.environ.get("ENV_SECURE_SSL_REDIRECT", 'False').lower() in 'true'
#
# # HTTP Strict Transport Security
# SECURE_HSTS_SECONDS = os.environ.get("ENV_SECURE_HSTS_SECONDS", None)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get("ENV_SECURE_HSTS_INCLUDE_SUBDOMAINS", 'False').lower() in 'true'
# SECURE_HSTS_PRELOAD = os.environ.get("ENV_SECURE_HSTS_PRELOAD", 'False').lower() in 'true'

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # internal
    'customers',
    'products',
    'profiles',
    'reports',
    'sales',
    # external
    'crispy_forms',
    'storages',
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
]

ROOT_URLCONF = 'data_analysis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'data_analysis.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAIL = all([DB_USERNAME, DB_PASSWORD, DB_DATABASE, DB_HOST, DB_PORT])
DB_IGNORE_SSL = os.environ.get("DB_IGNORE_SSL", 'True').lower() in 'true'

if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
    if not DB_IGNORE_SSL:
        DATABASES["default"]["OPTIONS"] = {"sslmode": "require"}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Authentication
LOGIN_URL = '/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

USE_SPACES = os.environ.get('USE_SPACES', 'False').lower() in 'true'

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = os.environ.get('STATIC_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('STATIC_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = os.environ.get('STORAGE_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'data_analysis.storages.StaticStorage'
    # media settings
    PUBLIC_MEDIA_LOCATION = 'media'
    MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'data_analysis.storages.MediaStorage'
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [BASE_DIR / 'static',
                    BASE_DIR / 'sales' / 'static',
                    BASE_DIR / 'reports' / 'static']
# Logging Configuration
if not DEBUG:
    # Disable Django's logging setup
    LOGGING_CONFIG = None

    # Get loglevel from env
    LOGLEVEL = os.environ.get('DJANGO_LOGLEVEL')

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                # exact format is not important, this is the minimum information
                'format': '%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %(message)s',
            },
        },
        'handlers': {
            # console logs to stderr
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'console',
            },
        },
        'loggers': {
            '': {
                'level': LOGLEVEL,
                'handlers': ['console', ],
            },
        },
    })
