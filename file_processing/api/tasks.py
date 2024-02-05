from celery import shared_task
from django.shortcuts import get_object_or_404

from file.models import File


@shared_task
def process_file(file_id):
    file = get_object_or_404(File, pk=file_id)
    print(f'File {file} processed')
    return True

