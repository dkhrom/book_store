from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-3-!fc-7rfp#fvz6q(h7-5-d$1+qq6+kpjl%5ap!&p)t6g9h@4b'

DEBUG = True

if DEBUG == True:
    ALLOWED_HOSTS = []

if DEBUG == False:
    ALLOWED_HOSTS = ['']
    PREPEND_WWW = True
    DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django_cleanup',
    'crispy_forms',
    'crispy_bootstrap5',
    'app',
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


# Security
if DEBUG == False:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    SECURE_PROXY_SSL_HEADER = ("header-name", "header-value")


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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


WSGI_APPLICATION = 'core.wsgi.application'


if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


if DEBUG == False:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dps010',
            'USER': 'dps010',
            'PASSWORD': '3Fd8K#43Gt*d7Uq',
            'HOST': 'localhost',
            'PORT': '',
        }
    }


# Password validation
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


CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True


if DEBUG == True:
    STATIC_URL = '/storage/static/'
    MEDIA_URL = '/storage/media/'

    MEDIA_ROOT = (BASE_DIR / 'storage/media/')
    STATICFILES_DIRS = [BASE_DIR / 'storage/static/']
    

if DEBUG == False:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / 'storage/static'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'storage/media'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'