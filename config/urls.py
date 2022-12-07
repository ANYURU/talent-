from django.contrib import admin
from django.urls import (
    include,
    path,
)

urlpatterns = [
    path("", include("apps.core.urls")),
    path("api/v1/", include("apps.talentapi.urls")),
    path("admin/", admin.site.urls)
]
