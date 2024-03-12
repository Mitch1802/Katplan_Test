import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import KatMaterial
from .renderers import KatMaterialienJSONRenderer, KatMaterialJSONRenderer
from .serializers import KatMaterialSerializer
from .permissions import IsVerwaltungOrReadOnly

logger = logging.getLogger(__name__)


class KatMaterialListCreateView(generics.ListCreateAPIView):
    queryset = KatMaterial.objects.all()
    serializer_class = KatMaterialSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [KatMaterialienJSONRenderer]

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        return Response({
            'main': mod_serializer.data
        })


class KatMaterialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KatMaterial.objects.all()
    serializer_class = KatMaterialSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [KatMaterialJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'katmaterial': serializer.data
        })
