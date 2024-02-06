"""Describes File app settings."""

from django.apps import AppConfig


class FileConfig(AppConfig):
    """Config for File app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "file"
