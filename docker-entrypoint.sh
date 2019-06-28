#!/usr/bin/env bash

echo "Waiting for MySQL to be ready..."

while ! nc -z db 3306; do
    sleep 0.5
done

echo "MySQL is up and ready"

# Init DB ab=nd create tables
python manage.py db init
python manage.py db migrate
python manage.py db upgrade

# Run server
python manage.py runserver
