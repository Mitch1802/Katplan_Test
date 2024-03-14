from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class KatMaterialConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.kat_material"
    verbose_name = _("Katastrophen Material")
