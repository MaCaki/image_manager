"""
Django settings for image_manager project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_g96%rg6)an9jq=975o@ppad@y49&mq74^!^&uf+0uyh%f_x8p'

DEBUG = False

# Flags for determning which environment.
# this is messy, may clean up later.
DEV_ENV = os.environ['IM_ENV'] == 'dev'
STAGE_ENV = os.environ['IM_ENV'] == 'stage'
PROD_ENV = os.environ['IM_ENV'] == 'prod'

AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_IMAGE_BUCKET')

DEFAULT_FROM_EMAIL = 'robot@ucsfproctorgrading.center'

# this log file is only used in stage or prod right now.  In future, when
# the dev environment is containerized it can be used there as well.
LOG_FILE = '/var/log/image_manager_logs/image_manager.log'


# SECURITY WARNING: don't run with debug turned on in production!
if DEV_ENV:
    DEBUG = True
    DEV_ENV = True

    ALLOWED_HOSTS = ['0.0.0.0']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('IM_POSTGRES_NAME'),
            'USER': os.environ.get('IM_POSTGRES_USER'),
            'PASSWORD': os.environ.get('IM_POSTGRES_PASSWORD'),
            'HOST': os.environ.get('IM_POSTGRES_HOST'),
            'PORT': 5432,
        }
    }
    # store image files locally in the same directory.
    MEDIA_ROOT = os.path.join(BASE_DIR, '.media')
    MEDIA_URL = "/media/"


# Setup logging for prod.
if os.environ['IM_ENV'] in ('prod', 'stage'):
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_SES_REGION_NAME = 'us-west-2'
    AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
    # Use s3 in stage and production.
    DEFAULT_FILE_STORAGE = 'core.backends.s3.PrivateMediaStorage'

    LOG_FILE = '/var/log/image_manager_logs/image_manager.log'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': LOG_FILE,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

    ALLOWED_HOSTS = ['localhost', '.elasticbeanstalk.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }


# Application definition


INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'grade.apps.GradeConfig',
    'storages',
    'rest_framework',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'image_manager.urls'

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

WSGI_APPLICATION = 'image_manager.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHELL_PLUS = "ipython"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")
STATIC_URL = '/static/'

# NOTE: boto3 will be able acces s3 from the Elastic Beanstalk EC2 instances
# based on their attached IAM policy.  No environment credentials are needed.

AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# This is the prefix of the file path
AWS_PRIVATE_MEDIA_LOCATION = 'images/private'
