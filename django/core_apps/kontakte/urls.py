from django.urls import path

from .views import KontaktListCreateView, KontaktRetrieveUpdateDestroyView

urlpatterns = [
    path("", KontaktListCreateView.as_view(), name="kontakt-list-create"),
    path(
        "<uuid:id>/",
        KontaktRetrieveUpdateDestroyView.as_view(),
        name="kontakt-retrieve-update-destroy",
    ),
]
