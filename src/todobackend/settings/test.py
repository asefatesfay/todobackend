from base import *
import os

INSTALLED_APPS += ('django_nose',)
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')

NOSE_ARGS = [
    '--verbosity=2',
    '--with-spec',
    '--nologcapture',
    '--with-coverage',
    '--spec-color',
    '--cover-package=todo',
    '--cover-xml',
    '--with-xunit'

]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'blah'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'testme'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306')
    }
}