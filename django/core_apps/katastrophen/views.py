import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Katastrophe
from .renderers import KatastropheJSONRenderer, KatastrophenJSONRenderer
from .serializers import KatastropheSerializer
from .permissions import IsVerwaltungOrReadOnly

from core_apps.gefahren.models import Gefahr
from core_apps.massnahmen.models import Massnahme
from core_apps.rollen.models import Rolle

from core_apps.gefahren.serializers import GefahrSerializer
from core_apps.massnahmen.serializers import MassnahmeSerializer
from core_apps.rollen.serializers import RolleSerializer

logger = logging.getLogger(__name__)


class KatastropheListCreateView(generics.ListCreateAPIView):
    queryset = Katastrophe.objects.all()
    serializer_class = KatastropheSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [KatastrophenJSONRenderer]

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        gef_queryset = Gefahr.objects.all()
        mas_queryset = Massnahme.objects.all()
        rol_queryset = Rolle.objects.all()
        
        gef_serializer = GefahrSerializer(gef_queryset, many=True)
        mas_serializer = MassnahmeSerializer(mas_queryset, many=True)
        rol_serializer = RolleSerializer(rol_queryset, many=True)

        return Response({
            'main': mod_serializer.data,
            'gefahren': gef_serializer.data,
            'massnahmen': mas_serializer.data,
            'rollen': rol_serializer.data
        })
        


class KatastropheRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Katastrophe.objects.all()
    serializer_class = KatastropheSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [KatastropheJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        gef_queryset = Gefahr.objects.all()
        mas_queryset = Massnahme.objects.all()
        rol_queryset = Rolle.objects.all()
        
        gef_serializer = GefahrSerializer(gef_queryset, many=True)
        mas_serializer = MassnahmeSerializer(mas_queryset, many=True)
        rol_serializer = RolleSerializer(rol_queryset, many=True)
        
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'katastrophe': serializer.data,
            'gefahren': gef_serializer.data,
            'massnahmen': mas_serializer.data,
            'rollen': rol_serializer.data
        })
