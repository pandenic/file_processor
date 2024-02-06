"""Describes models of File app."""
from django.conf import settings
from django.db import models


class File(models.Model):
    """Describe a model which stores information about files."""

    file = models.FileField(
        verbose_name="File",
        help_text="File to upload",
        upload_to=settings.FILES_SAVE_LOCATION,
    )
    uploaded_at = models.DateTimeField(
        verbose_name="Upload date",
        help_text="File upload date",
        auto_now_add=True,
    )
    processed = models.BooleanField(
        verbose_name="Is processed",
        help_text="Shows state of file processing",
        default=False,
    )

    class Meta:
        """Describe settings for File model."""

        ordering = ("-uploaded_at",)
        verbose_name = "File"
        verbose_name_plural = "Files"

    def __str__(self):
        """Show a name of a file."""
        return self.file.name
