import os
import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase
from django.test import override_settings
from django.conf import settings

from file.models import File


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class FileModelTest(APITestCase):

    @classmethod
    def tearDownClass(cls):
        """Delete test dirs."""
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def test_model_created_instance_name(self):
        test_file = b"Test file"
        uploaded_file = SimpleUploadedFile(
            name="file_example",
            content=test_file,
            content_type="text/plain",
        )
        file_obj = File.objects.create(
            file=uploaded_file,
        )
        self.assertEqual(str(file_obj), os.path.join(settings.FILES_SAVE_LOCATION, "file_example"))
