# Django settings for creative_cubes project.

import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
gettext = lambda s: s

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Christian Schweinhardt', 'cs@creative-cubes.de'),
    ('Manuel Schmidt', 'ms@creative-cubes.de'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cc',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
LANGUAGES = (
    ('de', gettext('Deutsch')),
    ('en', gettext('English')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT,  'media')
MEDIA_URL = '/site_media/'

ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '14w91qwc@5z!7e2$w5r)5pfnn7w@ife^y*f&%)i)59n#r&o9t%'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "cms.context_processors.media",
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
)

ROOT_URLCONF = 'creative_cubes.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'cms',
    'menus',
    'mptt',
    'publisher',
)

CMS_TEMPLATES = (
    ('cms/default.html', gettext('default')),
)

CMS_REDIRECTS = True
CMS_FLAT_URLS = True
CMS_SEO_FIELDS = True
CMS_TEMPLATE_INHERITANCE = True
