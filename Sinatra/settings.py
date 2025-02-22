from .Enums.DatabaseEnvironments import DatabaseEnvironments
from decouple import config
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DEPLOYMENT_ENVIRONMENT = DatabaseEnvironments[config('DATABASE_DEPLOYMENT_ENVIRONMENT')]



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    "djoser",
    "rest_framework_simplejwt.token_blacklist",
    "corsheaders",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
    'xhr',
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
]

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'localhost'
)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'User.custom_django_model_permissions.RoleBasedPermissions',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=45),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "password/reset-password-confirmation/?uid={uid}&token={token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {},
    "EMAIL": {
        "password_reset": "Emailing.views.PasswordResetEmail"
    },
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = config('EMAIL_HOST_USER')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'Sinatra.urls'

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

WSGI_APPLICATION = 'Sinatra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

if DATABASE_DEPLOYMENT_ENVIRONMENT == DatabaseEnvironments.PRODUCTION:
    DATABASES = {
    'default': {
        'ENGINE': config("ENGINE"),
        'NAME': config("VPS_POSTGRES_DEVELOPMENT_DATABASE"),
        'USER': config("VPS_POSTGRES_USER"),
        'PASSWORD': config("VPS_POSTGRES_PASSWORD"),
        'HOST': config("VPS_POSTGRES_HOST"),
        'PORT': '5432',
    }
}
elif DATABASE_DEPLOYMENT_ENVIRONMENT == DatabaseEnvironments.DEVELOPMENT:
    DATABASES = {
        'default': {
            'ENGINE': config("ENGINE"),
            'NAME': config("VPS_POSTGRES_DEVELOPMENT_DATABASE"),
            'USER': config("VPS_POSTGRES_USER"),
            'PASSWORD': config("VPS_POSTGRES_PASSWORD"),
            'HOST': config("VPS_POSTGRES_HOST"),
            'PORT': '5432',
        }
    }
else:
    raise Exception(f"DATABASE env var does not exist. Value = '{DATABASE_DEPLOYMENT_ENVIRONMENT}'")


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
