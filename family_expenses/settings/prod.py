from .base import *

DEBUG = False

ALLOWED_HOSTS = ['claudio-cuellar.com', 'www.claudio-cuellar.com']

# Security settings for production
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
FORCE_SCRIPT_NAME = "/api"
USE_X_FORWARDED_HOST = True