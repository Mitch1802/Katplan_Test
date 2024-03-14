import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Massnahme
from .renderers import MassnahmeJSONRenderer, MassnahmenJSONRenderer
from .serializers import MassnahmeSerializer
from .permissions import IsVerwaltungOrReadOnly

from core_apps.kontakte.models import Kontakt
from core_apps.fahrzeuge.models import Fahrzeug

from core_apps.kontakte.serializers import KontaktSerializer
from core_apps.fahrzeuge.serializers import FahrzeugSerializer

logger = logging.getLogger(__name__)


class MassnahmeListCreateView(generics.ListCreateAPIView):
    queryset = Massnahme.objects.all()
    serializer_class = MassnahmeSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [MassnahmenJSONRenderer]

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        kon_queryset = Kontakt.objects.all()
        fah_queryset = Fahrzeug.objects.all()
        
        kon_serializer = KontaktSerializer(kon_queryset, many=True)
        fah_serializer = FahrzeugSerializer(fah_queryset, many=True)

        return Response({
            'main': mod_serializer.data,
            'kontakte': kon_serializer.data,
            'fahrzeuge': fah_serializer.data
        })


class MassnahmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Massnahme.objects.all()
    serializer_class = MassnahmeSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [MassnahmeJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        kon_queryset = Kontakt.objects.all()
        fah_queryset = Fahrzeug.objects.all()
        
        kon_serializer = KontaktSerializer(kon_queryset, many=True)
        fah_serializer = FahrzeugSerializer(fah_queryset, many=True)
        
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'massnahme': serializer.data,
            'kontakte': kon_serializer.data,
            'fahrzeuge': fah_serializer.data
        })
