from django.urls import path

from .views import BackupGetPostView, RestorePostView

urlpatterns = [
    path("", BackupGetPostView.as_view(), name="backup-list-create"),
    path("restore/", RestorePostView.as_view(), name="restore-create"),
]
