from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path("api/v2/auth/login/", LoginView.as_view(), name="rest_login"),
    path("api/v2/auth/logout/", LogoutView.as_view(), name="rest_logout"),
    path("api/v2/auth/registration/", RegisterView.as_view(), name="rest_register"),
    path("api/v2/users/", include("core_apps.users.urls")),
    path("api/v2/module/", include("core_apps.module.urls")),
    path("api/v2/katastrophen/", include("core_apps.katastrophen.urls")),
    path("api/v2/gefahren/", include("core_apps.gefahren.urls")),
    path("api/v2/rollen/", include("core_apps.rollen.urls")),
    path("api/v2/massnahmen/", include("core_apps.massnahmen.urls")),
    path("api/v2/kontakte/", include("core_apps.kontakte.urls")),
    path("api/v2/dokumente/", include("core_apps.dokumente.urls")),
    path("api/v2/fahrzeuge/", include("core_apps.fahrzeuge.urls")),
    path("api/v2/kmaterial/", include("core_apps.kat_material.urls")),
    path("api/v2/konfiguration/", include("core_apps.konfiguration.urls")),
    path("api/v2/backup/", include("core_apps.backup.urls")),
]
