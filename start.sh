#!/usr/bin/env bash

set -e

echo $(date '+%F %T.%3N %Z') "[django] INFO: running start.sh"

env=${APP_ENV:-dev}

if [ $env = "prod" ]
then
    echo $(date '+%F %T.%3N %Z') "[django] INFO: running production environment"
    gunicorn edcilo_com.wsgi:application --bind 0.0.0.0:8000 --workers 3
else
    echo $(date '+%F %T.%3N %Z') "[django] INFO: running develop environment"
    python manage.py runserver 0.0.0.0:8000
fi
