"""URL configuration for Api app."""

from django.urls import path

from api.constants import HTTPMethod
from api.views import FileViewSet

urlpatterns = (
    path(
        "upload/",
        FileViewSet.as_view({HTTPMethod.POST: "create"}),
        name="upload",
    ),
    path(
        "files/",
        FileViewSet.as_view({HTTPMethod.GET: "list"}),
        name="files",
    ),
)
