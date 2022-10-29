#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn muscatalog.wsgi:application -c ./config/gunicorn.conf.py
