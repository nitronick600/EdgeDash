"""
Django settings for edgemark_dashboard project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Enable Persistent Connections
DATABASES = {
    'default':
        dj_database_url.config()
    }

# SECURITY WARNING: don't run with debug turned on in production!
INPROD = True
DEBUG = not INPROD
SECURE_CONTENT_TYPE_NOSNIFF = INPROD
SECURE_BROWSER_XSS_FILTER = INPROD
SECURE_SSL_REDIRECT = INPROD
SESSION_COOKIE_SECURE = INPROD
CSRF_COOKIE_SECURE = INPROD
CSRF_COOKIE_HTTPONLY = INPROD
X_FRAME_OPTIONS = "DENY"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = [
    'www.edgedash.com',
    'www.edgedash.herokuapp.com'
    '.edgedash.com',
    '.edgedash.com',
    '.edgedash.com.',
    'localhost',
    '127.0.0.1'
]

SECRET_KEY = os.environ['SECRET_KEY']
ADMINS = ((os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']))

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangosecure',
    'edgemark_dashboard',
    'dashing',
)

MIDDLEWARE_CLASSES = (
    'djangosecure.middleware.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'edgemark_dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'edgemark_dashboard/templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.request",
            ],
        },
    },
]

DASHING = {
        'PERMISSION_CLASSES':   ('dashing.permissions.IsAuthenticated',)
}

WSGI_APPLICATION = 'edgemark_dashboard.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/dashboard/'

LOGIN_URL = '/login'

LOGOUT_URL = '/logout'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = os.path.join(BASE_DIR,'/staticfiles/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'edgemark_dashboard/static'),
)
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
