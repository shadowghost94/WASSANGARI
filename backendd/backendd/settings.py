from pathlib import Path
import os
import dj_database_url
from datetime import timedelta
from .info import *

#Configurations pour envoie d'e-mail
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT

#LOGIN_URL
LOGIN_URL = '/connexion'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-5tkne!-vjoi7h0!#p-3m$kkmojev63p=$!3%r*o2tix=mcbnqw"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['wassangari.onrender.com', 'localhost', '127.0.0.1', 'plateforme.waxangarilabs.org']


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
]

ROOT_URLCONF = "backendd.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backendd.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "wassangari",
        "USER": "postgres",
        "PASSWORD": "kissira",
        "HOST": "localhost",
        
    }
}
DATABASES["default"]= dj_database_url.parse("postgresql://wassangari_user:6bLNrkY5wWZjWI1jn1mrPNkXubSq9zIx@dpg-cqqpenl6l47c73b19q0g-a.oregon-postgres.render.com/wassangari")

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = 'api.Utilisateur'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


CORS_ALLOW_ALL_ORIGINS = True

#ThereIsAWay
SESSION_COOKIE_NAME = 'sessionid'  # Nom du cookie de session
SESSION_COOKIE_AGE = 1209600  # Durée de vie du cookie de session en secondes (2 semaines par défaut)
SESSION_SAVE_EVERY_REQUEST = False  # Si True, la session sera sauvegardée à chaque requête
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Si True, la session expire lorsque le navigateur est fermé

CSRF_COOKIE_NAME = 'csrftoken'
CSRF_COOKIE_AGE = 31449600  # Durée de vie du cookie en secondes (par défaut 1 an)
CSRF_COOKIE_DOMAIN = None
CSRF_COOKIE_SECURE = False  # Si True, le cookie CSRF sera transmis uniquement sur des connexions HTTPS
CSRF_COOKIE_HTTPONLY = False  # Si True, le cookie CSRF sera inaccessible par JavaScript
