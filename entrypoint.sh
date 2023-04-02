#!/bin/sh
#python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

python manage.py loaddata admin_interface_theme_django.json
python manage.py loaddata admin_interface_theme_bootstrap.json
python manage.py loaddata admin_interface_theme_foundation.json
python manage.py loaddata admin_interface_theme_uswds.json

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn egatcore.wsgi:application --bind 0.0.0.0:8000