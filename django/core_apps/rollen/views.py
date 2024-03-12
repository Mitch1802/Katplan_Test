import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Rolle
from .renderers import RolleJSONRenderer, RollenJSONRenderer
from .serializers import RolleSerializer
from .permissions import IsVerwaltungOrReadOnly

from core_apps.kontakte.models import Kontakt
from core_apps.kontakte.serializers import KontaktSerializer

logger = logging.getLogger(__name__)


class RolleListCreateView(generics.ListCreateAPIView):
    queryset = Rolle.objects.all()
    serializer_class = RolleSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [RollenJSONRenderer]

    def list(self, request):
        mod_queryset = self.get_queryset()
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        kon_queryset = Kontakt.objects.all()
        kon_serializer = KontaktSerializer(kon_queryset, many=True)

        return Response({
            'main': mod_serializer.data,
            'kontakte': kon_serializer.data
        })


class RolleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rolle.objects.all()
    serializer_class = RolleSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [RolleJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        kon_queryset = Kontakt.objects.all()
        kon_serializer = KontaktSerializer(kon_queryset, many=True)
        
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'rolle': serializer.data,
            'kontakte': kon_serializer.data
        })
