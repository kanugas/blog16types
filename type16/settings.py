"""
Django settings for type16 project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMINS = [('Pavlo','pavlokaniuga2.0@gmail.com')]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@X[TIofbv)#68><r$02^mtnNI"Hs[jcYB9jk&(A2j3lW0V+49)!ipYmB=b*RzH1s4pq2o#QTO1Ly3WS:Epjd.%$p`W9Ts+M;\9wnw1oAOFi-6zI(fdx&t"#@~iq89}`'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['16types.happyuser.info',
                 '52.28.198.21',
                 '16types.top',
                 'www.16types.top']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homePage',
    'about',
    'blog',
    'products',
    'method',
    'contacts',
    'imagefit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'type16.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'about', 'templates'),
            os.path.join(BASE_DIR, 'homePage', 'templates'),
            os.path.join(BASE_DIR, 'blog', 'templates'),
            os.path.join(BASE_DIR, 'products', 'templates'),
            os.path.join(BASE_DIR, 'method', 'templates'),
            os.path.join(BASE_DIR, 'contacts', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'dateFormat': 'templatetags.dateFormat',

            }
        },
    },
]

WSGI_APPLICATION = 'type16.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db1.sqlite3'),
#         'CONN_MAX_AGE': 500
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog16types',
        'USER': 'kanugula',
        'PASSWORD': 'Kindle2018',
        'HOST': 'blog-db.cppgkyim0jym.eu-central-1.rds.amazonaws.com',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_ROOT = os.path.join(BASE_DIR, "live-static-files", "static-root")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

# MEDIAFILES_DIRS = (
#   os.path.join(BASE_DIR, 'media'),
# )

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = 'media'
#MEDIA_ROOT = os.path.join(BASE_DIR, "live-static-files", "media-root")
IMAGEFIT_ROOT = ''

MEDIA_URL = '/media/'

#MY_DATE_FORMAT = "d-m-Y \o H:i"
MY_DATE_FORMAT = "Y-m-d \o H:i"

EMAIL_HOST_USER = 'blog16types@gmail.com'

AUTH_USER_EMAIL_UNIQUE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

# EMAIL_PORT_SSL = 465

EMAIL_HOST_PASSWORD = 'hgjk902GHJHGhg9hgd5G54'

EMAIL_USE_TLS = True

# EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'JobMice'

# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
