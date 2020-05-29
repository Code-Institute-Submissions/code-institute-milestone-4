"""
Django settings for milestone_4 project.

Generated by 'django-admin startproject' using Django 1.11.28.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

if os.path.exists('env.py'):
    import env




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR  = os.path.join(BASE_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '192.168.1.225',
    'localhost',
    'milestone-4-ugogirl.herokuapp.com'
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django_countries',
    'materialize',
    'accounts.apps.AccountsConfig',
    'products',
    'cart',
    'checkout',
    'blog',
    'memberships',
    'orders',
    'search',
    'tags',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'milestone_4.urls'


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
                'django.template.context_processors.media',
                'products.context_processors.menu_links',
                'checkout.context_processors.counter',
                
            ],
        },
    },
]


WSGI_APPLICATION = 'milestone_4.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = { 'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }


# DATABASES = {"default": dj_database_url.parse(os.environ.get("DATABASE_URL"))}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}





# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length':8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


STATIC_URL       = '/static/'
STATICFILES_DIRS = STATIC_DIR,


MEDIA_ROOT = MEDIA_DIR
MEDIA_URL  = '/media/'

STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY')


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

LOGIN_REDIRECT_URL = '/'




AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

AWS_S3_REGION_NAME      = 'eu-west-2'
AWS_STORAGE_BUCKET_NAME = "ugogirl"
AWS_S3_CUSTOM_DOMAIN    = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_ACCESS_KEY_ID       = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY   = os.environ.get("AWS_SECRET_ACCESS_KEY")

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL       = None

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"