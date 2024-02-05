#!/bin/bash
poetry run python manage.py makemigrations;
yes | poetry run python manage.py migrate
poetry run gunicorn --bind 0:8000 file_processing.wsgi;
