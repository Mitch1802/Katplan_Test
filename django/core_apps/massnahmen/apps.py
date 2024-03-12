from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MassnahmenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.massnahmen"
    verbose_name = _("Massnahmen")
