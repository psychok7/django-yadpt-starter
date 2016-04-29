#!/bin/sh

python3 manage.py makemigrations --settings={{ project_name }}.settings.local
python3 manage.py migrate --settings={{ project_name }}.settings.local
python3 manage.py collectstatic --noinput --settings={{ project_name }}.settings.local
gunicorn {{ project_name }}.wsgi:application -w 4 -t 120 -e DJANGO_SETTINGS_MODULE={{ project_name }}.settings.local -b :8000

#python3 manage.py runserver 0.0.0.0:8000 --settings={{ project_name }}.settings.local