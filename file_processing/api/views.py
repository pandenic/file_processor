from api.constants import HTTPMethods
from api.mixins import ListCreateViewSet
from api.serializers import FileSerializer
from api.tasks import process_file
from file.models import File


class FileViewSet(ListCreateViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = (
        HTTPMethods.GET,
        HTTPMethods.POST,
    )

    def perform_create(self, serializer):
        instance = serializer.save()
        process_file(instance.id).delay()
