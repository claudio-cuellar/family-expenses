from .base import *
import dj_database_url

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL'),
        engine=env('DATABASE_ENGINE'),
        ssl_require=True,
    )
}

# Cloudflare settings
DEBUG = False

ALLOWED_HOSTS = ['claudio-cuellar.com', 'www.claudio-cuellar.com']

CORS_ALLOWED_ORIGINS = [
    "https://claudio-cuellar.com",
    "https://www.claudio-cuellar.com",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
FORCE_SCRIPT_NAME = "/api"
USE_X_FORWARDED_HOST = True