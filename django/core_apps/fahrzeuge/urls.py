from django.urls import path

from .views import FahrzeugListCreateView, FahrzeugRetrieveUpdateDestroyView

urlpatterns = [
    path("", FahrzeugListCreateView.as_view(), name="fahrzeug-list-create"),
    path(
        "<uuid:id>/",
        FahrzeugRetrieveUpdateDestroyView.as_view(),
        name="fahrzeug-retrieve-update-destroy",
    ),
]
