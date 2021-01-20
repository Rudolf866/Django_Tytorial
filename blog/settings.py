"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    with open(os.path.join(BASE_DIR, 'config', 'secret.json')) as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        'secret_key': 'a'
    }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(SECRETS['secret_key'])

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1']

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'account',
    'apps',
    'Blogs',
    'taggit',
    'social_django',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

SENDGRID_API_KEY = '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'

# Переключение режима песочницы (при работе в режиме отладки)
SENDGRID_SANDBOX_MODE_IN_DEBUG = False

# echo to stdout или любой другой файлоподобный объект, который передается бэкенду через поток kwargs.
SENDGRID_ECHO_TO_STDOUT = True

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

# AUTH_USER_MODEL = 'auth.User'


TAMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TAMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',  # Добавил эту строку
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SECRETS.get('db_name', ''),
        'USER': SECRETS.get('db_user', ''),
        'HOST': SECRETS.get('db_host', ''),
        'PASSWORD': SECRETS.get('db_password', ''),
        'PORT': SECRETS.get('db_port', ''),
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.vk.VKOAuth2',  # бекенд авторизации через ВКонтакте
]

SOCIAL_AUTH_FACEBOOK_KEY = '245591560418327'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8c35988469def96982ff6504e2c858b8'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '781610009664-ff1jovcql0agbbh2c8vp8gph0m79frsi.apps.googleusercontent.com'  # Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'BOTm_RCDWra17RAhL5jyJc5D'  # Google Consumer Secret
SOCIAL_AUTH_VK_OAUTH2_KEY = '7734471'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'ZtRDj8rmYJLwvGcys8yY'
LOGIN_REDIRECT_URL = '/account/'
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
