"""
Django settings for yefenjon project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



LOGIN_REDIRECT_URL = "account:home"
LOGIN_URL = "account:login"
LOGOUT_REDIRECT_URL = "account:login"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h-y$p0at+m7w!t6jxk1qrnn!#75qp2wpkqn)tt9r#(o3yewg$_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
	'account.apps.AccountConfig',
	'donate.apps.donateConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'azbankgateways',
    'peyment',
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

ROOT_URLCONF = 'yefenjon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'yefenjon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR,"static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT =  BASE_DIR / 'media'
AUTH_USER_MODEL = 'account.User'

#=========EMAIL==========
# in cmd/file:
# from django.core.mail import send_mail
# send_mail(sub, mass, se, [recipcie],fail_silently=False)
EMAIL_HOST= "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "amirho33einy1234@gmail.com"
EMAIL_HOST_PASSWORD = "13861386m"
EMAIL_USE_TLS = True
# EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DJANGO_SETTINGS_MODULE='mysite.settings'

#=============payment=====
AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       'IDPAY': {
           'MERCHANT_CODE': '*****************',
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       },
   },
   'IS_SAMPLE_FORM_ENABLE': True, # اختیاری و پیش فرض غیر فعال است
   'DEFAULT': 'IDPAY',
   'CURRENCY': 'IRR', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
  
}
