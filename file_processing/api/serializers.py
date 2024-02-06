"""Describes custom serializers for an Api app."""

from rest_framework import serializers

from file.models import File


class FileSerializer(serializers.ModelSerializer):
    """Serialize requests for File model."""

    class Meta:
        """Describe settings for FileSerializer."""

        model = File
        fields = (
            "file",
            "uploaded_at",
            "processed",
        )
        read_only_fields = (
            "uploaded_at",
            "processed",
        )
