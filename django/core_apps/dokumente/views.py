import logging

# from django.core.files.storage import default_storage
from django.http import Http404
from rest_framework import generics, permissions, status
# from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Dokument
from .renderers import DokumenteJSONRenderer, DokumentJSONRenderer
from .serializers import DokumentSerializer
from .permissions import IsVerwaltungOrReadOnly

logger = logging.getLogger(__name__)


class DokumentListCreateView(generics.ListCreateAPIView):
    queryset = Dokument.objects.all()
    serializer_class = DokumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    renderer_classes = [DokumenteJSONRenderer]

    def list(self, request):
        mod_queryset = self.filter_queryset(self.get_queryset())
        mod_serializer = self.get_serializer(mod_queryset, many=True)

        return Response({
            'main': mod_serializer.data
        })


class DokumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dokument.objects.all()
    serializer_class = DokumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerwaltungOrReadOnly]
    lookup_field = "id"
    renderer_classes = [DokumentJSONRenderer]
    # parser_classes = [MultiPartParser, FormParser]

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response({
            'dokument': serializer.data
        })

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     if "file" in self.request.FILES:
    #         if instance.file and instance.file.name != "/dokumente/default.pdf":
    #             default_storage.delete(instance.file.path)

    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         instance._prefetched_objects_cache = {}

    #     return Response(serializer.data)
    
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.file and instance.file.name != "/dokumente/default.pdf":
    #         default_storage.delete(instance.file.path)
    #     self.perform_destroy(instance)

    #     return Response(status=status.HTTP_204_NO_CONTENT)