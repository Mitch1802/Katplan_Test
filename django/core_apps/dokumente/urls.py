from django.urls import path

from .views import DokumentListCreateView, DokumentRetrieveUpdateDestroyView

urlpatterns = [
    path("", DokumentListCreateView.as_view(), name="dokument-list-create"),
    path(
        "<uuid:id>/",
        DokumentRetrieveUpdateDestroyView.as_view(),
        name="dokument-retrieve-update-destroy",
    ),
]
