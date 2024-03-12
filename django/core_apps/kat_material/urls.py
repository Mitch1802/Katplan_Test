from django.urls import path

from .views import KatMaterialListCreateView, KatMaterialRetrieveUpdateDestroyView

urlpatterns = [
    path("", KatMaterialListCreateView.as_view(), name="katmaterial-list-create"),
    path(
        "<uuid:id>/",
        KatMaterialRetrieveUpdateDestroyView.as_view(),
        name="katmaterial-retrieve-update-destroy",
    ),
]
