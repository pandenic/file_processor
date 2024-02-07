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

    def test_run_celery_tasks_text_file_extension(self):
        url = reverse_lazy("upload")
        text_file = b"Test file"
        uploaded_file_text = SimpleUploadedFile(
            name="file_example.txt",
            content=text_file,
            content_type="text/plain",
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            self.client.post(url, {'file': uploaded_file_text})
        except Exception:
            sys.stdout = sys.__stdout__
            raise Exception
        self.assertEqual(captured_output.getvalue(), 'text\n')

    def test_run_celery_tasks_image_file_extension(self):
        url = reverse_lazy("upload")
        small_gif = (
            b"\x47\x49\x46\x38\x39\x61\x02\x00"
            b"\x01\x00\x80\x00\x00\x00\x00\x00"
            b"\xFF\xFF\xFF\x21\xF9\x04\x00\x00"
            b"\x00\x00\x00\x2C\x00\x00\x00\x00"
            b"\x02\x00\x01\x00\x00\x02\x02\x0C"
            b"\x0A\x00\x3B"
        )
        uploaded_file_image = SimpleUploadedFile(
            name="file_example.gif",
            content=small_gif,
            content_type="text/plain",
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            self.client.post(url, {'file': uploaded_file_image})
        except Exception:
            sys.stdout = sys.__stdout__
            raise Exception
        self.assertEqual(captured_output.getvalue(), 'image\n')

    def test_run_celery_tasks_other_file_extension(self):
        url = reverse_lazy("upload")
        text_file = b"Test file"
        uploaded_file_text = SimpleUploadedFile(
            name="file_example",
            content=text_file,
        )
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            self.client.post(url, {'file': uploaded_file_text})
        except Exception:
            sys.stdout = sys.__stdout__
            raise Exception
        self.assertEqual(captured_output.getvalue(), 'other\n')