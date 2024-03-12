from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel
from core_apps.rollen.models import Rolle
from core_apps.massnahmen.models import Massnahme
from core_apps.gefahren.models import Gefahr


class Katastrophe(TimeStampedModel):
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    beschreibung = models.TextField(verbose_name=_("Beschreibung"), blank=True)
    rollen = models.ManyToManyField(Rolle, through='KatRollen', related_name="kat_rollen", blank=True)
    massnahmen = models.ManyToManyField(Massnahme, through='KatMassnahmen', related_name="kat_massnahmen", blank=True)
    gefahren = models.ManyToManyField(Gefahr, through='KatGefahren', related_name="kat_gefahren", blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["kuerzel"]


class KatRollen(models.Model):
    kat_id = models.ForeignKey(Katastrophe, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rolle, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.kat_id.__str__(), self.rol_id.__str__())
    

class KatMassnahmen(models.Model):
    kat_id = models.ForeignKey(Katastrophe, on_delete=models.CASCADE)
    mas_id = models.ForeignKey(Massnahme, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.kat_id.__str__(), self.mas_id.__str__())
    

class KatGefahren(models.Model):
    kat_id = models.ForeignKey(Katastrophe, on_delete=models.CASCADE)
    gef_id = models.ForeignKey(Gefahr, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.kat_id.__str__(), self.gef_id.__str__())



