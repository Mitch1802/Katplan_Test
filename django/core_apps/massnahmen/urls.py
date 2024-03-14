from django.urls import path

from .views import MassnahmeListCreateView, MassnahmeRetrieveUpdateDestroyView

urlpatterns = [
    path("", MassnahmeListCreateView.as_view(), name="massnahme-list-create"),
    path(
        "<uuid:id>/",
        MassnahmeRetrieveUpdateDestroyView.as_view(),
        name="massnahme-retrieve-update-destroy",
    ),
]
