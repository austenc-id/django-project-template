import os

SECRET_KEY = os.getenv('SECRET_KEY', default='django-devkey')

ROOT_URLCONF = '{{ project_name }}.urls'

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
