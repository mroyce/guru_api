import os
import sys
import datetime

from distutils.util import strtobool


def string_to_bool(bool_as_string):
    """Return a Python bool for a given string"""
    return bool(strtobool(bool_as_string))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY_CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(0)=+)'
SECRET_KEY = os.environ.get('SECRET_KEY', 'm58)p4s-j)&q0h%wfl(g36lsb_901od=_vc7d^8k*7m7s_ce&3')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = string_to_bool(os.environ.get('DEBUG', 'TRUE'))


# Host/Domain names that this Django site can serve
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', ['localhost'])


# Authentication Model
AUTH_USER_MODEL = 'core.Account'


# Designate all applications that are enabled in this Django project
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'rest_framework_swagger',

    'guru_api',
    'guru_api.core',
    'guru_api.apps.messaging',
    # 'guru_api.apps.payment',
    # 'guru_api.apps.review',
    # 'guru_api.apps.schedule',
)


# Middleware hooks into Django's request/response processing
MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)


# String representing full Python import path to root URLConf
ROOT_URLCONF = 'guru_api.urls'


# Python dotted path to the WSGI application used by Django's runserver
WSGI_APPLICATION = 'guru_api.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.environ.get('GURU_POSTGRES_DATABASE', ''),
        # 'USER': os.environ.get('GURU_POSTGRES_USER', ''),
        # 'PASSWORD': os.environ.get('GURU_POSTGRES_PASSWORD', ''),
        # 'HOST': os.environ.get('GURU_POSTGRES_HOST', 'localhost'),
        # 'PORT': os.environ.get('GURU_POSTGRES_PORT', '5432'),
    }
}


# Internationalization

# A string representing the language code for this installation
LANGUAGE_CODE = 'en-us'

# A string representing the time zone for this installation
TIME_ZONE = 'UTC'

# If you set this to False, Django will make some optimizations so as not
# to load the internalization machinery
USE_I18N = True

# If you set this to False, Django will not format dates, numbers, and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes
USE_TZ = True


# Static files (CSS, JavaScript, Images)

# Absolute filesystem path to the directory that will hold static files
STATIC_ROOT = os.environ.get('STATIC_ROOT', '{}/guru_api/static/'.format(BASE_DIR))

# URL that handles the static files served from STATIC_ROOT
STATIC_URL = os.environ.get('STATIC_URL', '/static/')


# Media Files (Pictures, Videos)

# Absolute filesystem path to the directory that will hold user-uploaded files
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '{}/guru_api/media/'.format(BASE_DIR))

# URL that handles the media served from MEDIA_ROOT
MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

# Upload root for uploading media files
UPLOAD_ROOT = os.environ.get('UPLOAD_ROOT', 'upload/')

# Default file storage class for file-related operations that don't specifiy a specific storage system
DEFAULT_FILE_STORAGE = os.environ.get('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')

# REST Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'guru_api.core.auth.jwt.JWTAuthentication',
    ),

    'DEFAULT_PERMISSION_CLASSES': (
        'guru_api.core.permissions.AllRequestsDenied',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
    ),

    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',

    'PAGE_SIZE': 50,
}


# Django Rest Framework JWT Library
# https://github.com/GetBlimp/django-rest-framework-jwt

# JWTs are signed with a combination of JWT_MASTER_SECRET_KEY and user.jwt_secret_key
# All tokens will be invalid if this string is changed!
JWT_MASTER_SECRET_KEY = os.environ.get('JWT_MASTER_SECRET_KEY', 'z&B3(s#76qd^-4,C*5vuDk8j8A{:;pCPXDt"7k.@m@"=^Z,Pa*')

# Algorithm used to create the JWT payload
JWT_ALGORITHM = 'HS256'

# The 'JWT' in the header `Authorization: JWT eyJhbGciOiAiSFMyNTYiLCAidHlwIj`
JWT_AUTH_HEADER_PREFIX = 'JWT'

# If you set this to False, JWTs will have no expiration time verification
JWT_VERIFY_EXPIRATION = True

# JWT expiration is one year
JWT_EXPIRATION_DELTA = datetime.timedelta(weeks=52)

# JWT_LEEWAY allows you to validate an expiration time which is in the past but not very far.
# For example, if you have a JWT payload with an expiration time set to 30 seconds after
# creation but you know that sometimes you will process it after 30 seconds, you can
# set a leeway of 10 seconds in order to have some margin.
# Default is 0 seconds.
JWT_LEEWAY = 0


# Stripe Secret Key
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_W7z8Qqxa89ZyZSrKDUryoKPi')


# If we're in debug mode, enable the browsable API
if 'test' not in sys.argv and DEBUG:
    REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] += ('rest_framework.authentication.SessionAuthentication',)
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ('rest_framework.renderers.BrowsableAPIRenderer',)
