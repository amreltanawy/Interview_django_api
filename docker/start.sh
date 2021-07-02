#!/bin/bash

export DJANGO_SUPERUSER_PASSWORD=test3241 && \
export USERNAME_FIELD=admin@genifyTask.io && \
export DJANGO_SUPERUSER_EMAIL=admin@genifyTask.io && \
python /code/MLWrapper/manage.py makemigrations api && \
python /code/MLWrapper/manage.py makemigrations && \
python /code/MLWrapper/manage.py migrate && \
python /code/MLWrapper/manage.py createsuperuser --username admin@genifyTask.io --noinput && \
python /code/MLWrapper/manage.py generate_swagger -f json swagger.json && \
python /code/MLWrapper/manage.py runserver 0.0.0.0:8000