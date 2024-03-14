from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel
from core_apps.kontakte.models import Kontakt
from core_apps.fahrzeuge.models import Fahrzeug


class Massnahme(TimeStampedModel):
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    beschreibung = models.TextField(verbose_name=_("Beschreibung"), blank=True)
    kategorie = models.CharField(verbose_name=_("Kategorie"), max_length=255, blank=True)
    verantwortung = models.CharField(verbose_name=_("Verantwortung"), max_length=255, blank=True)
    verstaendigung = models.ManyToManyField(Kontakt, through='MasKontakte', related_name="mas_kontakte", blank=True)
    staerke = models.IntegerField(verbose_name=_("Stärke"), null=True, blank=True)
    fahrzeuge = models.ManyToManyField(Fahrzeug, through='MasFahrzeuge', related_name="mas_fahrzeuge", blank=True)
    feld1Name = models.CharField(verbose_name=_("Feld 1 Name"), max_length=255, blank=True)
    feld1Value = models.CharField( verbose_name=_("Feld 1 Wert"), max_length=255, blank=True)
    feld2Name = models.CharField(verbose_name=_("Feld 2 Name"), max_length=255, blank=True)
    feld2Value = models.CharField(verbose_name=_("Feld 2 Wert"), max_length=255, blank=True)
    feld3Name = models.CharField(verbose_name=_("Feld 3 Name"), max_length=255, blank=True)
    feld3Value = models.CharField(verbose_name=_("Feld 3 Wert"), max_length=255, blank=True)
    feld4Name = models.CharField(verbose_name=_("Feld 4 Name"), max_length=255, blank=True)
    feld4Value = models.CharField(verbose_name=_("Feld 4 Wert"), max_length=255, blank=True)
    feld5Name = models.CharField(verbose_name=_("Feld 5 Name"), max_length=255, blank=True)
    feld5Value = models.CharField(verbose_name=_("Feld 5 Wert"), max_length=255, blank=True)
    durchfuehrung = models.TextField(verbose_name=_("Durchführung"), blank=True)
    rueckbau = models.TextField(verbose_name=_("Rückbau"), blank=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        ordering = ["kuerzel"]


class MasKontakte(models.Model):
    mas_id = models.ForeignKey(Massnahme, on_delete=models.CASCADE)
    kon_id = models.ForeignKey(Kontakt, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.mas_id.__str__(), self.kon_id.__str__())


class MasFahrzeuge(models.Model):
    mas_id = models.ForeignKey(Massnahme, on_delete=models.CASCADE)
    fah_id = models.ForeignKey(Fahrzeug, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.mas_id.__str__(), self.fah_id.__str__())