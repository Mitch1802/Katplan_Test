import os
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from drf_extra_fields.fields import Base64ImageField

from core_apps.common.models import TimeStampedModel


class Fahrzeug(TimeStampedModel):
    def file_name_change(instance, filename):
        ext = filename.split(".")[-1].lower()

        if ext not in ["jpg", "png"]:
            raise ValidationError(f"invalid file extension: {filename}")

        if instance.id:
            filename = f"{instance.id}.{ext}"
        else:
            filename = f"{filename}.{ext}"
        return os.path.join("fahrzeuge", filename)
    
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    # foto = models.ImageField(
    #     verbose_name=_("Foto"), upload_to=file_name_change, default="/fahrzeuge/default.png"
    # )
    foto = Base64ImageField(verbose_name=_("Foto"))
    fahrzeug = models.BooleanField(verbose_name=_("Fahrzeug"), default=False)
    anhaenger = models.BooleanField(verbose_name=_("Anhänger"), default=False)
    type = models.CharField(verbose_name=_("Type"), max_length=255, blank=True)
    lenkerberechtigung = models.CharField(
        verbose_name=_("Lenkerberechtigung"), max_length=1, blank=True
    )
    stationierung = models.CharField(
        verbose_name=_("Stationierung"), max_length=255, blank=True
    )
    personenkapazitaet = models.IntegerField(
        verbose_name=_("Personen Kapazität"), null=True, blank=True
    )
    treibstoff = models.CharField(
        verbose_name=_("Treibstoff"), max_length=50, blank=True
    )
    nutzlast = models.IntegerField(verbose_name=_("Nutzlast"), null=True, blank=True)
    ladebordwand = models.BooleanField(verbose_name=_("Ladebordwand"), default=False)
    ladekran = models.BooleanField(verbose_name=_("Ladekran"), default=False)
    wassertank = models.CharField(
        verbose_name=_("Wassertank"), max_length=255, blank=True
    )
    wassertankAbnehmbar = models.BooleanField(
        verbose_name=_("Wassertank abnehmar"), default=False
    )
    geschlossenerAufbau = models.BooleanField(
        verbose_name=_("Geschlossener Aufbau"), default=False
    )
    wechselaufbau = models.TextField(verbose_name=_("Wechselaufbau"), blank=True)
    anhaengervorrichtung = models.CharField(
        verbose_name=_("Anhängervorrichtung"), max_length=255, blank=True
    )

    def __str__(self):
        return f"{self.name}"
