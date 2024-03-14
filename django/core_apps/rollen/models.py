from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel
from core_apps.kontakte.models import Kontakt


class Rolle(TimeStampedModel):
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    beschreibung = models.TextField(verbose_name=_("Beschreibung"), blank=True)
    erreichbarkeit = models.ManyToManyField(Kontakt, through='RolleKontaktErreichbarkeit', related_name="rol_erreichbarkeit", blank=True)
    notruf = models.CharField(verbose_name=_("Notruf"), max_length=255, blank=True)
    aufgaben = models.TextField(verbose_name=_("Aufgaben"), blank=True)
    verstaendigung = models.ManyToManyField(Kontakt, through='RolleKontaktVerstaendigung', related_name="rol_verstaendigung", blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["kuerzel"]


class RolleKontaktErreichbarkeit(models.Model):
    rol_id = models.ForeignKey(Rolle, on_delete=models.CASCADE)
    kon_id = models.ForeignKey(Kontakt, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.rol_id.__str__(), self.kon_id.__str__())


class RolleKontaktVerstaendigung(models.Model):
    rol_id = models.ForeignKey(Rolle, on_delete=models.CASCADE)
    kon_id = models.ForeignKey(Kontakt, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.rol_id.__str__(), self.kon_id.__str__())

