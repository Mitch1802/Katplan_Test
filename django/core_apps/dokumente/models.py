import os
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from core_apps.common.models import TimeStampedModel


class Dokument(TimeStampedModel):
    def file_name_change(instance, filename):
        ext = filename.split(".")[-1].lower()

        if ext not in ["pdf"]:
            raise ValidationError(f"invalid file extension: {filename}")

        if instance.id:
            filename = f"{instance.id}.{ext}"
        else:
            filename = f"{filename}.{ext}"
        return os.path.join("dokumente", filename)
    
    kuerzel = models.CharField(verbose_name=_("Kürzel"), max_length=5, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    file = models.FileField(
        verbose_name=_("Dokument"),
        upload_to=file_name_change,
        default="/dokumente/default.pdf",
    )

    def __str__(self):
        return f"{self.name}"
