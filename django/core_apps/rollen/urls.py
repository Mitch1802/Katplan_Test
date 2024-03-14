from django.urls import path

from .views import RolleListCreateView, RolleRetrieveUpdateDestroyView

urlpatterns = [
    path("", RolleListCreateView.as_view(), name="rolle-list-create"),
    path(
        "<uuid:id>/",
        RolleRetrieveUpdateDestroyView.as_view(),
        name="rolle-retrieve-update-destroy",
    ),
]
