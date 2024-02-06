"""Decribes admin panel settings."""

from django.contrib import admin

from file.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    """Admin panel settings for File model."""

    list_display = (
        "id",
        "file",
        "uploaded_at",
        "processed",
    )
    search_fields = ("file",)
    list_filter = ("processed",)
    empty_value_display = "-empty-"
