from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel


class Kontakt(TimeStampedModel):
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    funktion = models.CharField(verbose_name=_("Funktion"), max_length=255, blank=True)
    telefon = models.CharField(verbose_name=_("Telefon"), max_length=255, blank=True)
    telefon2 = models.CharField(verbose_name=_("Telefon_2"), max_length=255, blank=True)
    telefon3 = models.CharField(verbose_name=_("Telefon_3"), max_length=255, blank=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["kuerzel"]
