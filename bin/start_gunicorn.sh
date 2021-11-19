#!/bin/bash

# https://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/
NAME="resume.smart-billing.ru"                    # Name of the application
DJANGODIR=/home/www/code/backend/resume           # Django project directory

echo "Starting $NAME"

# Activate the virtual environment
cd $DJANGODIR

source ./env/bin/activate
exec gunicorn -c "./resume_app/gunicorn_config.py" resume_app.wsgi