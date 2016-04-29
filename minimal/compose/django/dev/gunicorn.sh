#!/bin/sh

python3 manage.py makemigrations --settings=dorothy.settings.local
python3 manage.py migrate --settings=dorothy.settings.local
python3 manage.py collectstatic --noinput --settings=dorothy.settings.local
gunicorn dorothy.wsgi:application -w 4 -t 120 -e DJANGO_SETTINGS_MODULE=dorothy.settings.local -b :8000

#python3 manage.py runserver 0.0.0.0:8000 --settings=dorothy.settings.local