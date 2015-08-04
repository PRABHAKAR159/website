import os
from os.path import join, dirname, abspath

DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = False

BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

ADMINS = (
    ('Mathieu Comandon', 'strycore@gmail.com'),
    ('Pascal', 'dev@xod.me'),
)
INTERNAL_IPS = ('127.0.0.1',)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'lutris.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Paris'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    join(BASE_DIR, "public"),
)
FILES_ROOT = join('MEDIA_ROOT', 'files')
FILES_URL = 'http://localhost:8000/media/files/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
TOSEC_DAT_PACK = join(MEDIA_ROOT, "tosec",
                      "TOSEC - DAT Pack - Complete (2292) (TOSEC-v2014-10-31)")
FILES_ROOT = join(MEDIA_ROOT, 'files')

SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'lutrisweb.urls'
WSGI_APPLICATION = 'lutrisweb.wsgi.application'

TEMPLATE_DIRS = (
    join(BASE_DIR, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'sorl.thumbnail',
    'tastypie',
    'rest_framework',
    'rest_framework.authtoken',
    'django_jcrop',
    'crispy_forms',
    'django_select2',
    'markupfield',
    'django_openid_auth',
    'django_extensions',

    'common',
    'platforms',
    'games',
    'bundles',
    'runners',
    'accounts',
    'tosec',
)

BANNER_SIZE = "184x69"
ICON_SIZE = "32x32"
ICON_LARGE_SIZE = "256x256"
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_COLORSPACE = "sRGB"

AUTH_USER_MODEL = 'accounts.User'
AUTH_PROFILE_MODULE = "accounts.Profile"
ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/user/login/"
AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)
OPENID_SSO_SERVER_URL = 'http://steamcommunity.com/openid'

# Modify temporarily the session serializer because the json serializer in
# Django 1.6 can't serialize openid.yadis.manager.YadisServiceManager objects
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

RELEASES_URL = "http://lutris.net/releases/"
CLIENT_VERSION = "0.3.6.3"


# Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

# Admin
GRAPPELLI_ADMIN_TITLE = "Lutris Administration"

# Email
DEFAULT_FROM_EMAIL = "admin@lutris.net"
SERVER_EMAIL = "admin@lutris.net"
EMAIL_SUBJECT_PREFIX = "[Lutris] "

# Celery
CELERY_SEND_TASK_ERROR_EMAILS = True
BROKER_URL = 'amqp://guest:guest@localhost//'
# API Keys
STEAM_API_KEY = "********************************"

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# Logging
SEND_BROKEN_LINK_EMAILS = False
LOGGING_HANDLERS = ['file', 'mail_admins', 'console']
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'include_html': True,
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'lutrisweb.log'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': LOGGING_HANDLERS,
            'propagate': True,
            'level': 'INFO',
        },
        'factory': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': LOGGING_HANDLERS,
            'level': 'WARNING',
            'propagate': True,
        },
        'lutrisweb': {
            'handlers': LOGGING_HANDLERS,
            'level': 'DEBUG',
            'propagate': True,
        },
        'accounts': {
            'handlers': LOGGING_HANDLERS,
            'level': 'DEBUG',
            'propagate': True,
        },
        'common': {
            'handlers': LOGGING_HANDLERS,
            'level': 'DEBUG',
            'propagate': True,
        },
        'games': {
            'handlers': LOGGING_HANDLERS,
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
