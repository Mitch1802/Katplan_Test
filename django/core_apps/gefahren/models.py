from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel
from core_apps.rollen.models import Rolle
from core_apps.massnahmen.models import Massnahme
from core_apps.dokumente.models import Dokument


class Gefahr(TimeStampedModel):
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    beschreibung = models.TextField(verbose_name=_("Beschreibung"), blank=True)
    ausloeser = models.CharField(verbose_name=_("Auslöser"), max_length=255, blank=True)
    feld1Name = models.CharField(verbose_name=_("Feld 1 Name"), max_length=255, blank=True)
    feld1Value = models.CharField(verbose_name=_("Feld 1 Wert"), max_length=255, blank=True)
    feld2Name = models.CharField(verbose_name=_("Feld 2 Name"), max_length=255, blank=True)
    feld2Value = models.CharField(verbose_name=_("Feld 2 Wert"), max_length=255, blank=True)
    feld3Name = models.CharField(verbose_name=_("Feld 3 Name"), max_length=255, blank=True)
    feld3Value = models.CharField(verbose_name=_("Feld 3 Wert"), max_length=255, blank=True)
    feld4Name = models.CharField(verbose_name=_("Feld 4 Name"), max_length=255, blank=True)
    feld4Value = models.CharField(verbose_name=_("Feld 4 Wert"), max_length=255, blank=True)
    feld5Name = models.CharField(verbose_name=_("Feld 5 Name"), max_length=255, blank=True)
    feld5Value = models.CharField(verbose_name=_("Feld 5 Wert"), max_length=255, blank=True)
    folgen = models.CharField(verbose_name=_("Folgen"), max_length=255, blank=True)
    gefahren = models.CharField(verbose_name=_("Gefahren"), max_length=255, blank=True)
    rollen = models.ManyToManyField(Rolle, through='GefRollen', related_name="gef_rollen", blank=True)
    massnahmen = models.ManyToManyField(Massnahme, through='GefMassnahmen', related_name="gef_massnahmen", blank=True)
    dokumente = models.ManyToManyField(Dokument, through='GefDokumente', related_name="gef_dokumente", blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["kuerzel"]


class GefRollen(models.Model):
    gef_id = models.ForeignKey(Gefahr, on_delete=models.CASCADE)
    rol_id = models.ForeignKey(Rolle, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.gef_id.__str__(), self.rol_id.__str__())
    

class GefMassnahmen(models.Model):
    gef_id = models.ForeignKey(Gefahr, on_delete=models.CASCADE)
    mas_id = models.ForeignKey(Massnahme, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.gef_id.__str__(), self.mas_id.__str__())
    

class GefDokumente(models.Model):
    gef_id = models.ForeignKey(Gefahr, on_delete=models.CASCADE)
    dok_id = models.ForeignKey(Dokument, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.gef_id.__str__(), self.dok_id.__str__())



