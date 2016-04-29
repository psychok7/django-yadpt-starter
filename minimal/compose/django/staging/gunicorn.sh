#!/bin/sh

python3 manage.py makemigrations --settings={{ project_name }}.settings.staging
python3 manage.py migrate --settings={{ project_name }}.settings.staging
python3 manage.py collectstatic --noinput --settings={{ project_name }}.settings.staging
gunicorn {{ project_name }}.wsgi:application -w 4 -t 120 -e DJANGO_SETTINGS_MODULE={{ project_name }}.settings.staging -b :8004

#python3 manage.py runserver 0.0.0.0:8004 --settings={{ project_name }}.settings.staging