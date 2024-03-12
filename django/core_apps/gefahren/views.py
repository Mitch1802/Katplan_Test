import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Gefahr
from .renderers import GefahrenJSONRenderer, GefahrJSONRenderer
from .serializers import GefahrSerializer
from .permissions import IsVerwaltungOrReadOnly

from core_apps.dokumente.models import Dokument
from core_apps.massnahmen.models import Massnahme
from core_apps.rollen.models import Rolle

from core_apps.dokumente.serializers import DokumentSerializer
from core_apps.massnahmen.serializers import MassnahmeSerializer
from core_apps.rollen.serializers import RolleSerializer

logger = logging.getLogger(__name__)


class GefahrListCreateView(generics.ListCreateAPIView):
    queryset = Gefahr.objects.all()
    serializer_class = GefahrSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [GefahrenJSONRenderer]

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        rol_queryset = Rolle.objects.all()
        mas_queryset = Massnahme.objects.all()
        dok_queryset = Dokument.objects.all()
        
        dok_serializer = DokumentSerializer(dok_queryset, many=True)
        mas_serializer = MassnahmeSerializer(mas_queryset, many=True)
        rol_serializer = RolleSerializer(rol_queryset, many=True)

        return Response({
            'main': mod_serializer.data,
            'dokumente': dok_serializer.data,
            'massnahmen': mas_serializer.data,
            'rollen': rol_serializer.data
        })


class GefahrenRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gefahr.objects.all()
    serializer_class = GefahrSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [GefahrJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        rol_queryset = Rolle.objects.all()
        mas_queryset = Massnahme.objects.all()
        dok_queryset = Dokument.objects.all()
        
        dok_serializer = DokumentSerializer(dok_queryset, many=True)
        mas_serializer = MassnahmeSerializer(mas_queryset, many=True)
        rol_serializer = RolleSerializer(rol_queryset, many=True)
        
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'gefahr': serializer.data,
            'dokumente': dok_serializer.data,
            'massnahmen': mas_serializer.data,
            'rollen': rol_serializer.data
        })
