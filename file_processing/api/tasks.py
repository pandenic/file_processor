"""Describes Celery tasks for file processing."""

from django.db import transaction
from django.shortcuts import get_object_or_404

from file.models import File
from file_processing import celery_app


@celery_app.task
@transaction.atomic
def process_file_image(file_id):
    """Process files of image file type."""
    file = get_object_or_404(File, pk=file_id)
    print("image")
    file.processed = True
    file.save()


@celery_app.task
@transaction.atomic
def process_file_text(file_id):
    """Process files of text file type."""
    file = get_object_or_404(File, pk=file_id)
    print("text")
    file.processed = True
    file.save()


@celery_app.task
@transaction.atomic
def process_file_other(file_id):
    """Process files of any file type."""
    file = get_object_or_404(File, pk=file_id)
    print("other")
    file.processed = True
    file.save()


CELERY_FILE_TASKS_MAP = {
    "image": process_file_image,
    "text": process_file_text,
    "other": process_file_other,
}
