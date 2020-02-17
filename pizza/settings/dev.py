"""
Development Settings
"""
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from pizza.settings.base import *

INSTALLED_APPS += [
    'rest_framework',
    'django_filters',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pizza',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgresdb',
        'PORT': '5432',
    }
}
