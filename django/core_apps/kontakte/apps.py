from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class KontakteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.kontakte"
    verbose_name = _("Kontakte")
