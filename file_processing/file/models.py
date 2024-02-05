from django.db import models


class File(models.Model):
    file = models.FileField(
        verbose_name='File',
        help_text='File to upload',
        upload_to='files/'
    )
    uploaded_at = models.DateTimeField(
        verbose_name='Upload date',
        help_text='File upload date',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        verbose_name='Is processed',
        help_text='Shows state of file processing',
        default=False,
    )

    class Meta:
        """Describe settings for the Tag model."""

        ordering = ('uploaded_at',)
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        """Show a name of a file."""
        return self.name
