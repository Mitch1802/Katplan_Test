from .base import *  
from .base import env

ADMINS = [("Ing. Michael Reichenauer", "office@michael-web.at")]

# CSRF_TRUSTED_ORIGIS = env("DJANGO_CSRF_TRUSTED_ORIGINS").split(",")

SECRET_KEY = env("DJANGO_SECRET_KEY")

# ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(",")
ALLOWED_HOSTS = ["*"]

ADMIN_URL = "notused/"

DATABASES = {"default": env.db("DATABASE_URL")}

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 518400

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

SITE_NAME = "Katplan"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
