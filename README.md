# CRUD App: Vue.js & Django (DRF)
Template project for CRUD App using Vue.js and DRF

Create `drf_vue_template\local_settings.py` with following content (see `drf_vue_template\local_settings.example.py`):
```python
# from .settings import INSTALLED_APPS, MIDDLEWARE
# Uncomment first line for development server
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'Your secret key'

DEBUG = True  # False if your want to use in production

ALLOWED_HOSTS = []  # for development
ALLOWED_HOSTS = ['*']  # for docker-compose
ALLOWED_HOSTS = ["your-production-domain"]  # for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# if you want to use debug_toolbar (dev server only)
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

```

Fill your database and run Django development server:
```
$ pip3 install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

To run with a docker compose:
```
$ docker-compose up
```

## Screens
##### Example #1: Main page
![Main page](assets/screen_1.png)
##### Example #2: Pagination
![Main page](assets/screen_2.png)
##### Example #3: Create article
![Main page](assets/screen_3.png)
##### Example #4: Search article by title
![Failed services](assets/screen_4.png)
