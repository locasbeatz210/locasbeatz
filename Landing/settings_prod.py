DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_locasbeatz'
        'PASSWORD': '19960330'
        'HOST': 'localhost'
        'PORT': '',
    }