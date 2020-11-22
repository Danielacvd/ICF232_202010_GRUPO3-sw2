"""
Django settings for NoticiasUnab project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(e13ld*rp^jz^vmmv0e9j97%gi6c7if=)a$-bxhebed&p7awf7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'microsoft_auth',
    'Blog',
    'ckeditor',
    'usuarios',
    'tutorial',
]


SITE_ID =1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NoticiasUnab.urls'

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
                'microsoft_auth.context_processors.microsoft',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'microsoft_auth.backends.MicrosoftAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend' 
]

MICROSOFT_AUTH_CLIENT_ID = 'bdd712a8-5515-47bf-b230-ae35e3729bb3'
MICROSOFT_AUTH_CLIENT_SECRET = 'EA_MHSdPHGy0~GQU0_L-2u-KuMx7RnR159'
MICROSOFT_AUTH_LOGIN_TYPE = 'ma'
MICROSOFT_AUTH_TENANT_ID = '6fd48f41-af81-45a5-9c1e-e3990bc27e7c'


WSGI_APPLICATION = 'NoticiasUnab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.sqlite3',
       'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
    # 'default': {
    #   'ENGINE': 'mysql.connector.django',
    #   'NAME': 'grupo03',
    #   'USER': 'grupo03',
    #   'PASSWORD': '198914177',
    #   'DEFAULT-CHARACTER-SET': 'utf8',
    #   'HOST': 'grupo03.c5d4mi2dthpc.us-east-1.rds.amazonaws.com ',
    #   'PORT': '3306',
    #   'TEST': {
    #     'NAME': 'grupo03_test'
    #   }
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'