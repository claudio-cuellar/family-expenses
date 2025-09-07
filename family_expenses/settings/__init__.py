import os
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, "../.env"))

DJANGO_ENV = env("DJANGO_ENV", default="dev")

print(f"🔧 Loading Django settings for: {DJANGO_ENV}")  # DEBUG LINE

if DJANGO_ENV == "prod":
    from .prod import *
else:
    from .dev import *