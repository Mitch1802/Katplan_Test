from django.urls import path

from .views import GefahrenRetrieveUpdateDestroyView, GefahrListCreateView

urlpatterns = [
    path("", GefahrListCreateView.as_view(), name="gefahr-list-create"),
    path(
        "<uuid:id>/",
        GefahrenRetrieveUpdateDestroyView.as_view(),
        name="gefahren-retrieve-update-destroy",
    ),
]
