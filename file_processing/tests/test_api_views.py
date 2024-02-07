import shutil
import tempfile
import sys
from io import StringIO

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APITestCase, APIClient
from django.test import override_settings
from django.urls import reverse_lazy
from django.conf import settings

from file.models import File


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class ApiViewsTests(APITestCase):

    @classmethod
    def tearDownClass(cls):
        """Delete test dirs."""
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        super().tearDownClass()

    def setUp(self):
        self.client = APIClient()

    def test_post_request_upload_create_db_instance(self):
        test_file = b"Test file"
        uploaded_file = SimpleUploadedFile(
            name="file_example",
            content=test_file,
            content_type="text/plain",
        )
        url = reverse_lazy("upload")

        file_count = File.objects.count()
        self.client.post(url, {'file': uploaded_file})
        self.assertEqual(File.objects.count(), file_count + 1)

    def test_post_request_run_celery_tasks(self):
        test_file = b"Test file"
        uploaded_file = SimpleUploadedFile(
            name="file_example",
            content=test_file,
            content_type="text/plain",
        )
        url = reverse_lazy("upload")
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            self.client.post(url, {'file': uploaded_file})
        except Exception:
            sys.stdout = sys.__stdout__
            raise Exception
        self.assertNotEqual(captured_output.getvalue(), '')
