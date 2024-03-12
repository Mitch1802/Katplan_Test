from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel


class KatMaterial(TimeStampedModel):
    artikel = models.CharField(verbose_name=_("Kürzel"), max_length=255, unique=True)
    bemerkung = models.CharField(verbose_name=_("Bemerkung"), max_length=255, blank=True)
    menge = models.IntegerField(verbose_name=_("Menge"), null=True)
    stationierungsort = models.CharField(
        verbose_name=_("Stadionierungsort"), max_length=255, blank=True
    )

    def __str__(self):
        return f"{self.artikel}"
    
    class Meta:
        ordering = ["artikel"]
