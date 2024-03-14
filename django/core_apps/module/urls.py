from django.urls import path

from .views import ModulListView

urlpatterns = [
    path("", ModulListView.as_view(), name="modul-list"),
]
