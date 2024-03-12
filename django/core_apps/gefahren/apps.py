from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GefahrenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.gefahren"
    verbose_name = _("Gefahren")
