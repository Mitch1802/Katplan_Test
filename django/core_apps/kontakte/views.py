import logging

from django.http import Http404
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Kontakt
from .renderers import KontakteJSONRenderer, KontaktJSONRenderer
from .serializers import KontaktSerializer
from .permissions import IsVerwaltungOrReadOnly

logger = logging.getLogger(__name__)


class KontaktListCreateView(generics.ListCreateAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [KontakteJSONRenderer]

    # def perform_create(self, serializer):
    #     serializer.save()
    #     logger.info(
    #         f"kontakt {serializer.data.get('kuerzel')} - {serializer.data.get('name')} created by {self.request.user.username}"
    #     )

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        return Response({
            'main': mod_serializer.data
        })


class KontaktRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kontakt.objects.all()
    serializer_class = KontaktSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [KontaktJSONRenderer]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'kontakt': serializer.data
        })
