#!/bin/sh

python manage.py migrate
gunicorn muscatalog.wsgi:application -c ./config/gunicorn.conf.py
