from django.urls import path

from .views import KatastropheListCreateView, KatastropheRetrieveUpdateDestroyView

urlpatterns = [
    path("", KatastropheListCreateView.as_view(), name="katastrophe-list-create"),
    path(
        "<uuid:id>/",
        KatastropheRetrieveUpdateDestroyView.as_view(),
        name="katastrophe-retrieve-update-destroy",
    ),
]
