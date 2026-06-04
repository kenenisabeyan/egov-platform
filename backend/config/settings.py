import os
from pathlib import Path
from django_tenants.utils import tenant_context

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ.get('DEBUG', '0') == '1'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# Multi‑tenant
SHARED_APPS = [
    'django_tenants',
    'accounts',  # our custom user & tenant models
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'rest_framework',
]
TENANT_APPS = [
    'citizens',
    'services',
    'applications',
    'documents',
    'ai_assistant',
    'notifications',
]
INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'db',
        'PORT': 5432,
    }
}
DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

# REST + JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}