from rest_framework import generics
from rest_framework.response import Response

from core_apps.katastrophen.models import Katastrophe
from core_apps.gefahren.models import Gefahr
from core_apps.massnahmen.models import Massnahme
from core_apps.rollen.models import Rolle
from core_apps.kontakte.models import Kontakt
from core_apps.dokumente.models import Dokument
from core_apps.fahrzeuge.models import Fahrzeug
from core_apps.kat_material.models import KatMaterial
from core_apps.konfiguration.models import Konfiguration

from core_apps.katastrophen.serializers import KatastropheSerializer
from core_apps.gefahren.serializers import GefahrSerializer
from core_apps.massnahmen.serializers import MassnahmeSerializer
from core_apps.rollen.serializers import RolleSerializer
from core_apps.kontakte.serializers import KontaktSerializer
from core_apps.dokumente.serializers import DokumentSerializer
from core_apps.fahrzeuge.serializers import FahrzeugSerializer
from core_apps.kat_material.serializers import KatMaterialSerializer
from core_apps.konfiguration.serializers import KonfigurationSerializer


class ModulListView(generics.ListAPIView):    
    def list(self, request):
        kat_queryset = Katastrophe.objects.all()
        gef_queryset = Gefahr.objects.all()
        mas_queryset = Massnahme.objects.all()
        rol_queryset = Rolle.objects.all()
        kon_queryset = Kontakt.objects.all()
        dok_queryset = Dokument.objects.all()
        fahr_queryset = Fahrzeug.objects.all()
        kmat_queryset = KatMaterial.objects.all()
        konf_queryset = Konfiguration.objects.all()

        kat_serializer = KatastropheSerializer(kat_queryset, many=True)
        gef_serializer = GefahrSerializer(gef_queryset, many=True)
        mas_serializer = MassnahmeSerializer(mas_queryset, many=True)
        rol_serializer = RolleSerializer(rol_queryset, many=True)
        kon_serializer = KontaktSerializer(kon_queryset, many=True)
        dok_serializer = DokumentSerializer(dok_queryset, many=True)
        fahr_serializer = FahrzeugSerializer(fahr_queryset, many=True)
        kmat_serializer = KatMaterialSerializer(kmat_queryset, many=True)
        konf_serializer = KonfigurationSerializer(konf_queryset, many=True)

        return Response({
            'katastrophen': kat_serializer.data,
            'gefahren': gef_serializer.data,
            'massnahmen': mas_serializer.data,
            'rollen': rol_serializer.data,
            'kontakte': kon_serializer.data,
            'dokumente': dok_serializer.data,
            'fahrzeuge': fahr_serializer.data,
            'kmaterial': kmat_serializer.data,
            'konfiguration': konf_serializer.data,
        })