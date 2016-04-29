#!/bin/sh

python3 manage.py makemigrations --settings=dorothy.settings.staging
python3 manage.py migrate --settings=dorothy.settings.staging
python3 manage.py collectstatic --noinput --settings=dorothy.settings.staging
gunicorn dorothy.wsgi:application -w 4 -t 120 -e DJANGO_SETTINGS_MODULE=dorothy.settings.staging -b :8004

#python3 manage.py runserver 0.0.0.0:8004 --settings=dorothy.settings.staging