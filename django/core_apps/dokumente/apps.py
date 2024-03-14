from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DokumenteConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.dokumente"
    verbose_name = _("Dokumente")
