"""Describes custom views for Api app."""
import os

from api.constants import HTTPMethods
from api.mixins import ListCreateViewSet
from api.serializers import FileSerializer
from file.models import File
from file.tasks import CELERY_FILE_TASKS_MAP
from file_processing.settings import ALLOWED_FILE_TYPE


class FileViewSet(ListCreateViewSet):
    """Perform list and create operations for the File model."""

    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = (
        HTTPMethods.GET,
        HTTPMethods.POST,
    )

    def perform_create(self, serializer):
        """Perform actions during save an instance of File model."""
        instance = serializer.save()
        for filetype, extensions in ALLOWED_FILE_TYPE.items():
            root, ext = os.path.splitext(instance.file.name)
            if ext in extensions:
                CELERY_FILE_TASKS_MAP[filetype].delay(instance.id)
                return
        CELERY_FILE_TASKS_MAP["other"].delay(instance.id)
