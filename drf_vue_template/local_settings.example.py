# from .settings import INSTALLED_APPS, MIDDLEWARE
# Uncomment first line for development server
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Your secret key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # False if your want to use in production

ALLOWED_HOSTS = []  # for development
# ALLOWED_HOSTS = ['*']  # for docker-compose
# ALLOWED_HOSTS = ["your-production-domain"]  # for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# if you want to use debug_toolbar (dev server only)
# INSTALLED_APPS.append('debug_toolbar')
# MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
