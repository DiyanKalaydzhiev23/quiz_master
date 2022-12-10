import os
from pathlib import Path
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-jeda=+fr+8v8kx!3xq_tl(sz^u35t48lgz-e2=m8_wt@urjlu8'

DEBUG = True

ALLOWED_HOSTS = ["app-quiz-master.herokuapp.com"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'cloudinary',
]

MY_APPS = [
    'quiz_master.accounts',
    'quiz_master.quiz_app',
]

INSTALLED_APPS += MY_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quiz_master.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'quiz_master.wsgi.application'


if "127.0.0.1" in ALLOWED_HOSTS:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'quiz_master_database',
            'USER': 'postgres',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DBNAME'),
            'USER': os.getenv('DBUSER'),
            'PASSWORD': os.getenv('DBPASS'),
            'HOST': os.getenv('DBHOST'),
            'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'quizmasterappteam@gmail.com'
EMAIL_HOST_PASSWORD = 'pwxlnzwtlpgfxozt'
EMAIL_PORT = 587

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.QuizMasterUser'
LOGOUT_REDIRECT_URL = 'login'


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dhqp5qtsw',
    'API_KEY': '593912372856725',
    'API_SECRET': 'iedqyBTS3_zeKMh0t1vR7HjkpZA',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
