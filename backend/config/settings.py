import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key')
DEBUG = os.environ.get('DEBUG', '0') == '1'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', '1') == '1'
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', '1') == '1'
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', '1') == '1'
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', 31536000))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', '1') == '1'
SECURE_HSTS_PRELOAD = os.environ.get('SECURE_HSTS_PRELOAD', '1') == '1'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', 'https://localhost').split(',')

# Multi-tenant
SHARED_APPS = [
    'django_tenants',
    'apps.accounts',
    'apps.tenants',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'corsheaders',
    'apps.audit',
    'health',
]
TENANT_APPS = [
    'apps.citizens',
    'apps.services',
    'apps.applications',
    'apps.documents',
    'apps.notifications',
    'apps.ai_assistant',
]
INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.audit.middleware.AuditMiddleware',
]

TENANT_MODEL = "tenants.Tenant"
TENANT_DOMAIN_MODEL = "tenants.Domain"

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.environ.get('POSTGRES_DB', 'egov'),
        'USER': os.environ.get('POSTGRES_USER', 'egov_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'egov_pass'),
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': int(os.environ.get('POSTGRES_PORT', 5432)),
        'OPTIONS': {
            'sslmode': os.environ.get('POSTGRES_SSLMODE', 'prefer'),
        }
    }
}
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    import urllib.parse as urlparse
    urlparse.uses_netloc.append('postgres')
    parsed_url = urlparse.urlparse(DATABASE_URL)
    DATABASES['default'].update({
        'NAME': parsed_url.path[1:],
        'USER': parsed_url.username,
        'PASSWORD': parsed_url.password,
        'HOST': parsed_url.hostname,
        'PORT': parsed_url.port or 5432,
    })

DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

CORS_ALLOW_ALL_ORIGINS = DEBUG
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# MinIO / S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.environ.get('MINIO_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('MINIO_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('MINIO_BUCKET')
AWS_S3_ENDPOINT_URL = f"http://{os.environ.get('MINIO_ENDPOINT', 'minio:9000')}"
AWS_S3_USE_SSL = False
AWS_S3_VERIFY = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Celery + Redis
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://redis:6379/0')
CELERY_RESULT_BACKEND = os.environ.get('REDIS_URL', 'redis://redis:6379/0')

# Ollama
OLLAMA_HOST = os.environ.get('OLLAMA_HOST', 'http://ollama:11434')
OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'llama3')

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Addis_Ababa'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}